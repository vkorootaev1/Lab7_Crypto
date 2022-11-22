from PIL import Image
from steganography_picture import encode, decode

# Открытие изображения в формате bmp
img = Image.open("C:/Users/johnk/Downloads/sample_1280×853.bmp")

# Текст, который хотим скрыть в изображении
text = "Latest cryptography lab!"

# Сокрытие текста в изображении
key, new_img = encode(img, text)

# Поиск информации, скрытой в изображении
decode(key, new_img)
