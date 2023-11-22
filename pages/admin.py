import streamlit as st

st.title("Consulta")

requested_user_id = st.text_input("Usuário", placeholder="Digite o usuário que deseja buscar")
search = st.button("Buscar")

expander = st.expander(requested_user_id)
expander.write("teste123")

for i in range(2):
    with st.expander("teste"):
        st.write(f"teste{i}")