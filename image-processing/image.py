# You have to install pip install Pillow

from PIL import Image, ImageFilter
# im = Image.open("./images/kdp.jpg")
# print(im.format, im.size, im.mode)
# print(im.show())

# filteredImg = im.filter(ImageFilter.CONTOUR).rotate(90)
# filteredImg.save('./images/kdp_contour.jpeg', 'jpeg')

# to convert into grey mode
# image = Image.open("./images/kdp2.jpg")
# filteredImg = image.convert('L')
# filteredImg.save('./images/kdp2_grey.png', 'png')

# img = Image.open("./images/kdp.jpg")
# reSize = img.resize((100, 100))
# reSize.save('./images/kdp_resize.jpeg', 'jpeg')

# If we use resize function it will compress the image and width and height ratio will be gone
# So there is one more utility thumbnail we can use but it will work on actual image

img = Image.open('./images/tiger.jpg')
img.thumbnail((200, 200))
img.save('./images/thumbnail.jpeg')
