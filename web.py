import streamlit as st
import functions_test

todos = functions_test.get_todos()
def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    print(new_todo)
    todos.append(new_todo)
    functions_test.write_todos(todos)


st.title("Ali's Todo App")
st.subheader("The ultimate todo app that "
             "will boos your productivity")

st.write("Current list of todos, check the box to complete")
todos = functions_test.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions_test.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

st.session_state
