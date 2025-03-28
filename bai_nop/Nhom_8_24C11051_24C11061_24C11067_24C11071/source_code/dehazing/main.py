import os
import torch
import argparse
from torch.backends import cudnn
from models.SFNet import build_net
from eval import _eval
from train import _train
from train_ots import _train_ots

def main(args):
    cudnn.benchmark = True

    if not os.path.exists('results/'):
        os.makedirs(args.model_save_dir)
    if not os.path.exists('results/' + args.model_name + '/'):
        os.makedirs('results/' + args.model_name + '/')
    if not os.path.exists(args.result_dir):
        os.makedirs(args.result_dir)
    mode = [args.mode, args.data]
    model = build_net(mode)
    # print(model)

    if torch.cuda.is_available():
        model.cuda()

    if args.fine_tune:
        # Load model parameters
        state_dict = torch.load(args.pretrained)
        model.load_state_dict(state_dict['model'])
        
        # Freeze Encoder
        for param in model.Encoder.parameters():
            param.requires_grad = False  
        
        # Freeze các phần không cần fine-tune (Convs, ConvsOut, FAM, SCM)
        for param in model.Convs.parameters():
            param.requires_grad = False  
        for param in model.ConvsOut.parameters():
            param.requires_grad = False  
        for param in model.FAM1.parameters():
            param.requires_grad = False  
        for param in model.FAM2.parameters():
            param.requires_grad = False  
        for param in model.SCM1.parameters():
            param.requires_grad = False  
        for param in model.SCM2.parameters():
            param.requires_grad = False  
        
        # Fine-tune Decoder
        for param in model.Decoder.parameters():
            param.requires_grad = True   
        
        # Fine-tune feat_extract (cả phần downsampling & upsampling)
        for param in model.feat_extract.parameters():  
            param.requires_grad = True  

    if args.mode == 'train' and (args.data == 'I_Haze' or args.data == 'O_Haze'):
        _train_ots(model, args)
    elif args.mode == 'train' and args.data == 'SOTS_Indoor':
        _train(model, args)
    elif args.mode == 'train' and args.data == 'SOTS_Outdoor':
        _train_ots(model, args)
    elif args.mode == 'test':
        _eval(model, args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Directories
    parser.add_argument('--model_name', default='SFNet', type=str)
    parser.add_argument('--data_dir', type=str, default='/root/autodl-tmp/SFNet/reside-indoor')
    parser.add_argument('--data', type=str, default='SOTS_Indoor', choices=['SOTS_Indoor', 'SOTS_Outdoor', 'I_Haze', 'O_Haze'])
    parser.add_argument('--mode', default='train', choices=['train', 'test'], type=str)

    # Fine-tune
    parser.add_argument('--pretrained', type=str, default='')
    
    # Train
    parser.add_argument('--batch_size', type=int, default=4)
    parser.add_argument('--learning_rate', type=float, default=1e-4)
    parser.add_argument('--weight_decay', type=float, default=0)
    parser.add_argument('--num_epoch', type=int, default=300)
    parser.add_argument('--print_freq', type=int, default=100)
    parser.add_argument('--num_worker', type=int, default=8)
    parser.add_argument('--save_freq', type=int, default=10)
    parser.add_argument('--valid_freq', type=int, default=10)
    parser.add_argument('--resume', type=str, default='')
    parser.add_argument('--fine_tune', action='store_true', help='Enable fine-tune mode')

    # Test
    parser.add_argument('--test_model', type=str, default='/root/autodl-tmp/SFNet/SOTS-Indoor.pkl')
    parser.add_argument('--save_image', type=bool, default=False, choices=[True, False])

    args = parser.parse_args()
    args.model_save_dir = os.path.join('results/', args.model_name, args.data, 'Training-Results/')
    args.result_dir = os.path.join('results/', args.model_name, 'images', args.data)
    if not os.path.exists(args.model_save_dir):
        os.makedirs(args.model_save_dir)
    command = 'cp ' + 'models/layers.py ' + args.model_save_dir
    os.system(command)
    command = 'cp ' + 'models/SFNet.py ' + args.model_save_dir
    os.system(command)
    command = 'cp ' + 'train.py ' + args.model_save_dir
    os.system(command)
    command = 'cp ' + 'main.py ' + args.model_save_dir
    os.system(command)
    print(args)
    main(args)
