import os
import json
import re
import importlib

def get_file_info(file_path):
    if not os.path.exists(file_path):
        return None
    
    size = os.path.getsize(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chars = len(content)
    
    sentences = re.split(r'(?<=[.!?])\s+', content.strip())
    
    return {
        "size": size,
        "chars": chars,
        "sentences": sentences,
        "full_content": content
    }

def main():
    # I. Зчитування конфігурації
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print("Помилка: Конфігураційний файл не знайдено.")
        return

    # II. Отримання інформації про файл
    info = get_file_info(cfg['file_name'])
    if not info:
        print(f"Помилка: Файл {cfg['file_name']} відсутній.")
        return

    # Динамічно імпортуємо обраний модуль
    try:
        translator_mod = importlib.import_module(f"my_translator.{cfg['module_name']}")
    except ImportError:
        print(f"Помилка: Модуль {cfg['module_name']} не знайдено.")
        return

    # Визначаємо мову оригіналу (перше речення)
    lang_orig = translator_mod.LangDetect(info['sentences'][0], set="lang")

    print(f"Назва файлу: {cfg['file_name']}")
    print(f"Розмір файлу: {info['size']} байт")
    print(f"Кількість символів: {info['chars']}")
    print(f"Кількість речень: {len(info['sentences'])}")
    print(f"Мова тексту: {lang_orig}")
    print("-" * 30)

    # III. Відбір речень для перекладу
    count_to_translate = min(len(info['sentences']), cfg['max_sentences'])
    text_to_translate = " ".join(info['sentences'][:count_to_translate])

    # IV. Виконання перекладу
    try:
        translated = translator_mod.TransLate(text_to_translate, "auto", cfg['target_lang'])
        
        # V. Вивід результату 
        if cfg['output'] == "screen":
            print(f"Мова перекладу: {cfg['target_lang']}")
            print(f"Використаний модуль: {cfg['module_name']}")
            print(f"Результат:\n{translated}")
        
        elif cfg['output'] == "file":
            # ім'я файлу: B-12_ja.txt
            base_name = os.path.splitext(cfg['file_name'])[0]
            out_file_name = f"{base_name}_{cfg['target_lang']}.txt"
            
            with open(out_file_name, 'w', encoding='utf-8') as f:
                f.write(translated)
            print("Ok")
            
    except Exception as e:
        print(f"Виникла помилка при перекладі: {e}")

if __name__ == "__main__":
    main()