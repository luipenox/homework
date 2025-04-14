import streamlit as st
from functions import load_tasks

tasks = {
    '1. Ahoj světe': {
        'instructions': """
            Vytvořte program, který na obrazovku vypíše text "Ahoj světe!".
            """,
        'hint': """
            Pro výpis textu na obrazovku použijte funkci `print()`.
            """,
        'code': """
            # Výpis textu na obrazovku
            print("Ahoj světe!")
            """,
        'demonstration': """
st.code('Ahoj světe!')
            """
    }
    ,

    '2. Vstup jména': {
        'instructions': """
            Vytvořte program, který se zeptá uživatele na jeho jméno a poté vypíše pozdrav s tímto jménem.
            """,
        'hint': """
            Pro získání jména uživatele použijte funkci `input()`.
            Pro výpis textu na obrazovku použijte funkci `print()`.
            """,
        'code': """
            # Získání jména uživatele
            name = input('Jaké je vaše jméno? ')

            # Výpis pozdravu s jménem
            print('Ahoj,' + name + '!')
            """,
        'demonstration': """
name = st.text_input('Jaké je vaše jméno?')
if name:
    greeting = f'Ahoj {name}!'
    st.code(greeting)
        """
    },

    '3. Součet dvou čísel': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na dvě čísla a poté vypíše jejich součet. Ve výpisu budou zmíněna obě čísla a výsledek.
        """,
        'hint': """
        Pro získání čísel od uživatele použijte funkci `input()`.
        Převedení vstupu na číslo proveďte pomocí funkce `int()`, případně `float()` pro součet desetinných čísel.
        Pro výpis součtu použijte funkci `print()`.
        Pro formátování výstupu použijte f-string, případně metodu `.format()`.
        """,
        'code': """
        # Získání dvou čísel od uživatele
        cislo_1 = float(input('Zadejte první číslo: '))
        cislo_2 = float(input('Zadejte druhé číslo: '))

        soucet = cislo_1 + cislo_2

        # Výpočet a výpis součtu
        print(f'Součet {cislo_1} a {cislo_2} těchto dvou čísel je: {soucet}\\n')
        """,
        'demonstration': """
num1 = st.text_input('Zadejte první číslo:')
num2 = st.text_input('Zadejte druhé číslo:')
if num1 and num2:
    try:
        cislo_1 = float(num1)
        cislo_2 = float(num2)
        
        soucet = cislo_1 + cislo_2

        # Výpočet a výpis součtu
        result = f'Součet {cislo_1} a {cislo_2} těchto dvou čísel je: {soucet}\\n'
        st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """
    },

    '4. Dělení dvou čísel': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na dvě čísla a poté vypíše jejich podíl.
        Nezapomeňte ošetřit situaci, kdy by druhé číslo bylo nula.
        Ve výpisu budou zmíněna obě čísla a výsledek.
        Výsledek zaokrouhlete na dvě desetinná místa.   
        """,
        'hint': """
        Pro získání vstupu od uživatele použijte funkci `input()`.
        Převedení vstupu na číslo proveďte pomocí funkce `float()`.
        Pro výpis podílu použijte funkci `print()`.
        Jestliže druhé číslo (dělitel) je nula, vypíše se upozornění na neplatný vstup.
        Výsledek zaokrouhlete pomocí funkce `round()`.
        Pro formátování výstupu použijte f-string, případně metodu `.format()`.
        """,
        'code': """
        try:
            # Získání dvou čísel od uživatele
            cislo_1 = float(input('Zadejte dělenec: '))
            cislo_2 = float(input('Zadejte dělitel: '))

            if cislo_2 == 0:
                print("Dělení nulou neni možné")
            else:
                # Výpočet a výpis podílu
                podil = round(cislo_1 / cislo_2, 2)
                print(f'Podíl {cislo_1} a {cislo_2} je: {podil}\\n')
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """,
        'demonstration': """
cislo_1 = st.text_input('Zadejte dělenec:')
cislo_2 = st.text_input('Zadejte dělitel:')
if cislo_1 and cislo_2:
    try:
        cislo_1 = float(cislo_1)
        cislo_2 = float(cislo_2)

        if cislo_2 == 0:
            st.write("Dělení nulou není možné.")
        else:
            # Výpočet a výpis podílu
            podil = round(cislo_1 / cislo_2, 2)
            result = f'Podíl {cislo_1} a {cislo_2} je: {podil}\\n'
            st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """
    },

    '5. Převod teploty z Celsius na Fahrenheit': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na teplotu ve stupních Celsia a poté ji převede na stupně Fahrenheita.
        Výsledek zaokrouhlete na dvě desetinná místa.
        """,
        'hint': """
        Pro získání teploty od uživatele použijte funkci `input()`.
        Převedení vstupu na číslo proveďte pomocí funkce `float()`.
        Pro výpis výsledné teploty použijte funkci `print()`.
        Výsledek zaokrouhlete pomocí funkce `round()`.
        Převod teploty proveďte podle vzorce: F = C * 9/5 + 32, kde F je teplota ve stupních Fahrenheita a C je teplota ve stupních Celsia.
        """,
        'code': """
        try:
            # Získání teploty od uživatele
            temp_celsius = float(input('Zadejte teplotu ve stupních Celsia: '))

            # Převod teploty na stupně Fahrenheita
            temp_fahrenheit = round(temp_celsius * 9/5 + 32, 2)

            print(f'Teplota {temp_celsius} stupňů Celsius je {temp_fahrenheit} stupňů Fahrenheit.')
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """,
        'demonstration': """
