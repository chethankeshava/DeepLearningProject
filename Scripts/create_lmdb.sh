#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

EXAMPLE=~/caffe/examples/cifar10 # Path to storing the db file
DATA=~/caffe/examples/cifar10/label  # Path to your folder having label file
TOOLS=~/caffe/build/tools # Path to caffe build tools folder
TRAIN_DATA_ROOT=~/caffe/train/ #Path to training data set images
VAL_DATA_ROOT=~/caffe/test/ #Path to testing data set images
# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
#RESIZE=false
RESIZE=true 
if $RESIZE; then
  RESIZE_HEIGHT=32
  RESIZE_WIDTH=32
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi
if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path where the ImageNet training data is stored."  
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path where the ImageNet validation data is stored."
  exit 1
fi
echo "Creating train lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    $DATA/train.txt \
    $EXAMPLE/cifar10_train_lmdb #name of your train lmdb file

echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $VAL_DATA_ROOT \
    $DATA/val.txt \
    $EXAMPLE/cifar10_test_lmdb #name of your test or val lmdb file
echo "Done."
