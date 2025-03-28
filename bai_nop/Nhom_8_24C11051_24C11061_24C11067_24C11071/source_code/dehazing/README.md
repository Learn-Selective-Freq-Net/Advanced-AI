
### Setting up environment
~~~
cd ./SFNet
pip install tensorboard einops scikit-image pytorch_msssim opencv-python
cd ./pytorch-gradual-warmup-lr
python setup.py install
cd ..
cd ./Image_dehazing
~~~


### Download the Datasets
- I-Haze [[kaggle](https://kaggle.com/datasets/de50e3b5252e0201b9c247e6c347816211fb4d9c601cfb5c9e51f8c227571a42)]
- O-Haze [[kaggle](https://kaggle.com/datasets/87284bf708291dc77456e0a71ea3b53176b6024ba26f8c1a8b5da97f24a39570)]
- reside-indoor [[gdrive](https://drive.google.com/drive/folders/1pbtfTp29j7Ip-mRzDpMpyopCfXd-ZJhC?usp=sharing), [Baidu](https://pan.baidu.com/s/1jD-TU0wdtSoEb4ki-Cut2A?pwd=1lr0)]
- reside-outdoor [[gdrive](https://drive.google.com/drive/folders/1eL4Qs-WNj7PzsKwDRsgUEzmysdjkRs22?usp=sharing)]
- (Separate SOTS test set if needed) [[gdrive](https://drive.google.com/file/d/16j2dwVIa9q_0RtpIXMzhu-7Q6dwz_D1N/view?usp=sharing), [Baidu](https://pan.baidu.com/s/1R6qWri7sG1hC_Ifj-H6DOQ?pwd=o5sk)]

### Training

#### Training on SOTS-Indoor
~~~
python main.py --data SOTS_Indoor --mode train --data_dir your_path/reside-indoor
~~~


#### Training on SOTS-Outdoor
~~~
python main.py --data SOTS_Outdoor --mode train --data_dir your_path/reside-outdoor --batch_size 8 --num_epoch 30  --save_freq 1 --valid__freq 1
~~~

#### Fine-tuning on I-Haze
~~~
python main.py --data I_Haze --mode train --fine_tune --data_dir "your_path/I-HAZE" --batch_size 2 --num_worker 2 --num_epoch 20 --save_freq 1 --valid_freq 1 --pretrained 'your_path/SOTS_Indoor.pkl'
~~~

#### Fine-tuning on O-Haze
~~~
python main.py --data O_Haze --mode train --fine_tune --data_dir "your_path/O-HAZE" --batch_size 2 --num_worker 2 --num_epoch 20 --save_freq 1 --valid_freq 1 --pretrained 'your_path/SOTS_Outdoor.pkl'
~~~

### Evaluation
#### Download the model 
- SOTS-Indoor [[gdrive](https://drive.google.com/file/d/1UsNrGkWie-PKXcGSA6oFkt0WgnW8Bqsi/view?usp=sharing), [Baidu](https://pan.baidu.com/s/1Z3La73rya9GVQR4STYk_XA?pwd=ods2)]
- SOTS-Outdoor [[gdrive](https://drive.google.com/file/d/16lbhL3fqHeVu-aPkmFSUnaHWQKxmhPz6/view?usp=sharing), [Baidu](https://pan.baidu.com/s/1NEcAus7lOuvtot-00sjxBg?pwd=hkab)]

#### Testing on SOTS-Indoor
~~~
python main.py --data SOTS_Indoor --save_image True --mode test --data_dir your_path/reside-indoor --test_model path_to_its_model
~~~

#### Testing on SOTS-Outdoor
~~~
python main.py --data SOTS_Outdoor --save_image True --mode test --data_dir your_path/reside-outdoor --test_model path_to_ots_model
~~~

#### Testing on I-Haze
~~~
python main.py --data I_Haze --save_image True --mode test --data_dir "your_path/I-HAZE" --test_model path_to_ots_model
~~~

#### Testing on O-Haze
~~~
python main.py --data O_Haze --save_image True --mode test --data_dir "your_path/O-HAZE" --test_model path_to_ots_model
~~~