temp_celsius = st.text_input('Zadejte teplotu ve stupních Celsia:')
if temp_celsius:
    try:
        temp_celsius = float(temp_celsius)

        # Převod teploty na stupně Fahrenheita
        temp_fahrenheit = round(temp_celsius * 9/5 + 32, 2)

        result = f'Teplota {temp_celsius} stupňů Celsius je {temp_fahrenheit} stupňů Fahrenheit.\\n'
        st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """
    },

    '6. Převod teploty z Fahrenheit na Celsius': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na teplotu ve stupních Fahrenheita a poté ji převede na stupně Celsia.
        Výsledek zaokrouhlete na dvě desetinná místa.
        """,
        'hint': """
        Pro získání teploty od uživatele použijte funkci `input()`.
        Převedení vstupu na číslo proveďte pomocí funkce `float()`.
        Pro výpis výsledné teploty použijte funkci `print()`.
        Výsledek zaokrouhlete pomocí funkce `round()`.
        Převod teploty proveďte podle vzorce: C = (F - 32) * 5/9, kde F je teplota ve stupních Fahrenheita a C je teplota ve stupních Celsia.
        """,
        'code': """
        try:
            # Získání teploty od uživatele
            temp_fahrenheit = float(input('Zadejte teplotu ve stupních Fahrenheita: '))

            # Převod teploty na stupně Celsia
            temp_celsius = round((temp_fahrenheit - 32) * 5/9, 2)

            print(f'Teplota {temp_fahrenheit} stupňů Fahrenheit je {temp_celsius} stupňů Celsius.')
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """,
        'demonstration': """
temp_fahrenheit = st.text_input('Zadejte teplotu ve stupních Fahrenheita:')
if temp_fahrenheit:
    try:
        temp_fahrenheit = float(temp_fahrenheit)

        # Převod teploty na stupně Celsia
        temp_celsius = round((temp_fahrenheit - 32) * 5/9, 2)

        result = f'Teplota {temp_fahrenheit} stupňů Fahrenheit je {temp_celsius} stupňů Celsius.\\n'
        st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """
    },

    '7. Obvod obdélníku': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na délku a šířku obdélníku a poté vypočítá a vypíše jeho obvod.
        """,
        'hint': """
        Pro získání délky a šířky obdélníku od uživatele použijte funkci `input()`.
        Převedení vstupu na číslo proveďte pomocí funkce `float()`.
        Pro výpis obvodu obdélníku použijte funkci `print()`.
        Obvod obdélníku vypočtěte podle vzorce: 2 * (délka + šířka).
        """,
        'code': """
        try:
            # Získání délky a šířky obdélníku od uživatele
            length = float(input('Zadejte délku obdélníku: '))
            width = float(input('Zadejte šířku obdélníku: '))

            # Výpočet a výpis obvodu obdélníku
            circumference = 2 * (length + width)

            print(f'Obvod obdélníku o délce {length} a šířce {width} je {circumference}.')
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """,
        'demonstration': """
