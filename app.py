import streamlit as st


def home():
    st.title('O kurzu')



home_page = st.Page(home, title="O kurzu", icon=":material/info:")

simple_tasks_page = st.Page('pages/python/introduction.py', title='Jednoduché úlohy', icon=":material/task:")

account_pages = [home_page, simple_tasks_page]

pg = st.navigation({"Informace": account_pages})

pg.run()