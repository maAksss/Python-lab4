import asyncio
from my_translator import module1

async def main():
    # Тест перекладу
    res = await module1.TransLate("Привіт світ", "uk", "en")
    print(f"Переклад: {res}")
    
    # Тест детекції
    det = await module1.LangDetect("Hello world", "all")
    print(f"Детекція: {det}")
    
    # Тест списку 
    print("Генерація списку мов...")
    await module1.LanguageList("screen", "Hi")

if __name__ == "__main__":
    asyncio.run(main())