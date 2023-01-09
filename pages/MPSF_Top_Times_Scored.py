import streamlit as st
import pandas as pd
import numpy as np

with st.container():
    st.title('MPSF Top Times Scored')
    gen = st.selectbox(
        'Gender:',
        ('Men', 'Women')
    )
    event = st.selectbox(
        'Event:',
        ('50 Fr', '100 Fr', '200 Fr', '500 Fr', '1650 Fr',
        '100 Bk', '200 Bk', '100 Br', '200 Br', '100 Fly',
        '200 Fly', '200 IM', '400 IM')
    )

top_times = pd.read_csv('MPSF_' + gen + '.csv', index_col=False).drop(columns='Unnamed: 0')

col1, col2 = st.columns(2)

with col1:
    st.write('Top times in event:')
    if event == '50 Fr':
        st.table(top_times[top_times['Event'] == '50 Freestyle SCY'])
    if event == '100 Fr':
         st.table(top_times[top_times['Event'] == '100 Freestyle SCY'])
    if event == '200 Fr':
         st.table(top_times[top_times['Event'] == '200 Freestyle SCY'])
    if event == '500 Fr':
         st.table(top_times[top_times['Event'] == '500 Freestyle SCY'])
    if event == '1650 Fr':
         st.table(top_times[top_times['Event'] == '1650 Freestyle SCY'])
    if event == '100 Bk':
         st.table(top_times[top_times['Event'] == '100 Backstroke SCY'])
    if event == '200 Bk':
        st.table(top_times[top_times['Event'] == '200 Backstroke SCY'])
    if event == '100 Br':
        st.table(top_times[top_times['Event'] == '100 Breaststroke SCY'])
    if event == '200 Br':
        st.table(top_times[top_times['Event'] == '200 Breaststroke SCY'])
    if event == '100 Fly':
        st.table(top_times[top_times['Event'] == '100 Butterfly SCY'])
    if event == '200 Fly':
        st.table(top_times[top_times['Event'] == '200 Butterfly SCY'])
    if event == '200 IM':
        st.table(top_times[top_times['Event'] == '200 Individual Medley SCY'])
    if event == '400 IM':
        st.table(top_times[top_times['Event'] == '400 Individual Medley SCY'])

with col2:
    st.write('Scoring break down per team:')
    if event == '50 Fr':
        st.table(pd.read_csv('50 Freestyle SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '100 Fr':
         st.table(pd.read_csv('100 Freestyle SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '200 Fr':
         st.table(pd.read_csv('200 Freestyle SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '500 Fr':
         st.table(pd.read_csv('500 Freestyle SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '1650 Fr':
         st.table(pd.read_csv('1650 Freestyle SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '100 Bk':
         st.table(pd.read_csv('100 Backstroke SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '200 Bk':
        st.table(pd.read_csv('200 Backstroke SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '100 Br':
        st.table(pd.read_csv('100 Breaststroke SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '200 Br':
        st.table(pd.read_csv('200 Breaststroke SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '100 Fly':
        st.table(pd.read_csv('100 Butterfly SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '200 Fly':
        st.table(pd.read_csv('200 Butterfly SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '200 IM':
        st.table(pd.read_csv('200 Individual Medley SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))
    if event == '400 IM':
        st.table(pd.read_csv('400 Individual Medley SCY_' + gen.lower() + '_points.csv').sort_values(['Points'], ascending=[False]))

    st.write('Scoring break down for all events:')
    st.table(top_times.groupby('Team')['Points'].sum().sort_values(ascending=False))

    