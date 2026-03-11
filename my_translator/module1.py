from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        res = translator.translate(text, src=scr, dest=dest)
        return res.text
    except Exception as e:
        return f"Помилка: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        det = translator.detect(text)
        if set == "lang":
            return det.lang
        elif set == "confidence":
            return str(det.confidence)
        elif set == "all":
            return f"Language: {det.lang}, Confidence: {det.confidence}"
        return "Помилка: невірний параметр set"
    except Exception as e:
        return f"Помилка: {str(e)}"

def CodeLang(lang: str) -> str:
    try:
        lang = lang.lower()
        # 'en' -> 'english'
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        
        # 'english' -> 'en'
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
        
        return "Помилка: мову або код не знайдено"
    except Exception as e:
        return f"Помилка: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        # Заголовки таблиці
        # f-рядок з вирівнюванням: :< за лівим краєм, число - ширина стовбця
        header = f"{'N':<4} {'Language':<20} {'ISO-639':<10}"
        if text:
            header += f" {'Text translation':<30}"
        
        output_lines = [header, "-" * len(header)]
        
        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            line = f"{i:<4} {name.capitalize():<20} {code:<10}"
            if text:
                translation = TransLate(text, "auto", code)
                line += f" {translation:<30}"
            output_lines.append(line)
        
        result_text = "\n".join(output_lines)

        if out == "screen":
            print(result_text)
        elif out == "file":
            with open("lang_list.txt", "w", encoding="utf-8") as f:
                f.write(result_text)
        else:
            return "Помилка: невірний параметр out"
            
        return "Ok"
    except Exception as e:
        return f"Помилка: {str(e)}"