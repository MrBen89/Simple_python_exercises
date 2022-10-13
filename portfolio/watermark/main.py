
import PIL.Image

def add_mark():
    im = PIL.Image.open("background.png")
    watermark = PIL.Image.open("watermark.png")
    merge(im, watermark)



def merge(im1, im2):
    w = im1.size[0]
    h = max(im1.size[1], im2.size[1])
    im = PIL.Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2)

    im.save("cat.png")




add_mark()
