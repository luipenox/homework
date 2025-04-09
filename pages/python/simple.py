import streamlit as st
from functions import load_tasks

tasks = {
    '1. Uživatelský vstup a jednoduchý výstup': {
        'instructions': """
            Získejte od uživatele jeho jméno, které uložíte do proměnné a následně vypíšete pozdrav.
            Formát pozdravu je `Ahoj, --jméno--!`, kde `--jméno--` nahradíte zadaným jménem.
        """,
        'hint': """
            Pro získání uživatelského vstupu použijte funkci `input()`, která jako argument přijímá textovou zprávu, kterou vypíše uživateli.
            Pro výpis použijte funkci `print()`. Pro správný formát pozdravu můžete použít f-string, do kterého uvedete zprávu spolu s proměnnou ve složených závorkách.
        """,
        'code': """
            name = input("Zadejte své jméno: ")
            print(f"Ahoj, {name}!")
        """,
        'demonstration': """
text = st.text_input("Zadejte své jméno:")
if text:
    st.write(f"Ahoj, {text}!")
            """

    },

    '2. Uživatelský vstup a výpis hvězdiček': {
        'instructions': """
            Získejte od uživatele číslo a vypište tolikkrát písmeno (`X`), kolik určil.
            Výstup by měl být na jednom řádku bez dalších znaků. Ošetření chyby při převodu čísla nemusíte ošetřovat.
        """,
        'hint': """
            Pro získání uživatelského vstupu použijte funkci `input()` a převeďte jej na celé číslo pomocí `int()`.
            Hvězdičky můžete vypisovat buď pomocí řetězcové násobení (`'*' * číslo`), nebo cyklem.
            Pro výstup použijte funkci `print()`.
        """,
        'code': """
            number = int(input("Zadejte číslo: "))
            print('*' * number)
        """,
        'demonstration': """
number = st.text_input("Zadejte číslo:")
if number:
    try:
        number = int(number)
        st.write('X' * number)
    except ValueError:
        st.write('ValueError')
            """
    },

    '3. Výpis obvodového čtverce z písmen X': {
        'instructions': """
        Na základě uživatelského vstupu v podobě čísla vytvořte textový čtverec z písmen `X`. 
        Čtverec bude mít zadanou délku strany, přičemž jeho obvod bude tvořen pouze písmeny `X`. 
        Vnitřek čtverce zůstane prázdný (vyplněný mezerami). Velikost strany čtverce musí být od 3 do 20.
        V opačném případě uživatele upozorněte, že zadal neplatný rozsah a program ukončete.
    """,
        'hint': """
        Pro získání délky strany použijte funkci `input()` a převod na celé číslo pomocí `int()`.
        Čtverec vytvořte pomocí cyklu `for`, kde na prvním a posledním řádku vypíšete pouze `X` podle délky strany.
        Na středních řádcích vypište `X` na začátek a konec řádku, zbytek vyplňte mezerami.
        Použijte funkci `print()` pro výpis každého řádku čtverce zvlášť. Testování rozsahu můžeme provést pomocí `if`, operátoru porovnání a logického `and`.
        Případně můžete použít porovnání z obou stran (`3 <= strana <= 20`).
    """,
        'code': """
        size = int(input("Zadejte délku strany čtverce: "))
        if 3 <= size <= 20:
            for i in range(size):
                if i == 0 or i == size - 1:  # První a poslední řádek
                    print('X' * size)
                else:  # Střední řádky s mezerami uprostřed
                    print('X' + ' ' * (size - 2) + 'X')
    """,
        'demonstration': """
output = ''
size = st.text_input("Zadejte délku strany čtverce:")
if size:
    try:
        size = int(size)
        if size < 3 or size > 20:
            st.write("Zadal jsi neplatný rozsah.")
        else:
            for i in range(size):
                if i == 0 or i == size - 1:  # První a poslední řádek
                    output += ('X' * size + '\\n')
                else:  # Střední řádky s mezerami uprostřed
                    output += ('X' + ' ' * (size - 2) + 'X' + '\\n')
        
            st.code(output)
    except ValueError:
        st.write('ValueError')
                    """
    },

    '4. Výpočet obsahu kruhu': {
        'instructions': """
            Na základě uživatelského vstupu vypočítejte obsah kruhu. 
            Program si vyžádá poloměr kruhu, přičemž tento poloměr musí být kladné číslo. 
            Obsah vypočítejte na základě vzorce `S = π * r^2`, kde `r` je poloměr kruhu. 
            Pokud uživatel zadá záporné číslo nebo nepodporovaný vstup, program ho upozorní a ukončí.
            Pro výpočet hodnoty π použijte modul `math`.
            """,
        'hint': """
            Pro získání poloměru použijte funkci `input()` a převod na desetinné číslo pomocí `float()`.
            Pro kontrolu kladného vstupu použijte podmínku `if` a porovnání, zda zadaný poloměr není záporný.
            Pro výpočet obsahu kruhu použijte modul `math` a jeho konstantu `math.pi`.
            Při chybě převodu na desetinné číslo použijte blok `try...except`, kde zachytíte `ValueError`.
            Výsledek zaokrouhlete pomocí metody `round()` na dvě desetinná místa.
            """,
        'code': """
            import math

            try:
                # Zadejte poloměr kruhu
                polomer = float(input("Zadejte kladný poloměr kruhu: "))

                # Kontrola, zda je poloměr kladný
                if polomer > 0:
                    # Výpočet obsahu kruhu
                    obsah = math.pi * polomer ** 2
                    print(f"Obsah kruhu o poloměru {polomer} je přibližně {round(obsah, 2)}.")
                else:
                    print("Poloměr musí být kladné číslo.")
            except ValueError:
                print("Neplatný vstup. Zadejte číselnou hodnotu.")
            """,
        'demonstration': """
output = ''
radius = st.text_input("Zadejte poloměr kruhu:")
if radius:
    try:
        radius = float(radius)
        if radius <= 0:
            st.write("Poloměr musí být kladné číslo.")
        else:
            import math
            area = math.pi * radius ** 2
            output = f"Obsah kruhu o poloměru {radius} je přibližně {round(area, 2)}."
            st.write(output)
    except ValueError:
        st.write("Neplatný vstup. Zadejte číselnou hodnotu.")
            """
    },

    '5. Výpočet mocnin zadaného čísla': {
        'instructions': """
        Vytvořte program, který si od uživatele vyžádá jedno číslo. Z tohoto čísla vypočítejte jeho druhou, třetí, čtvrtou a pátou mocninu. 
        Tyto hodnoty uložte do seznamu. Pomocí cyklu `for` projděte všechny hodnoty v seznamu a po řádcích je vypište. 
        Každý řádek by měl obsahovat informaci o tom, jaká mocnina byla počítána (např.: "Číslo 3 na 2. mocninu je 9.").
        Ověřte, že uživatel zadal číselný vstup a ošetřete případné chyby při převodu vstupu.
        """,
        'hint': """
        Pro získání vstupního čísla použijte funkci `input()`. Převod na typ čísla proveďte pomocí `float()` (pokud chcete podporovat desetinná čísla) 
        nebo `int()`. Pro vypočítání mocnin použijte operátor `**` a výsledky ukládejte do seznamu. 
        Seznam můžete procházet pomocí cyklu `for` spolu s funkcí `enumerate()`, která vám umožní jednoduše získat index (pro určení mocniny) a hodnotu. 
        Ověřte také, že uživatel zadal platný číselný vstup. Pokud vstup není číslo, zachyťte chybu `ValueError` a vypište uživateli upozornění.
        """,
        'code': """
        try:
            # Získání čísla od uživatele
            cislo = float(input("Zadejte číslo: "))

            # Vytvoření seznamu s mocninami
            mocniny = [cislo ** i for i in range(2, 6)]

            # Výpis výsledků po řádcích
            for i, hodnota in enumerate(mocniny, start=2):
                print(f"Číslo {cislo} na {i}. mocninu je {hodnota}.")
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """,
        'demonstration': """
output = ''
number = st.text_input("Zadejte číslo:")
if number:
    try:
        number = float(number)

        # Výpočet mocnin a jejich uložení do seznamu
        powers = [number ** i for i in range(2, 6)]

        # Iterace přes seznam a formátovaný výpis
        for i, value in enumerate(powers, start=2):
            output += f"Číslo {number} na {i}. mocninu je {value}\\n"

        st.code(output)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """
    }

}





load_tasks("Jednoduché úlohy", tasks)
