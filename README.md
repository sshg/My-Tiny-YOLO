# darknet mobilenet

Implement depth-wise conv layer based on darknet framework. See cfg/

1. git clone this repo

2. open Makefile ,set GPU=1 、CUDNN=1 and make compile

3. network example:cfg/mobilenet_imagenet.cfg 

4. main implement :depthwise_convolutional_kernels.cu  depthwise_convolutional_layer.c depthwise_convolutional_layer.h
