from functions import load_tasks

tasks = {
    '1. Kontrola validního emailu': {
        'instructions': """
    Vytvořte program, který zkontroluje, zda uživatelem zadaný email je validní nebo ne.
    """,
        'hint': """
    Použijte modul `re` a regulární výraz pro kontrolu emailů:
    `r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'`.
    """,
        'code': """
    import re

    email = input("Zadejte email: ")

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(pattern, email):
        print(f"Email '{email}' je validní.")
    else:
        print(f"Email '{email}' je neplatný.")
    """,
        'demonstration': """
import re

email = st.text_input('Zadejte email:')
if email:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        st.write(f"Email '{email}' je validní.")
    else:
        st.write(f"Email '{email}' je neplatný.")
    """
    },

    '2. Hledání čísel v textu': {
        'instructions': """
        Vytvořte program, který vyhledá v textu všechna čísla pomocí regulárního výrazu.
        """,
        'hint': """
        Použijte modul `re` a regulární výraz `r'\\d+'` pro vyhledání všech čísel v textu. Pro výpis výsledného textu můžete využít metodu `.join()`.
        """,
        'code': """
        import re

        text = input("Zadejte text: ")

        pattern = r'\\d+'
        numbers = re.findall(pattern, text)

        if numbers:
            print(f"Nalezená čísla: {', '.join(numbers)}")
        else:
            print("V textu nebyla nalezena žádná čísla.")
        """,
        'demonstration': """
import re

text = st.text_input('Zadejte text:')
if text:
    pattern = r'\\d+'
    numbers = re.findall(pattern, text)
    if numbers:
        st.write(f"Nalezená čísla: {', '.join(numbers)}")
    else:
        st.write("V textu nebyla nalezena žádná čísla.")
        """
    },

    '3. Ošetření výjimky při indexování seznamu': {
        'instructions': """
    Vytvořte program, který v seznamu čísel `[1, 10, 100, 1000, 10000, 100000, 1000000]` bude hledat číslo podle indexu zadaného uživatelem.
    Pokud index neexistuje, ošetřete výjimku a vypište chybovou zprávu. Stejně tak ošetřete situaci, kdy uživatel nezadá platné číslo.
    Uživatele informujte, z jakého seznamu vybírá a vypište mu rozsah od-do indexu, ze kterých může vybírat (zvolte obecné řešení, kdyby se seznam čísel měnil).
    Pokud bude index platný, vypište uživateli informaci, že na indexu, který zadal, se nachází příslušná hodnota.
    """,
        'hint': """
    Použijte blok `try-except` a zachyťte výjimku typu `IndexError`, která se vyvolá při přístupu k neexistujícímu indexu.
    Pro zachycení hodnoty, která nebude číslo, použijte výjimku typu `ValueError`. Indexy bude přístupný od 0 do `len(seznam_cisel) - 1`.
    
    """,
        'code': """
    try:
        items = [1, 10, 100, 1000, 10000, 100000, 1000000]
        index = int(input(f"Zadejte index prvku (0-{len(items) - 1}): "))

        print(f"Hodnota na indexu {index}: {items[index]}")
    except IndexError:
        print("Chyba: Zadaný index není v seznamu.")
    except ValueError:
        print("Chyba: Prosím, zadejte platné celé číslo.")
    """,
        'demonstration': """
items = [1, 10, 100, 1000, 10000, 100000, 1000000]
index = st.text_input(f"Zadejte index prvku (0-{len(items) - 1}): ")

if index:
    try:
        index = int(index)
        result = f"Hodnota na indexu {index}: {items[index]}\\n"
        st.code(result)
    except IndexError:
        st.write("Chyba: Zadaný index není v seznamu.")
    except ValueError:
        st.write("Chyba: Prosím, zadejte platné číslo.")
    """
    },

    '4. Kontrola platného hesla': {
        'instructions': """
    Napište program, který zkontroluje, zda zadané heslo splňuje pravidla:
    - Má alespoň 8 znaků.
    - Obsahuje alespoň jedno číslo.
    - Obsahuje alespoň jedno velké a malé písmeno.
    """,
        'hint': """
    Použijte regulární výrazy jako `r'.{8,}'`, `r'[A-Z]'`, `r'[a-z]'` a `r'\\d'` a ověřte je všechny na zadané heslo.
    """,
        'code': """
    import re

    password = input("Zadejte heslo: ")
    
    is_length_ok = len(password) >= 8
    is_digit_ok = re.search(r'\\d', password)
    is_alpha_ok = re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)

    if all((is_length_ok, is_digit_ok, is_alpha_ok)):
        print("Heslo je platné.")
    else:
        print("Heslo není platné.")
    """,
        'demonstration': """
import re

password = st.text_input('Zadejte heslo:')
if password:
    is_length_ok = len(password) >= 8
    is_digit_ok = re.search(r'\\d', password)
    is_alpha_ok = re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)

    if all((is_length_ok, is_digit_ok, is_alpha_ok)):
        st.write("Heslo je platné.")
    else:
        st.write("Heslo není platné.")
    """
    },

    '5. Sčítání četností výskytů písmen ve větě': {
        'instructions': """
        Napište program, který zadanou větu analyzuje na četnost každého písmene (pouze písmen latinské abecedy).
        Písmena se nemají rozlišovat podle velikosti, tj. 'A' a 'a' jsou chápána jako totéž.
        Výsledek uložte do slovníku (klíčem je písmeno, hodnotou je počet jeho výskytů).
        Seřaďte výsledný slovník vzestupně podle abecedy a vypište ho.
        """,
        'hint': """
        Použijte `dict` pro uložení četností. Pro normalizaci velikosti písmen použijte metodu `.lower()` 
        a otestujte, zda je znak písmeno pomocí metody `isalpha()`.
        Chcete-li slovník seřadit podle klíče, využijte `sorted()` s metodou `.items()`.
        """,
        'code': """
        # Funkce pro výpočet četností písmen
        def calculate_frequencies(sentence):
            frequency = {}
            for char in sentence.lower():  # Ignorujeme velikosti písmen
                if char.isalpha():  # Zajímáme se pouze o písmena
                    if char in frequency:
                        frequency[char] += 1
                    else:
                        frequency[char] = 1
            return frequency

        # Vstup a výpočet
        sentence = input("Zadejte větu: ")
        frequencies = calculate_frequencies(sentence)

        # Seřazení a výpis výsledků
        sorted_frequencies = dict(sorted(frequencies.items()))
        print("Počet výskytů písmen ve větě:")
        for letter, count in sorted_frequencies.items():
            print(f"{letter}: {count}")
        """,
        'demonstration': """
# Funkce pro výpočet četností písmen
def calculate_frequencies(sentence):
    frequency = {}
    for char in sentence.lower():  # Ignorujeme velikosti písmen
        if char.isalpha():  # Zajímáme se pouze o písmena
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

sentence = st.text_input("Zadejte větu:")

if sentence:
    frequencies = calculate_frequencies(sentence)
    sorted_frequencies = dict(sorted(frequencies.items()))

    st.write("Počet výskytů písmen ve větě:")
    for letter, count in sorted_frequencies.items():
        st.write(f"{letter}: {count}")
        """
    }

}

load_tasks("Složitější úlohy", tasks)
