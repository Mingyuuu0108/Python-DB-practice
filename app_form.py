import pandas as pd
import streamlit as st
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

st.subheader('회원목록')
df = pd.read_sql('SELECT * FROM users', con)

st.subheader('회원가입')

with st.form('my_form', clear_on_submit=True):
    st.info('다음 양식을 모두 입력한 후 제출해주세요.')
    uid = st.text_input('아이디', max_chars=12)
    uname = st.text_input('이름', max_chars=10)
    upw = st.text_input('비밀번호', type='password')
    upw_chk = st.text_input('비밀번호 재입력', type='password')
    ubd = st.date_input('생년월일')
    ugender = st.radio('성별', options=['남','여'], horizontal=True)

    submitted = st.form_submit_button('제출')
    if submitted:

        if upw != upw_chk:
            st.warning('비밀번호를 확인하세요')
            st.stop()

        st.success(f'{uid} {uname} {upw} {ubd} {ugender}')
        cur.execute(f"INSERT INTO users VALUES"
                    f"'{uid}','{uname}','{upw}',"
                    f"'{ubd}','{ugender}',CURRENT_DATE)")
        con.commit()
