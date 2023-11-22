import streamlit as st
from src.user_list import UserList
from streamlit_extras.switch_page_button import switch_page


def sign_in(user_list: UserList):
    st.title("Login")
    with st.form(key="signin", clear_on_submit=True):
        username = st.text_input("Usuário", placeholder="Insira seu usuário")
        password = st.text_input("Senha", placeholder="Insira sua senha", type="password")
        submit = st.form_submit_button("Entrar")

    if submit:
        #check if user exists
        if user_list.is_user_id_unique(username):
            st.warning("Usuário não cadastrado")
        else:
            user = user_list.get_user(username)
            authentication = user.authenticate(password)

            if authentication:
                #abrir outra pagina
                # st.warning("Senha correta")
                switch_page("home")

            else:
                st.warning("Senha incorreta")