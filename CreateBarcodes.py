"""Create barcodes"""


import sys, os
from PIL import Image
import barcode
from barcode.writer import ImageWriter
from StringIO import StringIO

wordList = ['helicopter', 'puppy', 'doggy', 'elephant', 'mouse', 'moose', 'bird']

wordList += ["alligator","ant","bear","bee","bird","camel","cat","cheetah","chicken","chimpanzee","cow","crocodile","deer","dog","dolphin","duck","eagle","elephant","fish","fly","fox","frog","giraffe","goat","goldfish","hamster","hippopotamus","horse","kangaroo","kitten","lion","lobster","monkey","octopus","owl","panda","pig","puppy","rabbit","rat","scorpion","seal","shark","sheep","snail","snake","spider","squirrel","tiger","turtle","wolf","zebra"]

wordList +=
for word in wordList:
    EAN = barcode.get_barcode_class('code39')
    ean = EAN(word, writer=ImageWriter())
    ean.code = word.upper()
    fullname = ean.save(os.path.join('barcodes', '%s_barcode' %word))

#
# ean = EAN(u'5901234123457')
#
# >>> EAN
# <class 'barcode.ean.EuropeanArticleNumber13'>
# >>> ean = EAN(u'5901234123457')
# >>> ean
# <barcode.ean.EuropeanArticleNumber13 object at 0x00BE98F0>
# >>> fullname = ean.save('ean13_barcode')
# >>> fullname
# u'ean13_barcode.svg'
# # Example with PNG
# >>> from barcode.writer import ImageWriter
# >>> ean = EAN(u'5901234123457', writer=ImageWriter())
# >>> fullname = ean.save('ean13_barcode')
# u'ean13_barcode.png'
# # New in v0.4.2
# >>> from StringIO import StringIO
# >>> fp = StringIO()
# >>> ean.write(fp)
# # or
# >>> f = open('/my/new/file', 'wb')
# >>> ean.write(f) # PIL (ImageWriter) produces RAW format here
# # New in v0.5.0
# >>> from barcode import generate
# >>> name = generate('EAN13', u'5901234123457', output='barcode_svg')
# >>> name
# u'barcode_svg.svg'
# # with file like object
# >>> fp = StringIO()
# >>> generate('EAN13', u'5901234123457', writer=ImageWriter(), output=fp)
# >>>
#


image_filename_list = [os.path.join('barcodes', '%s_barcode.png' %word) for word in wordList]
images = map(Image.open, image_filename_list)
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

image_size_x = 2300
image_size_y = int(np.round(image_size_x * 11.5 /8))
new_im = Image.new('RGB', (image_size_x, image_size_y), color= 'white')


image_index = 0
y_offset = 0
x_gap = 25
y_gap = 10
for i in xrange(20):
    x_offset = 0
    for j in xrange(10):

        if (x_offset +x_gap + images[image_index].size[1]-1) > image_size_x:
            break
        new_im.paste(images[image_index], (x_offset, y_offset))
        x_offset += images[image_index].size[0] + x_gap
        image_index+=1
        if image_index == len(images):
            break
    if image_index == len(images):
        break

    y_offset += max_height + y_gap

new_im.save('test.png')