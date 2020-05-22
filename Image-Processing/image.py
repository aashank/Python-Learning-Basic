from PIL import Image, ImageFilter

img=Image.open('./astro.jpg')
new_astro=img.thumbnail((300,300)) 
img.save('small.jpg')