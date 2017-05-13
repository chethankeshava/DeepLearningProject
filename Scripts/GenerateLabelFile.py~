import sys, getopt, json, os

# Used for generating the label files for the image dataset
# Keep the script and the images in the same folder
# Edit the label and value as required
# Label - Name the file should have
# Value - Class of the images
# After running it should have all the images renamed and text file for labels

def main(argv):
    label = 'SpeedLimit35'
    value = '2'
    path = ''
    print 'Creating Label file for ' + label + ' with value ' + value
    title = ''
    all_dicts = []

    count = 1
    outputfile = 'labels.txt'
    with open(outputfile, 'w') as output:
        for file in os.listdir('.'):
            if file.endswith('.png'):
                newName = label + '.' + str(count) + '.png'
                os.rename(file, newName)

                output.write(newName + ' ' + value + '\n')
                print 'Label ' + newName + ' ' + value + ' added to file'
                count = count + 1

    print 'Total ' + str(count-1) + ' files renamed and labels added'

if __name__ == "__main__":
   main(sys.argv[1:])
