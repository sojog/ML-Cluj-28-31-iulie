
# streamlit run 07.streamlit.py
import streamlit as st
import pickle
from sklearn.pipeline import Pipeline

st.title("Titanic")
mesaj = st.chat_input("Care este genul tau?")
print(mesaj)

with open("model.pkl", "rb") as freader:
        model:Pipeline = pickle.load(freader)

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
    
    # ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']
    data_to_predict = [1, int(mesaj), 10, 0, 0, 32100, 3, 1]
    # data_to_predict = [3,	1,	34.5,	0,	0,	7.8292,	7,	1]
    raspuns = model.predict([data_to_predict])

    with st.chat_message("ai") as msg:
        st.write("Ai zice ai supravietui:", raspuns)
