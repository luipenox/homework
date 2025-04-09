import streamlit as st


def home():
    st.title('Stránka s úkoly')
    st.write('Autor: Luděk Reif')



home_page = st.Page(home, title="Home", icon=":material/info:")

simple_tasks_page = st.Page('pages/python/simple.py', title='Jednoduché úlohy', icon=":material/task:")

account_pages = [home_page, simple_tasks_page]

pg = st.navigation({"Menu": account_pages})

pg.run()