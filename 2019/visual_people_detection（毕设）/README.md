#Set up

##Opencv
1.sudo apt-get install libopencv-dev
2.sudo apt-get install python-opencv

##Dlib
sudo pip install dlib(如果需要配置GPU，需要自行下载编译)

##Openface
1.git clone https://github.com/cmusatyalab/openface.git 
2.安装Openface的依赖库
cd openface
sudo pip install -r requirements.txt

##Torch
git clone https://github.com/torch/distro.git ~/torch --recursive
cd torch
bash install-deps
./install.sh

##配置的环境变量立刻生效：
source ~/.bashrc

##利用luarocks包安装cunn、dpnn、nn、optim、csvigo

##编译openface
python setup.py build
sudo python setup.py install

##下载预训练模型
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 
文件下载好后，放到./models/dlib中。

https://storage.cmusatyalab.org/openface-models/nn4.small2.v1.t7 
文件下载好后，放到./models/openface中。

https://storage.cmusatyalab.org/openface-models/celeb-classifier.nn4.small2.v1.pkl 
文件下载好后，放到./models/openface中。
