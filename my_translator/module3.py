from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

# Отримуємо словник мов з deep_translator
# Формат: {'afrikaans': 'af', 'albanian': 'sq', ...}
translator_instance = GoogleTranslator()
SUPPORTED_LANGS = translator_instance.get_supported_languages(as_dict=True)

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        # deep_translator очікує 'auto' або код мови
        translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Помилка модуля 3: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        if set == "lang":
            return detect(text)
        elif set == "confidence":
            res = detect_langs(text)[0]
            return str(res.prob)
        else:
            res = detect_langs(text)[0]
            return f"Language: {res.lang}, Confidence: {res.prob}"
    except Exception as e:
        return f"Помилка модуля 3: {str(e)}"

def CodeLang(lang: str) -> str:
    try:
        lang = lang.lower()
        if lang in SUPPORTED_LANGS.values():
            for name, code in SUPPORTED_LANGS.items():
                if code == lang:
                    return name
        
        if lang in SUPPORTED_LANGS:
            return SUPPORTED_LANGS[lang]
            
        return "Помилка: мову або код не знайдено"
    except Exception as e:
        return f"Помилка модуля 3: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        header = f"{'N':<4} {'Language':<20} {'ISO-639':<10}"
        if text:
            header += f" {'Translation':<30}"
        
        output_lines = [header, "-" * len(header)]
        
        for i, (name, code) in enumerate(SUPPORTED_LANGS.items(), 1):
            line = f"{i:<4} {name.capitalize():<20} {code:<10}"
            if text:
                tr_text = TransLate(text, "auto", code)
                line += f" {tr_text:<30}"
            output_lines.append(line)
        
        final_output = "\n".join(output_lines)

        if out == "screen":
            print(final_output)
        elif out == "file":
            with open("lang_list_mod3.txt", "w", encoding="utf-8") as f:
                f.write(final_output)
        
        return "Ok"
    except Exception as e:
        return f"Помилка модуля 3: {str(e)}"