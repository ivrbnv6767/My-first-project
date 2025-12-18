import steamlit as st
st.title("My first project")
name = st.text_input("Въведи име")
if name:
  st.write("Hello {name}!")
