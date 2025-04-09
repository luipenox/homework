import streamlit as st

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
    }

}


def load_tasks():
    st.title('Jednoduché úlohy')

    example = st.selectbox("Vyberte dotaz:", list(tasks.keys()))

    st.markdown("### Zadání")
    st.markdown(tasks[example]['instructions'])

    st.divider()
    _, left_column, middle_column, right_column, _ = st.columns([1, 2, 2, 2, 1])
    with left_column:
        show_hint = st.toggle("nápověda")
    with middle_column:
        show_solution = st.toggle("řešení")
    with right_column:
        show_demonstration = st.toggle("ukázka")
    st.divider()

    if show_hint:
        st.markdown("### Nápověda")
        st.caption(tasks[example]['hint'])

    if show_solution:
        st.markdown("### Řešení")
        st.code(tasks[example]['code'], language='python')

    if show_demonstration:
        st.markdown("### Ukázka")
        exec(tasks[example]['demonstration'])


load_tasks()
