# 3D pose using Single RGB camera robot tracking

This script use open pose with tensorflow extension to calculate 2D pose of human. After calucalting 2d pose the lifiting deep pose algorithm is used to estimate the depth 2d points to calculate 3d point cloud. After calculating the 3D points these points are then send to UR Simulator and Webots for Robot Training 

## Installation:
#### ubuntu:
1. First of all install cmake gcc and build essentials by this command
```
	sudo apt update 
	sudo apt-get install git cmake build-essential libusb-1.0-0-dev
	sudo apt install python-numpy
```


2. Install anaconda from its website <https://docs.anaconda.com/anaconda/install/>

3.  Create Conda ENV:

```
	conda create -n  AIMachine
	conda activate AIMachine
	conda install anaconda
	conda install python==3.7.6
	conda install opencv
	conda install tensorflow
```


4. Install libfreenect library :

```
	mkdir bin && cd bin
	git clone https://github.com/OpenKinect/libfreenect
	cd libfreenect
	mkdir build  && cd build
	cmake .. -DBUILD_PYTHON3=ON -DCYTHON_EXECUTABLE=/home/$USER/anaconda3/envs/AIMachine/bin/cython -DCMAKE_INSTALL_PREFIX=/home/$USER/anaconda3/envs/AIMachine -L
	sudo make install
	cd ../wrappers/python
	python setup.py install
	cd ../../../
```

5. Install tf-pose Estimation using these links:

```
	git clone https://github.com/gsethi2409/tf-pose-estimation.git
	cd tf-pose-estimation
	pip install -r requirements.txt
	conda install swig
	cd tf_pose/pafprocess
	swig -python -c++ pafprocess.i && python3 setup.py build_ext --inplace
	cd ../../
	pip install git+https://github.com/adrianc-a/tf-slim.git@remove_contrib
	cd models/graph/cmu
	bash download.sh
	cd ../../..
	python setup.py install
```
