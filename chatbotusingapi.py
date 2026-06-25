import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Ask something")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    st.chat_message("user").write(prompt)

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    answer = response.output_text

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.chat_message("assistant").write(answer)