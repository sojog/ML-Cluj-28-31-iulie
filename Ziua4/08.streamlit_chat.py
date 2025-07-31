
# streamlit run 07.streamlit.py
import streamlit as st


st.title("Titanic")
mesaj = st.chat_input("Cati ani ai?")
print(mesaj)

print(type(st.session_state))


if not st.session_state.get("messages"):
    st.session_state["messages"] = []


if mesaj:
    print("Ai primit un mesaj nou")
    st.session_state["messages"].append(mesaj)
    print("st.session_state[messages]", st.session_state["messages"])


for mesaj in st.session_state["messages"]:
    with st.chat_message("human") as msg:
        st.write(mesaj)
    
    with st.chat_message("ai") as msg:
        st.write("acesta este raspunsul AI...")
