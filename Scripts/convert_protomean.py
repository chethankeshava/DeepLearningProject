import sys
import numpy as np

sys.path.insert(0, './python')
import caffe

# Used for converting the binaryproto to the npy file
# Use command python convert_protomean.py <binaryproto> <npy output file name>
# Assuming the script and binaryproto are in same folder

if len(sys.argv) != 3:
	print "Usage: python convert_protomean.py proto.mean out.npy"
	sys.exit()

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( sys.argv[1] , 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
out = arr[0]
np.save( sys.argv[2] , out )