length = st.text_input('Zadejte délku obdélníku:')
width = st.text_input('Zadejte šířku obdélníku:')
if length and width:
    try:
        length = float(length)
        width = float(width)

        # Výpočet a výpis obvodu obdélníku
        circumference = 2 * (length + width)

        result = f'Obvod obdélníku o délce {length} a šířce {width} je {circumference}.\\n'
        st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """
    },

    '8. Výpočet věku podle roku narození': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na rok narození a poté vypočítá a vypíše jeho aktuální věk. Rozdíl způsobení datem, kdy má uživatel v roce narozeniny, zanedbejte.
        """,
        'hint': """
        Pro získání roku narození od uživatele použijte funkci `input()`.
        Převedení vstupu na číslo proveďte pomocí funkce `int()`.
        Aktuální rok získáte pomocí funkce `datetime.datetime.now().year` z modulu `datetime`.
        Pro výpis věku použijte funkci `print()`.
        """,
        'code': """
        import datetime

        try:
            # Získání roku narození od uživatele
            birth_year = int(input('Zadejte rok Vašeho narození: '))

            # Aktuální rok
            current_year = datetime.datetime.now().year

            # Výpočet a výpis věku
            age = current_year - birth_year

            print(f'Váš věk je {age} let.')
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """,
        'demonstration': """
import datetime

birth_year = st.text_input('Zadejte rok Vašeho narození:')
if birth_year:
    try:
        birth_year = int(birth_year)

        # Aktuální rok
        current_year = datetime.datetime.now().year

        # Výpočet a výpis věku
        age = current_year - birth_year

        result = f'Váš věk je {age} let.\\n'
        st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """
    },

    '9. Pozdrav podle času': {
        'instructions': """
        Vytvořte program, který podle aktuálního času vypíše "Dobré ráno" (6-11), "Dobrý den" (11-18), nebo "Dobrý večer" (18-06).
        """,
        'hint': """
        Aktuální hodinu získáte pomocí výrazu datetime.datetime.now().hour z modulu `datetime`.
        Podle hodnoty aktuální hodiny rozhodněte, který pozdrav vypíšete.
        """,
        'code': """
        import datetime

        # Aktuální hodina
        current_hour = datetime.datetime.now().hour

        if 6 <= current_hour < 11:
            print("Dobré ráno!")
        elif 11 <= current_hour < 18:
            print("Dobrý den!")
        else:
            print("Dobrý večer!")
        """,
        'demonstration': """
import datetime

# Aktuální hodina
current_hour = datetime.datetime.now().hour

if 6 <= current_hour < 11:
    greeting = "Dobré ráno!\\n"
elif 11 <= current_hour < 18:
    greeting = "Dobrý den!\\n"
else:
    greeting = "Dobrý večer!\\n"

st.code(greeting)
        """
    },

    '10. Kontrola sudého/lichého čísla': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na číslo a poté zjistí, zda je toto číslo sudé nebo liché.
        """,
        'hint': """
        Pro získání čísla od uživatele použijte funkci `input()`.
        Zkontrolování, zda je číslo sudé nebo liché, můžete provést pomocí operátoru modulo `%` (výsledek operace `x % 2` je nulový pro sudá čísla).
        Pro výpis výsledku použijte funkci `print()`.
        """,
        'code': """
        try:
            # Získání čísla od uživatele
            number = int(input('Zadejte číslo: '))

            # Kontrola parity čísla
            if number % 2 == 0:
                print(f'Číslo {number} je sudé.')
            else:
                print(f'Číslo {number} je liché.')
        except ValueError:
            print("Neplatný vstup! Zadejte prosím celé číslo.")
        """,
        'demonstration': """
