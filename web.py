# https://svidinski-todoweb-web-gzu7yn.streamlit.app/
import streamlit as st
from streamlit import session_state
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To Do App")
st.subheader("This is my to do app.")

st.write("This is an to do app to keep track on daily tasks")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")
