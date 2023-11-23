from dotenv import load_dotenv
from src.user_list import UserList
from dependencies import sign_in, sign_up
import streamlit as st
from streamlit_extras.switch_page_button import switch_page


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_dotenv()

    mocked_user_file_path = "data/mock_user.json"

    user_list = UserList()
    user_list.load_mocked_users(mocked_user_file_path)

    st.session_state["user_list"] = user_list

    st.title(":hospital: Global Solution 2")

    tab_sign_in, tab_sign_up = st.tabs(["Login", "Cadastrar"])

    with tab_sign_in:
        st.header("Login")

        with st.form(key="signin", clear_on_submit=True):
            username = st.text_input("Usuário", placeholder="Insira seu usuário")
            password = st.text_input("Senha", placeholder="Insira sua senha", type="password")
            submit = st.form_submit_button("Entrar")

        if submit:
            sign_in(st.session_state["user_list"], username, password)

    with tab_sign_up:
        st.header("Cadastro")

        with st.form(key="signup", clear_on_submit=True):
            name = st.text_input("Nome", placeholder="Insira seu nome completo")
            gender = st.radio("Sexo", ["Masculino", "Feminino"])
            age = st.number_input("Idade", min_value=0)
            username = st.text_input("Usuário", placeholder="Insira seu usuário")
            password = st.text_input("Senha", placeholder="Insira sua senha", type="password")
            submit = st.form_submit_button("Cadastrar")

        if submit:
            sign_up(st.session_state["user_list"], username, password, name, gender, age)
