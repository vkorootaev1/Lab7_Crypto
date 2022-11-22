from PIL import Image


# Функция перевода строки в двоичный формат
def str2bin(text: str, encoding='ascii') -> str:
    return ''.join(
        bin(c)[2:].rjust(8, '0') for c in text.encode(encoding)
    )


# Функция дополнения пустыми символами
def append_null(text):
    if len(text) % 3 != 0:
        for q in range(0, 3 - len(text) % 3):
            text += '\0'
    return text


# Алгоритм скрытия данных в изображении
def encode(img, text):
    img.show('Начальное изображение')
    print(f'Текст, который хотим скрыть в изображении:\n {text}')
    text = append_null(text)
    text_bin = str2bin(text)
    print(f'Бинарное представление текста на основе таблицы ASCII:\n {text_bin}')
    pixel = list(img.getdata())
    start = 0
    temp = start

    for i in range(0, len(text_bin), 3):

        red = pixel[temp][0]
        green = pixel[temp][1]
        blue = pixel[temp][2]

        if (text_bin[i] == '0' and red % 2 != 0) or (text_bin[i] == '1' and red % 2 == 0):
            if red == 0:
                red = 1
            else:
                red = pixel[temp][0] - 1

        if (text_bin[i + 1] == '0' and green % 2 != 0) or (text_bin[i + 1] == '1' and green % 2 == 0):
            if green == 0:
                green = 1
            else:
                green = pixel[temp][1] - 1

        if (text_bin[i + 2] == '0' and blue % 2 != 0) or (text_bin[i + 2] == '1' and blue % 2 == 0):
            if blue == 0:
                blue = 1
            else:
                blue = pixel[temp][2] - 1

        pixel[temp] = (red, green, blue)
        temp += 1

    end = temp

    OUTPUT_IMAGE_SIZE = (img.size[0], img.size[1])
    new_img = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    new_img.putdata(pixel)
    new_img.save("C:/Users/johnk/Downloads/new_sample_1280×853.bmp")
    new_img.show(title='Измененное изображение')
    return start, end, new_img


# Алгоритм раскрытия данных из изображения
def decode(start, end, img):
    text_bin = ''
    text_out = ''
    pixel = list(img.getdata())

    for i in range(start, end):
        text_bin += str(pixel[i][0] & 1) + str(pixel[i][1] & 1) + str(pixel[i][2] & 1)

    for j in range(0, len(text_bin), 8):
        text_out += chr(int(text_bin[j:j + 8], 2))

    print(f'Бинарное представление скрытого текста: \n {text_bin}')
    print(f"Скрытый в изображении текст: \n {text_out.replace(chr(0), '')}")