number = st.text_input('Zadejte číslo:')
if number:
    try:
        number = int(number)

        # Kontrola parity čísla
        if number % 2 == 0:
            result = f'Číslo {number} je sudé.\\n'
        else:
            result = f'Číslo {number} je liché.\\n'

        st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím celé číslo.")
        """
    },

    '11. Největší ze dvou čísel': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na dvě čísla a poté vypíše to větší z nich.
        """,
        'hint': """
        Pro získání dvou čísel od uživatele použijte funkci `input()`.
        Zjistění, které číslo je větší, můžete provést pomocí funkce `max()`.
        Pro výpis většího čísla použijte funkci `print()`.
        """,
        'code': """
        try:
            # Získání dvou čísel od uživatele
            cislo_1 = float(input('Zadejte první číslo: '))
            cislo_2 = float(input('Zadejte druhé číslo: '))

            # Výpočet a výpis většího čísla
            print(f'Větší číslo je {max(cislo_1, cislo_2)}.')
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """,
        'demonstration': """
cislo_1 = st.text_input('Zadejte první číslo:')
cislo_2 = st.text_input('Zadejte druhé číslo:')
if cislo_1 and cislo_2:
    try:
        cislo_1 = float(cislo_1)
        cislo_2 = float(cislo_2)

        # Výpočet a výpis většího čísla
        result = f'Větší číslo je {max(cislo_1, cislo_2)}.\\n'

        st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """
    },

    '12. Největší ze dvou čísel (porovnání)': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na dvě čísla a poté vypíše to větší z nich. Při řešení nepoužívejte funkci `max()`.
        """,
        'hint': """
        Pro získání dvou čísel od uživatele použijte funkci `input()`.
        Zjistění, které číslo je větší, můžete provést pomocí porovnávacího operátoru `>`.
        Pro výpis většího čísla použijte funkci `print()`.
        """,
        'code': """
        try:
            # Získání dvou čísel od uživatele
            number1 = float(input('Zadejte první číslo: '))
            number2 = float(input('Zadejte druhé číslo: '))

            # Porovnání čísel a výpis většího
            if number1 > number2:
                print(f'Vetší číslo je {number1}.')
            elif number2 > number1:
                print(f'Vetší číslo je {number2}.')
            else:
                print('Čísla jsou stejná.')
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """,
        'demonstration': """
number1 = st.text_input('Zadejte první číslo:')
number2 = st.text_input('Zadejte druhé číslo:')
if number1 and number2:
    try:
        number1 = float(number1)
        number2 = float(number2)

        # Porovnání čísel a výpis většího
        if number1 > number2:
            result = f'Vetší číslo je {number1}.\\n'
        elif number2 > number1:
            result = f'Vetší číslo je {number2}.\\n'
        else:
            result = 'Čísla jsou stejná.\\n'

        st.code(result)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselné hodnoty.")
        """
    },

    '13. Délka řetězce': {
        'instructions': """
        Vytvořte program, který se zeptá uživatele na řetězec a poté vypíše jeho délku.
        """,
        'hint': """
        Pro získání řetězce od uživatele použijte funkci `input()`.
        Zjištění délky řetězce můžete provést pomocí funkce `len()`.
        Pro výpis délky řetězce použijte funkci `print()`.
        """,
        'code': """
        # Získání řetězce od uživatele
        text = input('Zadejte text: ')

        # Výpočet a výpis délky řetězce
        print(f'Délka zadaného textu je {len(text)} znaků.')
        """,
        'demonstration': """
