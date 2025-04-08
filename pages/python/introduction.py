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
        """
    }
}


def load_tasks():
    st.title('Jednoduché úlohy')

    example = st.selectbox("Vyberte dotaz:", list(tasks.keys()))
    st.markdown(tasks[example]['instructions'])

    _, left_column, middle_column, right_column, _ = st.columns([1, 2, 2, 2, 1])
    with left_column:
        show_hint = st.toggle("nápověda")
    with middle_column:
        show_solution = st.toggle("řešení")
    with right_column:
        show_demonstration = st.toggle("ukázka")

    if show_hint:
        st.markdown("### Nápověda")
        st.caption(tasks[example]['hint'])

    if show_solution:
        st.markdown("### Řešení")
        st.code(tasks[example]['code'], language='python')

    if show_demonstration:
        st.markdown("### Ukázka")
        text = st.text_input("Zadejte své jméno:")
        if text:
            st.write(f"Ahoj, {text}!")


load_tasks()
