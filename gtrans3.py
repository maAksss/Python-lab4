from my_translator import module2

def demo():
    print("--- Демонстрація роботи Module 2 (googletrans 3.1.0a0) ---")
    
    text = "Джобс є найвищим зразком винахідливості."
    
    # 1. Переклад на англійську
    translated = module2.TransLate(text, "uk", "en")
    print(f"Оригінал: {text}")
    print(f"Переклад (EN): {translated}")
    
    # 2. Визначення мови
    detect = module2.LangDetect(text, "all")
    print(f"Детекція: {detect}")
    
    # 3. Код мови
    print(f"Код мови 'japanese': {module2.CodeLang('japanese')}")
    
    # 4. Вивід таблиці
    print("\nГенерація таблиці мов...")
    module2.LanguageList("screen", "Світ")

if __name__ == "__main__":
    demo()