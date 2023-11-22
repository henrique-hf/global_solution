import streamlit as st

st.title("Sintomas")

with st.form("symptoms_form"):
    symptoms = st.text_area("O que você está sentindo?", placeholder="Descreva detalhadamente os sintomas que levaram você a procurar um médico")
    submit = st.form_submit_button("Enviar")

    if submit:
        st.info("As informações já foram passadas para o médico. Dirija-se ao hospital.")
