from PIL import Image
from steganography_picture import encode, decode

# Открытие изображения в формате bmp
img = Image.open("C:/Users/johnk/Downloads/sample_1280×853.bmp")

# Текст, который хотим скрыть в изображении
text = "Latest Cryptography Lab!!!"

# Сокрытие текста в изображении
start_position, end_position, new_img = encode(img, text)

# Поиск текста, скрытого в изображении
decode(start_position, end_position, new_img)
