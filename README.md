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
  1. mkdir bin && cd bin
  2. git clone https://github.com/OpenKinect/libfreenect
  3. cd libfreenect
  4. mkdir build  && cd build
  5. cmake .. -DBUILD_PYTHON3=ON -DCYTHON_EXECUTABLE=/home/$USER/anaconda3/envs/AIMachine/bin/cython -DCMAKE_INSTALL_PREFIX=/home/$USER/anaconda3/envs/AIMachine -L
  6. sudo make install 
  7. cd ../wrappers/python
  8. python setup.py install
  9. cd ../../../
```

5. Install tf-pose Estimation using these links:

```
  1. git clone https://github.com/gsethi2409/tf-pose-estimation.git
  2. cd tf-pose-estimation
  3. pip install -r requirements.txt
  4. conda install swig
  5. cd tf_pose/pafprocess
  6. swig -python -c++ pafprocess.i && python3 setup.py build_ext --inplace
  7. cd ../../
  8. pip install git+https://github.com/adrianc-a/tf-slim.git@remove_contrib
  9. cd models/graph/cmu
  10. bash download.sh
  11. cd ../../..
  12.python setup.py install
```
