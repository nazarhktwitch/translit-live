from pynput import keyboard
import pyperclip

# Таблица для транслитерации
translit_table = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
    'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
    'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
}

# Функция для транслитерации текста
def transliterate(text):
    return ''.join(translit_table.get(char, char) for char in text)

# Буфер для хранения набранного текста
input_buffer = []

def on_press(key):
    try:
        # Если клавиша - символ, добавляем в буфер
        if hasattr(key, 'char') and key.char:
            input_buffer.append(key.char)
        elif key == keyboard.Key.space:
            input_buffer.append(' ')
        elif key == keyboard.Key.ctrl_r:
            # При нажатии Enter выполняем транслитерацию
            original_text = ''.join(input_buffer)
            transliterated_text = transliterate(original_text)
            print(f"Original: {original_text}")
            print(f"Transliterated: {transliterated_text}")
            # Копируем результат в буфер обмена
            pyperclip.copy(transliterated_text)
            input_buffer.clear()
        elif key == keyboard.Key.backspace and input_buffer:
            input_buffer.pop()  # Удаляем последний символ
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Выход из программы при нажатии Esc
    if key == keyboard.Key.esc:
        return False

# Запуск слушателя клавиатуры
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Listening for keyboard input... Press ESC to quit.")
    listener.join()
