import streamlit as st
import functions
st.title("My Todo App")
st.subheader("This is a web todo app")
st.write("This app will help you to manage todos")
todos = functions.read_todo()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)

for index,todo in enumerate(todos):
    checked = st.checkbox(todo,key=todo)
    if checked:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()
st.write("Enter a new todo")
st.text_input(label="Enter a todo",placeholder="Enter a todo",key="new_todo",on_change=add_todo)
# st.session_state