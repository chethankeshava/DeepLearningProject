from PIL import Image

# Uses PIL to resize the images

img = Image.open('PedestrianCrossing.15.png')
img = img.resize((32,32), Image.ANTIALIAS)
img.save('thumbnail.png')
