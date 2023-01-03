import streamlit as st
import pandas as pd

st.set_page_config(page_title='Line Up Camparison', layout='wide')

with st.container():
    st.title('Web app to compare meet lineups')
    gender = st.selectbox(
        'Gender:',
        ('Men', 'Women')
    )

col1, col2 = st.columns(2)

with col1:
    meet =st.selectbox(
        'Meet:',
        ('TCU', 'UNLV', 'Midseason 2022', 'Midseason 2021', 'MPSF 2022'),
        key='col1'
    )
    if gender == 'Men':
        if meet == 'TCU':
            df = pd.read_excel('BYUvTCU_men.xlsx')
        if meet == 'UNLV':
            df = pd.read_excel('BYUvUNLV_men.xlsx')
        if meet == 'Midseason 2022':
            df = pd.read_excel('midseason_men.xlsx')
        if meet == 'Midseason 2021':
            df = pd.read_excel('Dixie21_men.xlsx')
        if meet == 'MPSF 2022':
            df = pd.read_excel('MPSF22_men.xlsx')
    if gender == 'Women':
        if meet == 'TCU':
            df = pd.read_excel('BYUvTCU_women.xlsx')
        if meet == 'UNLV':
            df = pd.read_excel('BYUvUNLV_women.xlsx')
        if meet == 'Midseason 2022':
            df = pd.read_excel('midseason_women.xlsx')
        if meet == 'Midseason 2021':
            df = pd.read_excel('Dixie21_women.xlsx')
        if meet == 'MPSF 2022':
            df = pd.read_excel('MPSF22_women.xlsx')
    st.table(df)
    


with col2:
    meet2 =st.selectbox(
        'Meet:',
        ('TCU', 'UNLV', 'Midseason 2022', 'Midseason 2021', 'MPSF 2022'),
        key='col2'
    )
    if gender == 'Men':
        if meet2 == 'TCU':
            df2 = pd.read_excel('BYUvTCU_men.xlsx')
        if meet2 == 'UNLV':
            df2 = pd.read_excel('BYUvUNLV_men.xlsx')
        if meet2 == 'Midseason 2022':
            df2 = pd.read_excel('midseason_men.xlsx')
        if meet2 == 'Midseason 2021':
            df2 = pd.read_excel('Dixie21_men.xlsx')
        if meet2 == 'MPSF 2022':
            df2 = pd.read_excel('MPSF22_men.xlsx')
    if gender == 'Women':
        if meet2 == 'TCU':
            df2 = pd.read_excel('BYUvTCU_women.xlsx')
        if meet2 == 'UNLV':
            df2 = pd.read_excel('BYUvUNLV_women.xlsx')
        if meet2 == 'Midseason 2022':
            df2 = pd.read_excel('midseason_women.xlsx')
        if meet2 == 'Midseason 2021':
            df2 = pd.read_excel('Dixie21_women.xlsx')
        if meet2 == 'MPSF 2022':
            df2 = pd.read_excel('MPSF22_women.xlsx')
    st.table(df2)