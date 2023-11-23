import streamlit as st

st.title("Consultar usuário")

requested_user_id = st.text_input("Usuário", placeholder="Digite o usuário que deseja buscar")
search = st.button("Buscar")

if search:
    user = st.session_state["user_list"].get_user(requested_user_id)
    if user is not None:
        st.write(f"**Nome:** {user.name}")
        st.write(f"**Idade:** {str(user.age)}")
        st.write(f"**Sexo:** {user.gender}")

        for e in reversed(user.symptoms):
            date = e[0].strftime("%d/%m/%Y %H:%M")
            with st.expander(date):
                st.write(e[2])

    else:
        st.warning("Usuário não encontrado")