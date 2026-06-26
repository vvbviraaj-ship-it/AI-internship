import streamlit as st
import google.generativeai as genai
import time


st.set_page_config(
    page_title="Gemini AI Assistant",
    page_icon="🤖",
    layout="centered"
)


st.markdown("""
<style>
.stApp{
    background-color:#0E1117;
}

h1{
    text-align:center;
}

footer{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.title("🤖 Gemini Assistant")

    api_key = "AQ.Ab8RN6Kx4CHeUGO2_hHdFMKShxOP7nWeYHNyKiHrb2PpIMIP3Q"

    st.divider()

    temperature = st.slider(
        "Creativity",
        0.0,
        1.0,
        0.7,
        0.1
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()



genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={
        "temperature": temperature
    }
)



st.title("💬 Gemini AI Chatbot")

st.caption("Powered by Google Gemini")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        try:

            response = model.generate_content(prompt)

            answer = response.text

            typed = ""

            for word in answer.split():

                typed += word + " "

                placeholder.markdown(typed + "▌")

                time.sleep(0.02)

            placeholder.markdown(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:

            st.error(f"Error: {e}")