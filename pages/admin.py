import streamlit as st

st.title("Consulta")

requested_user_id = st.text_input("Usuário", placeholder="Digite o usuário que deseja buscar")
search = st.button("Buscar")

if search:
    if not st.session_state["user_list"].is_user_id_unique(requested_user_id):
        user = st.session_state["user_list"].get_user(requested_user_id)
        st.header("Nome")
        st.write(user.name)
        st.header("Idade")
        st.write(str(user.age))
        st.header("Sexo")
        st.write(user.gender)

        for e in reversed(user.symptoms):
            date = e[0].strftime("%d/%m/%Y %H:%M")
            with st.expander(date):
                st.write(e[2])

    else:
        st.warning("Usuário não encontrado")