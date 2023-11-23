import streamlit as st
from src.user_list import UserList
from src.user import User
from streamlit_extras.switch_page_button import switch_page
import time


def sign_in(user_list: UserList, username: str, password: str) -> bool:
    if user_list.is_user_id_unique(username):
        st.warning("Usuário não cadastrado")
        return False
    else:
        user = user_list.get_user(username)
        authentication = user.authenticate(password)

        if authentication:
            st.session_state["user"] = user
            switch_page("home")
            return True

        else:
            st.warning("Senha incorreta")
            return False


def sign_up(user_list: UserList, username: str, password: str) -> bool:
    if user_list.is_user_id_unique(username):
        user = User(username, password)
        user_list.add_user(user)
        st.info("Usuário cadastrado com sucesso")
        st.session_state["user"] = user
        time.sleep(2)
        switch_page("home")
        return True

    else:
        st.warning("Usuário já cadastrado")
        return False
