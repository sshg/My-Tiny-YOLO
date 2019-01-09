# Optimized Tiny YOLO for inland ship detection

Implementation of tiny-YOLOv2 with depthwise conv layer based on [Darknet](https://pjreddie.com/darknet/). The network was slightly changed for faster detection speed.

For network, see cfg/my-yolov2-tiny.cfg.

For label generating, see my_script. The dataset I used to train this network is 13000 inland ship images.

For pre-trained weight, see backup/my-yolov2-tiny_final.weights.

Remeber to set GPU & CUDNN=1 in Makefile. Then make compile. (It needs CUDA & CUDNN dependencies to compile)
   
