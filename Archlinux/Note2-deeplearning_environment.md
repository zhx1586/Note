# Caffe 环境搭建

## 1 安装CUDA

使用AUR源中的CUDA8.0版本

    yaourt -S cuda

并对 ~/.zshrc 进行配置

    export PATH=$PATH:/opt/cuda/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/lib64

测试

    nvcc -V 

## 2 安装cudnn

    yaourt -S cudnn

## 3 安装 BLAS 

    yaourt -S atlas-lapack 

## 4 安装Boost 

    yaourt -S boost 

## 5 安装opencv

    yaourt -S opencv opencv-samples

## 6 安装其他依赖

    yaourt -S protobuf python-protobuf
    yaourt -S google-glog
    yaourt -S gflags
    yaourt -S hdf5
    yaourt -S lmdb leveldb 

## 7 下载caffe源码包

    git clone git://github.com/BVLC/caffe

## 8 编译

    mkdir build
    cd build
    cmake ..
    make all -j8
    make install

## 9 添加到PATH

    export PATH=$PATH:~/test/caffe/build/tools
    export PYTHONPATH=$PYTHONPATH:~/test/caffe/python

    
