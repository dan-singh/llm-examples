import openai
import streamlit as st
#from llama_index import VectorStoreIndex, ServiceContext, Document
#from llama_index.llms import OpenAI
import openai
#from llama_index import SimpleDirectoryReader
from PIL import Image

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="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", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

image = Image.open('pages/directv_hz_rgb_pos.png')
#st.image(image, caption='')
st.image(image, caption=None, width=100, use_column_width=100, clamp=True, channels="RGB", output_format="auto")

#st.title(" Chatbot")
#st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
#if "messages" not in st.session_state:
#    st.session_state["messages"] = [{"role": "assistant", "content": ""}]

#for msg in st.session_state.messages:
#    st.chat_message(msg["role"]).write(msg["content"])

file = st.file_uploader("Choose a text file", type="txt")

# If the file was uploaded successfully
if file is not None:

    # Get the text from the file
    text = file.read()

    # Analyze the text with OpenAI
    response = openai.Completion.create(
        engine="davinci",
        text=text,
        temperature=0.7,
        top_p=0.9,
        presence_penalty=0.2,
        stop_token="<|endoftext|>",
    )

    # Display the results
    st.write(response.choices[0].text)
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})

    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-4", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)