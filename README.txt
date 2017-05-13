Traffic Sign Detection

After unzipping the file you should see below structure:
Cifar10DNN.tar.gz
  image dataset used: the images we used for training
  Images : input data images
  label: the label files used while training
  Scripts : Script files used for data preparation and running model
  Caffe Model file (.caffemodel)
  Image mean file (.binaryproto and .npy)
  Lmbd files: Training and testing lmdb files
  Model parameters files (solver, deploy and train prototxt files)
  README.txt

Assuming that you have cloned the git repo of caffe (https://github.com/BVLC/caffe) and it's build and tested.

Loading Caffe model and placing scripts at correct locations:
1. Copy the .caffemodel.h5, mean.npy, and cifar10_quick.prototxt to the caffe/examples/cifar10 folder
2. Copy classify_test.py script to caffe/examples/ folder
2. Copy the rest of the scripts to the caffe root directory

Testing for given input images:
1. Go to Scripts folder and edit the IMAGE_FILE in classify_test.py to point to the correct image.
2. Run the script using command "python classify_test.py"
3. Should show predicted class in the terminal

To test for new images:
1. Either copy the new images the path mentioned in the IMAGE_FILE variable
2. Repeat above steps 2 and 3

To Train for your own image dataset:
1. Create lmdb files:
  a. Copy the training and validation images in caffe/train and caffe/test folder respectively
  b. Keep the train.txt and val.txt in caffe/examples/cifar10/label
  b. Run the 'create_lmdb.sh' from caffe folder
2. Generate mean file:
  a. Update the path for lmdb files in the 'generate_mean.sh' script
  b. Run the script from caffe folder.
  c. Use 'convert_protomean.py' to get .npy file for mean
  d. Copy both binaryproto and npy mean files to caffe/examples/cifar10 folder
3. Train:
  a. Update the model parameter files with relevant path to lmdb and mean files
  b. Change the number of iterations, batch size or other settings from model parameter files
  c. Start training by executing train_quick.sh from caffe folder
4. Testing the model with input images:
  a. Execute the classify_test.py from caffe/examples folder by pointing to correct relevant files.

To get test accuracy for one class at a time:
Refer classify_folders.py for detailed steps.

NOTE: All the scripts have the comments to give more information.