text = st.text_input('Zadejte text:')
if text:
    # Výpočet a výpis délky řetězce
    result = f'Délka zadaného textu je {len(text)} znaků.\\n'

    st.code(result)
        """
    },

    '14. Seznam jmen': {
        'instructions': """
        Vytvořte program, který obsahuje seznam několika jmen a následně vypíše každé jméno zvlášť.
        """,
        'hint': """
        Seznam jmen můžete vytvořit pomocí datové struktury `list`, tedy pomocí `[]`.
        Pro výpis každého jména zvlášť použijte cyklus `for`.
        Výpis jména proveďte funkcí `print()`.
        """,
        'code': """
        # Vytvoření seznamu jmen
        names = ['Jan', 'Petr', 'Anna', 'Eva']

        # Výpis jmen
        for name in names:
            print(name)
        """,
        'demonstration': """
names = ['Jan', 'Petr', 'Anna', 'Eva']

result = ""
# Výpis jmen
for name in names:
    result += name + "\\n"

st.code(result)
        """
    },

    '15. Výpis obvodového čtverce z písmen X': {
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

    '16. Výpočet obsahu kruhu': {
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

    '17. Výpočet mocnin zadaného čísla': {
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
    },

    '18. Výpočet známkování podle dosažených bodů': {
        'instructions': """
        Vytvořte program, který si od uživatele vyžádá počet bodů, které dosáhl na testu, a maximální počet bodů, který bylo možné získat.
        Poté spočítejte procentuální úspěšnost (v procentech počet dosažených bodů vydělený maximálním počtem bodů a vynásobený 100).
        Na základě vypočítané procentuální úspěšnosti vypište známku podle následujícího rozdělení: 1 (90-100%), 2 (80-90%), 3 (70-80%), 4 (60-70%), 5 (0-60%).
        Ověřte, že uživatel zadal číselný vstup a ošetřete případné chyby při převodu vstupu.
        """,
        'hint': """
        Pro získání vstupních čísel použijte funkci `input()`. Převod na typ čísla proveďte pomocí `float()`. 
        Pro výpočet procentuální úspěšnosti použijte základní matematický výraz. 
        Aby jste vypočítali známku, můžete použít sérii podmínek `if` a `elif`, které porovnávají výsledek s danými intervaly a vrací odpovídající známku.
        Pokud vstup není číslo, zachyťte chybu `ValueError` a vypište uživateli upozornění.
        """,
        'code': """
        try:
            # Získání počtu bodů a maximálního počtu bodů od uživatele
            body = float(input("Zadejte počet dosažených bodů: "))
            max_body = float(input("Zadejte maximální počet bodů: "))

            # Výpočet procentuální úspěšnosti
            uspesnost = (body / max_body) * 100

            # Výpočet známky
            if uspesnost >= 90:
                znamka = 1
            elif uspesnost >= 80:
                znamka = 2
            elif uspesnost >= 70:
                znamka = 3
            elif uspesnost >= 60:
                znamka = 4
            else:
                znamka = 5

            print(f"Při úspěšnosti {uspesnost}% je vaše známka {znamka}.")
        except ValueError:
            print("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """,
        'demonstration': """
output = ''
score = st.text_input("Zadejte počet dosažených bodů:")
max_score = st.text_input("Zadejte maximální počet bodů:")
if score and max_score:
    try:
        score = float(score)
        max_score = float(max_score)

        # Výpočet procentuální úspěšnosti
        success = (score / max_score) * 100

        # Výpočet známky
        if success >= 90:
            grade = 1
        elif success >= 80:
            grade = 2
        elif success >= 70:
            grade = 3
        elif success >= 60:
            grade = 4
        else:
            grade = 5

        output = f"Při úspěšnosti {success}% je vaše známka {grade}.\\n"

        st.code(output)
    except ValueError:
        st.write("Neplatný vstup! Zadejte prosím číselnou hodnotu.")
        """
    }

}

load_tasks("Jednoduché úlohy", tasks)
