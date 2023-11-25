import streamlit as st
from openai import OpenAI
from src.llm import generate_response, generate_question
from src.util import read_text_file
import datetime

st.title("Minha página")

client = OpenAI()

user = st.session_state["user"]

tab_new_symptom, tab_history, tab_profile = st.tabs(["Novo atendimento", "Histórico", "Perfil"])

with tab_new_symptom:
    st.header("Sintomas")

    with st.form("symptoms_form"):
        symptoms = st.text_area("O que você está sentindo?", placeholder="Descreva detalhadamente os sintomas que levaram você a procurar um médico")
        submit = st.form_submit_button("Enviar")

        if submit:
            role_file_path = "src/prompt/role.txt"
            role = read_text_file(role_file_path)

            instruction_file_path = "src/prompt/instruction.txt"
            instruction = read_text_file(instruction_file_path)

            example_file_path = "src/prompt/example.txt"
            example = read_text_file(example_file_path)

            question = generate_question(instruction, symptoms, example)
            # st.write(question)

            response = generate_response(client, role, question)
            # response = "Teste mockado"
            # st.write(response)

            user.save_symptom(datetime.datetime.now(), symptoms, response)
            # st.write(user.symptoms)

            st.info("As informações já foram passadas para o médico. Dirija-se ao hospital.")


with tab_history:
    if len(user.symptoms) > 0:
        for e in reversed(user.symptoms):
            date = e[0].strftime("%d/%m/%Y %H:%M")
            with st.expander(date):
                st.write(e[1])
    else:
        st.write("Sem histórico")

with tab_profile:
    st.write(f"**Nome:** {user.name}")
    st.write(f"**Idade:** {str(user.age)}")
    st.write(f"**Sexo:** {user.gender}")
    st.write(f"**Número de atendimentos:** {str(len(user.symptoms))}")
    if len(user.symptoms) > 0:
        st.write(f"**Data do último atendimento:** {user.symptoms[-1][0].strftime('%d/%m/%Y %H:%M')}")
    else:
        st.write(f"**Data do último atendimento:** Sem histórico")
