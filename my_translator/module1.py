import asyncio
from googletrans import Translator, LANGUAGES

translator = Translator()

async def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        # ПРЯМИЙ ВИКЛИК з await, бо метод вже асинхронний
        res = await translator.translate(text, src=scr, dest=dest)
        return res.text
    except Exception as e:
        return f"Помилка [Async]: {str(e)}"

async def LangDetect(text: str, set: str = "all") -> str:
    try:
        # ПРЯМИЙ ВИКЛИК з await
        det = await translator.detect(text)
        if set == "lang":
            return det.lang
        elif set == "confidence":
            return str(det.confidence)
        else:
            return f"Language: {det.lang}, Confidence: {det.confidence}"
    except Exception as e:
        return f"Помилка [Async]: {str(e)}"

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    for code, name in LANGUAGES.items():
        if name == lang:
            return code
    return "Помилка: мову не знайдено"

async def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        header = f"{'N':<4} {'Language':<20} {'ISO-639':<10}"
        if text:
            header += f" {'Translation':<30}"
        
        output_lines = [header, "-" * len(header)]
        
        if text:
            # Створюємо список корутин для паралельного виконання
            tasks = [TransLate(text, "auto", code) for code in LANGUAGES.keys()]
            # Виконуємо всі одночасно
            translations = await asyncio.gather(*tasks)
        
        for i, (code, name) in enumerate(LANGUAGES.items()):
            line = f"{i+1:<4} {name.capitalize():<20} {code:<10}"
            if text:
                line += f" {translations[i]:<30}"
            output_lines.append(line)
        
        final_output = "\n".join(output_lines)

        if out == "screen":
            print(final_output)
        elif out == "file":
            with open("lang_list_async.txt", "w", encoding="utf-8") as f:
                f.write(final_output)
        
        return "Ok"
    except Exception as e:
        return f"Помилка [Async List]: {str(e)}"