import streamlit as st
import re

def sort_names(text):
    lines = text.split('\n')
    names = [re.sub(r'\d+:\d+-\d+:\d+\s+', '', line).strip() for line in lines if line.strip()]
    return '\n'.join(sorted(set(name.upper() for name in names)))

st.title("DJ Lineup Automator :headphones: :musical_keyboard: :technologist:")

st.header("정렬 시킬 Lineup")

col1, col2 = st.columns(2)

with col1:
    st.subheader("금")
    friday_input = st.text_area("", height=200, key="friday_input")

with col2:
    st.subheader("토")
    saturday_input = st.text_area("", height=200, key="saturday_input")

if st.button("Gimme the Lineup", type="primary"):
    st.empty()

    st.divider()
    
    st.header("정렬된 Lineup")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("금")
        st.text_area("", value=sort_names(friday_input), height=200, key="friday_output")

    with col4:
        st.subheader("토")
        st.text_area("", value=sort_names(saturday_input), height=200, key="saturday_output")
