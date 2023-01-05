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
        ('BYU vs TCU', 'BYU vs UNLV', 'BYU Midseason 2022', 'BYU Midseason 2021', 
        'BYU MPSF 2022', 'Hawaii Midseason 2022', 'Hawaii Midseason 2021',
        'Hawaii MPSF 2022', 'UCSD Midseason 2022', 'UCSD Midseason 2021',
        'UCSD MPSF 2022'),
        key='col1'
    )
    if gender == 'Men':
        if meet == 'BYU vs TCU':
            df = pd.read_excel('BYUvTCU_men.xlsx')
        if meet == 'BYU vs UNLV':
            df = pd.read_excel('BYUvUNLV_men.xlsx')
        if meet == 'BYU Midseason 2022':
            df = pd.read_excel('BYU_mid22_men.xlsx')
        if meet == 'BYU Midseason 2021':
            df = pd.read_excel('BYU_mid21_men.xlsx')
        if meet == 'BYU MPSF 2022':
            df = pd.read_excel('BYU_MPSF22_men.xlsx')
        if meet == 'Hawaii Midseason 2022':
            df = pd.read_excel('Hawaii_mid22_men.xlsx')
        if meet == 'Hawaii Midseason 2021':
            df = pd.read_excel('Hawaii_mid21_men.xlsx')
        if meet == 'Hawaii MPSF 2022':
            df = pd.read_excel('Hawaii_MPSF22_men.xlsx')
        if meet == 'UCSD Midseason 2022':
            df = pd.read_excel('UCSD_mid22_men.xlsx')
        if meet == 'UCSD Midseason 2021':
            df = pd.read_excel('UCSD_mid21_men.xlsx')
        if meet == 'UCSD MPSF 2022':
            df = pd.read_excel('UCSD_MPSF22_men.xlsx')
    if gender == 'Women':
        if meet == 'BYU vs TCU':
            df = pd.read_excel('BYUvTCU_women.xlsx')
        if meet == 'BYU vs UNLV':
            df = pd.read_excel('BYUvUNLV_women.xlsx')
        if meet == 'BYU Midseason 2022':
            df = pd.read_excel('BYU_mid22_women.xlsx')
        if meet == 'BYU Midseason 2021':
            df = pd.read_excel('BYU_mid21_women.xlsx')
        if meet == 'BYU MPSF 2022':
            df = pd.read_excel('BYU_MPSF22_women.xlsx')
        if meet == 'Hawaii Midseason 2022':
            df = pd.read_excel('Hawaii_mid22_women.xlsx')
        if meet == 'Hawaii Midseason 2021':
            df = pd.read_excel('Hawaii_mid21_women.xlsx')
        if meet == 'Hawaii MPSF 2022':
            df = pd.read_excel('Hawaii_MPSF22_women.xlsx')
        if meet == 'UCSD Midseason 2022':
            df = pd.read_excel('UCSD_mid22_women.xlsx')
        if meet == 'UCSD Midseason 2021':
            df = pd.read_excel('UCSD_mid21_women.xlsx')
        if meet == 'UCSD MPSF 2022':
            df = pd.read_excel('UCSD_MPSF22_women.xlsx')
    st.table(df)
    

with col2:
    meet2 =st.selectbox(
        'Meet:',
        ('BYU vs TCU', 'BYU vs UNLV', 'BYU Midseason 2022', 'BYU Midseason 2021', 
        'BYU MPSF 2022', 'Hawaii Midseason 2022', 'Hawaii Midseason 2021',
        'Hawaii MPSF 2022', 'UCSD Midseason 2022', 'UCSD Midseason 2021',
        'UCSD MPSF 2022'),
        key='col2'
    )
    if gender == 'Men':
        if meet2 == 'BYU vs TCU':
            df2 = pd.read_excel('BYUvTCU_men.xlsx')
        if meet2 == 'BYU vs UNLV':
            df2 = pd.read_excel('BYUvUNLV_men.xlsx')
        if meet2 == 'BYU Midseason 2022':
            df2 = pd.read_excel('BYU_mid22_men.xlsx')
        if meet2 == 'BYU Midseason 2021':
            df2 = pd.read_excel('BYU_mid21_men.xlsx')
        if meet2 == 'BYU MPSF 2022':
            df2 = pd.read_excel('BYU_MPSF22_men.xlsx')
        if meet2 == 'Hawaii Midseason 2022':
            df2 = pd.read_excel('Hawaii_mid22_men.xlsx')
        if meet2 == 'Hawaii Midseason 2021':
            df2 = pd.read_excel('Hawaii_mid21_men.xlsx')
        if meet2 == 'Hawaii MPSF 2022':
            df2 = pd.read_excel('Hawaii_MPSF22_men.xlsx')
        if meet2 == 'UCSD Midseason 2022':
            df2 = pd.read_excel('UCSD_mid22_men.xlsx')
        if meet2 == 'UCSD Midseason 2021':
            df2 = pd.read_excel('UCSD_mid21_men.xlsx')
        if meet2 == 'UCSD MPSF 2022':
            df2 = pd.read_excel('UCSD_MPSF22_men.xlsx')
    if gender == 'Women':
        if meet2 == 'BYU vs TCU':
            df2 = pd.read_excel('BYUvTCU_women.xlsx')
        if meet2 == 'BYU vs UNLV':
            df2 = pd.read_excel('BYUvUNLV_women.xlsx')
        if meet2 == 'BYU Midseason 2022':
            df2 = pd.read_excel('BYU_mid22_women.xlsx')
        if meet2 == 'BYU Midseason 2021':
            df2 = pd.read_excel('BYU_mid21_women.xlsx')
        if meet2 == 'BYU MPSF 2022':
            df2 = pd.read_excel('BYU_MPSF22_women.xlsx')
        if meet2 == 'Hawaii Midseason 2022':
            df2 = pd.read_excel('Hawaii_mid22_women.xlsx')
        if meet2 == 'Hawaii Midseason 2021':
            df2 = pd.read_excel('Hawaii_mid21_women.xlsx')
        if meet2 == 'Hawaii MPSF 2022':
            df2 = pd.read_excel('Hawaii_MPSF22_women.xlsx')
        if meet2 == 'UCSD Midseason 2022':
            df2 = pd.read_excel('UCSD_mid22_women.xlsx')
        if meet2 == 'UCSD Midseason 2021':
            df2 = pd.read_excel('UCSD_mid21_women.xlsx')
        if meet2 == 'UCSD MPSF 2022':
            df2 = pd.read_excel('UCSD_MPSF22_women.xlsx')
    st.table(df2)