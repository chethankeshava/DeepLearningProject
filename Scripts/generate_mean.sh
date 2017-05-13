#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12
EXAMPLE=~/caffe/examples/cifar10  #Path to storing the mean file 
DATA=~/caffe/examples/cifar10 #Path to your folder
TOOLS=/home/ubuntu/caffe/build/tools #Path to caffe build tools
$TOOLS/compute_image_mean $EXAMPLE/cifar10_train_lmdb/ $DATA/cifar10_mean.binaryproto
echo "Done."
