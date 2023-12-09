from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import  Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='\hp\Downloads', title='Select an Image:')
##print(filename)

def add_watermark(image, wm_text):
    #Create the image object
    opened_image = Image.open(image)

    #Get image size
    image_width, image_height = opened_image.size

    #Draw the image
    draw = ImageDraw.Draw(opened_image)

    #Specify a font size
    font_size = int(image_width / 10)

    #font type
    font = ImageFont.truetype('arial.ttf', font_size)

    #coordinates for where you want the image
    x, y = int(image_width/2), int(image_height/2)

     #add the watermark
    draw.text((x,y), wm_text, font=font, fill='#EEE', stroke_width=5, stroke_fill='#222', anchor='ms')

    #show the new image
    opened_image.show()

add_watermark(filename, 'mywesite.com')

