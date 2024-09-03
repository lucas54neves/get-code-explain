import streamlit as st
from openai import OpenAI

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key", key="chatbot_api_key", type="password"
    )
st.title("💬 Get Code Explain")
st.caption("AI that gets code explain for you.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Send me your code to get explanation.",
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input(placeholder="Write your code here..."):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=st.session_state.messages
    )

    msg = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
