import streamlit as st

st.title('이민규')
st.header('leemingyu')
st.subheader('대구소프트웨어고등학교')
my_stacks = [ 'swift','c/c++','python','java']
choice = st.selectbox('My stacks',my_stacks)
st.write('You selected {', format(choice),'}')