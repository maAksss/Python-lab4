from my_translator import module3

def demo_deep_translator():
    print("="*60)
    print(f"{'ДЕМОНСТРАЦІЯ МОДУЛЯ 3 (deep_translator + langdetect)':^60}")
    print("="*60)

    # 1. Тест перекладу 
    original_text = "Джобс є найвищим зразком винахідливості."
    target_lang = "ja"
    
    print(f"\n[1] Тест TransLate:")
    translated = module3.TransLate(original_text, "auto", target_lang)
    print(f"Оригінал: {original_text}")
    print(f"Переклад ({target_lang}): {translated}")

    # 2. Тест визначення мови 
    print(f"\n[2] Тест LangDetect:")
    print(f"Повна інформація: {module3.LangDetect(original_text, set='all')}")

    # 3. Тест кодів мов (Пункт 4: CodeLang)
    print(f"\n[3] Тест CodeLang:")
    print(f"Код для 'japanese'  -> {module3.CodeLang('japanese')}")
    print(f"Назва для 'uk'      -> {module3.CodeLang('uk')}")

    # 4. Тест списку мов у ТЕРМІНАЛ
    print(f"\n[4] Тест LanguageList (вивід на екран):")
    # Викликаємо функцію з параметром out="screen"
    # Для демонстрації передаємо текст "Добрий день"
    module3.LanguageList(out="screen", text="Добрий день")

    print("\n" + "="*60)
    print(f"{'Демонстрацію завершено успішно':^60}")
    print("="*60)

if __name__ == "__main__":
    demo_deep_translator()