from PIL import Image
from PIL import ImageFilter

with Image.open('shrek.jfif') as pic_original:
    print('Зображення відкрито: \n Розмір:', pic_original.size)
    print('Формат', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()

    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpeg')
    print('Зображення створено: \n Розмір:', pic_gray.size)
    print('Формат', pic_gray.format)
    print('Тип:', pic_gray.mode)
    pic_gray.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save('pic_up.jpg')
    pic_up.show()