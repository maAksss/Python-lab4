import sys

def _check_ver():
    if sys.version_info >= (3, 13):
        print("="*60)
        print("УВАГА: Виявлено версію Python 3.13 або вище!")
        print("Бібліотека googletrans НЕ СУМІСНА з цією версією (відсутній модуль cgi).")
        print("="*60)

_check_ver()

try:
    from googletrans import Translator, LANGUAGES
    translator = Translator()
except ImportError:
    translator = None
    LANGUAGES = {}

def TransLate(text: str, scr: str, dest: str) -> str:
    if not translator:
        return "Помилка модуля 2: бібліотека не завантажена через несумісність версій."
    try:
        res = translator.translate(text, src=scr, dest=dest)
        return res.text
    except Exception as e:
        return f"Помилка модуля 2: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    if not translator:
        return "Помилка модуля 2: бібліотека не завантажена через несумісність версій."
    try:
        det = translator.detect(text)
        if set == "lang":
            return det.lang
        elif set == "confidence":
            return str(det.confidence)
        else:
            return f"Language: {det.lang}, Confidence: {det.confidence}"
    except Exception as e:
        return f"Помилка модуля 2: {str(e)}"

def CodeLang(lang: str) -> str:
    if not LANGUAGES:
        return "Помилка модуля 2: словник мов недоступний."
    try:
        lang = lang.lower()
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
        return "Помилка: мову не знайдено"
    except Exception as e:
        return f"Помилка модуля 2: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    if not LANGUAGES:
        return "Помилка модуля 2: словник мов недоступний."
    try:
        header = f"{'N':<4} {'Language':<20} {'ISO-639':<10}"
        if text:
            header += f" {'Translation':<30}"
        
        output_lines = [header, "-" * len(header)]
        
        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            line = f"{i:<4} {name.capitalize():<20} {code:<10}"
            if text:
                tr_text = TransLate(text, "auto", code)
                line += f" {tr_text:<30}"
            output_lines.append(line)
        
        final_output = "\n".join(output_lines)

        if out == "screen":
            print(final_output)
        elif out == "file":
            with open("lang_list_mod2.txt", "w", encoding="utf-8") as f:
                f.write(final_output)
        
        return "Ok"
    except Exception as e:
        return f"Помилка модуля 2: {str(e)}"