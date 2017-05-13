import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# This script is used to compute the testing accuracy for the model. 
# Location: Should be 'examples' folder of caffe
# Usage:
# 1. Create 'output', 'test' and 'temp' folder in examples folder
# 2. Keep all the images to test accuracy in 'test' folder
# 3. Give name to output text file to save the output fo testing
# 3. Run the script, it will generate the text file with name given
# 4. File will have the results



# Make sure that caffe is on the python path:

caffe_root = '../'  # this file is expected to be in {caffe_examples}/root

print caffe_root
import sys

sys.path.insert(0, caffe_root + 'python')

import caffe

# Set the right path to your model definition file, pretrained model, weights

# and the image you would like to classify.

#MODEL_FILE = './examples/cifar10/cifar10_quick.prototxt'  //deploy.prototxt file for our model

MODEL_FILE = './cifar10/cifar10_quick.prototxt'
PRETRAINED = './cifar10/cifar10_quick_iter_5000.caffemodel.h5'

caffe.set_mode_gpu()
f = open('./output/yield.txt', 'w')
save_path = './temp/test.jpg'

for file in os.listdir('./stop'):
	net = caffe.Classifier(MODEL_FILE, PRETRAINED,
				mean=np.load(caffe_root + './examples/cifar10/cifar10_mean.npy').mean(1).mean(1),
		                channel_swap=(2,1,0),                       
				raw_scale=255,
		                image_dims=(32, 32))

	input_image = Image.open('./test/'+file)

	input_image = input_image.resize((32,32), Image.ANTIALIAS)
	input_image.save(save_path)
	input_image = caffe.io.load_image(save_path)

	prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
	classes = {0: 'Speed Limit 35', 1: 'Keep Right', 2: 'Speed Limit 25', 3: 'Signal Ahead', 4: 'Pedestrian Crossing', 5: 'Stop', 6: 'Merge', 7: 'Added Lane', 8: 'Yield'}

	f.write('Prediction for image '+ file + '\n')
	f.write('Predicted Traffic Sign is '+ classes[prediction[0].argmax()] + '\n')
	f.write('Predicted class:'+ str(prediction[0].argmax()) + '\n')
	f.write('Predicted class probabilty:'+ format(round(prediction[0].max()*100, 2))+'%' + '\n\n')

f.close()
