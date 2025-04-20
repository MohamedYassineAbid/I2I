import streamlit as st
import google.generativeai as genai
API_KEY = "AIzaSyCQknFN_Ys0Z5qS6w8zPTBsWmOJqfyk1dw" 
genai.configure(api_key=API_KEY)
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("Chat with Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
def generate_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text
if prompt := st.chat_input("What would you like to know?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            full_response = generate_gemini_response(prompt)
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.stop()
    st.session_state.messages.append({"role": "assistant", "content": full_response})
