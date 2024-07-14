import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['user_input'] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title('My Todo app')
st.write('This app is to increase your productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='user_input')
