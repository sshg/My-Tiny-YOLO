# Optimized Tiny YOLO for inland ship detection

Main implementations are included in src folder and mostly titled with depthwise_convolution. Other implementations used for webcam demo are included in src/demo.c.

For network, see cfg/my-yolov2-tiny.cfg.

For data generating, see my_script. The dataset I used to train this network is 13000 inland ship images.

# How to run it

1. Git clone this repo.

2. Open Makefile and set GPU & CUDNN=1. Then make compile. (It needs CUDA & CUDNN dependencies to compile)
   
