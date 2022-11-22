from PIL import Image


# Функция перевода строки в двоичный формат
def str2bin(text: str, encoding='ascii') -> str:
    return ''.join(
        bin(c)[2:].rjust(8, '0') for c in text.encode(encoding)
    )


# Алгоритм скрытия данных в изображении
def encode(img, text):

    img.show('Начальное изображение')
    print(f'Текст, который хотим скрыть в изображении:\n {text}')
    text_bin = str2bin(text)
    print(f'Бинарное представление текста на основе таблицы ASCII:\n {text_bin}')
    pixel = list(img.getdata())
    start = 10000
    end = start
    for i in text:

        symbol_bin = str2bin(i)
        bit_symbol = 0

        for j in range(0, 3):

            red = pixel[end][0]
            green = pixel[end][1]
            blue = pixel[end][2]

            if (symbol_bin[bit_symbol] == '0' and red % 2 != 0) or (symbol_bin[bit_symbol] == '1' and red % 2 == 0):
                if red == 0:
                    red = 1
                else:
                    red -= 1

            if (symbol_bin[bit_symbol + 1] == '0' and green % 2 != 0) or (symbol_bin[bit_symbol + 1] == '1' and green % 2 == 0):
                if green == 0:
                    green = 1
                else:
                    green -= 1

            if j != 2:
                if (symbol_bin[bit_symbol + 2] == '0' and blue % 2 != 0) or (symbol_bin[bit_symbol + 2] == '1' and blue % 2 == 0):
                    if blue == 0:
                        blue = 1
                    else:
                        blue -= 1

            pixel[end] = (red, green, blue)
            bit_symbol += 3
            end += 1

    OUTPUT_IMAGE_SIZE = (img.size[0], img.size[1])
    new_img = Image.new('RGB', OUTPUT_IMAGE_SIZE)
    new_img.putdata(pixel)
    new_img.save("C:/Users/johnk/Downloads/new_sample_1280×853.bmp")
    new_img.show(title='Измененное изображение')
    key = (start, end)
    print(f"Начальный пиксель, содержащий информацию: {start} \nКонечный пиксель, содержащий информацию: {end}")
    print(f"Количество пикселей, содержащих информацию: {end-start}")
    return key, new_img


# Алгоритм раскрытия данных из изображения
def decode(key, img):

    start = key[0]
    end = key[1]
    text_bin = ''
    text_out = ''
    pixel = list(img.getdata())

    for i in range(start, end):
        text_bin += str(pixel[i][0] & 1) + str(pixel[i][1] & 1)
        if (i-start) % 3 != 2:
            text_bin += str(pixel[i][2] & 1)

    for j in range(0, len(text_bin), 8):
        text_out += chr(int(text_bin[j:j + 8], 2))

    print(f'Бинарное представление скрытого текста: \n {text_bin}')
    print(f"Скрытый в изображении текст: \n {text_out}")

