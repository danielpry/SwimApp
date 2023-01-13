import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

with st.container():
    st.title('MPSF Top Times Scored')
    gen = st.selectbox(
        'Gender:',
        ('Men', 'Women')
    )
    if gen == 'Men':
        gen2 = 'Male'
    if gen == 'Women':
        gen2 = 'Female'

    event = st.selectbox(
        'Event:',
        ('50 Fr', '100 Fr', '200 Fr', '500 Fr', '1650 Fr',
        '100 Bk', '200 Bk', '100 Br', '200 Br', '100 Fly',
        '200 Fly', '200 IM', '400 IM', '200 Medley Relay',
        '400 Medley Relay', '200 Free Relay', '400 Free Relay',
        '800 Free Relay', '1 Meter', '3 Meter', 'Platform')
    )

top_times = pd.read_csv('MPSF_' + gen.lower() + '.csv', index_col=False).drop(columns='Unnamed: 0')

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
    if event == '200 Medley Relay':
        st.table(top_times[top_times['Event'] == '200 Medley Relay'])
    if event == '400 Medley Relay':
        st.table(top_times[top_times['Event'] == '400 Medley Relay'])
    if event == '200 Free Relay':
        st.table(top_times[top_times['Event'] == '200 Free Relay'])
    if event == '400 Free Relay':
        st.table(top_times[top_times['Event'] == '400 Free Relay'])
    if event == '800 Free Relay':
        st.table(top_times[top_times['Event'] == '800 Free Relay'])
    if event == '1 Meter':
        st.table(top_times[top_times['Event'] == '1 Meter'])
    if event == '3 Meter':
        st.table(top_times[top_times['Event'] == '3 Meter'])
    if event == 'Platform':
        st.table(top_times[top_times['Event'] == 'Platform'])

with col2:
    st.write('Scoring break down per team:')
    if event == '50 Fr':
        st.table(pd.read_csv('50 Freestyle SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '100 Fr':
         st.table(pd.read_csv('100 Freestyle SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '200 Fr':
         st.table(pd.read_csv('200 Freestyle SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '500 Fr':
         st.table(pd.read_csv('500 Freestyle SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '1650 Fr':
         st.table(pd.read_csv('1650 Freestyle SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '100 Bk':
         st.table(pd.read_csv('100 Backstroke SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '200 Bk':
        st.table(pd.read_csv('200 Backstroke SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '100 Br':
        st.table(pd.read_csv('100 Breaststroke SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '200 Br':
        st.table(pd.read_csv('200 Breaststroke SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '100 Fly':
        st.table(pd.read_csv('100 Butterfly SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '200 Fly':
        st.table(pd.read_csv('200 Butterfly SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '200 IM':
        st.table(pd.read_csv('200 Individual Medley SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '400 IM':
        st.table(pd.read_csv('400 Individual Medley SCY_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '200 Medley Relay':
        st.table(pd.read_csv('200 Medley Relay_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '400 Medley Relay':
        st.table(pd.read_csv('400 Medley Relay_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '200 Free Relay':
        st.table(pd.read_csv('200 Free Relay_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '400 Free Relay':
        st.table(pd.read_csv('400 Free Relay_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '800 Free Relay':
        st.table(pd.read_csv('800 Free Relay_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '1 Meter':
        st.table(pd.read_csv('1 Meter_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == '3 Meter':
        st.table(pd.read_csv('3 Meter_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    if event == 'Platform':
        st.table(pd.read_csv('Platform_' + gen.lower() + '_points.csv', index_col=False).sort_values(['Points'], ascending=[False]))
    
    
    st.write('Scoring break down for all events:')
    st.table(top_times.groupby('Team')['Points'].sum().sort_values(ascending=False))

# visual
with st.container():
    plot = alt.Chart(top_times).mark_bar().encode(
        x='sum(Points)',
        y='Team',
        color=alt.Color('Event', scale=alt.Scale(scheme='tableau20')),
        order=alt.Order(
            # Sort the segments of the bars by this field
            'Event',
            sort='ascending')
    ).properties(
        width=1850,
        height=500
    ).interactive()

    st.write('Plot of points by event')
    st.altair_chart(plot, use_container_width=True)

    # indivdual points
    x = top_times['Name'].value_counts()
    x = pd.DataFrame(data=x).reset_index().rename(columns={'index':'Name', 'Name':'Number of Events'})
    num_events = pd.merge(top_times, x, on='Name', how='outer')
    pts = num_events.groupby(['Name'])['Points'].sum()
    pts = pd.DataFrame(data=pts).reset_index().rename(columns={'Points':'Total Points'})
    final = pd.merge(num_events, pts, on='Name', how='outer').sort_values(by='Number of Events', ascending=False)

    if gen == 'Women':
        team_list = ['University of Hawaii', 'UC San Diego', 'UC Santa Barbara',
       'University of San Diego', 'Brigham Young University',
       'California State University Bakersfield',
       'University of California, Davis', 'University of Incarnate Word',
       'Cal Poly', 'University of the Pacific']
    if gen == 'Men':
        team_list = ['University of Hawaii', 'UC San Diego', 'UC Santa Barbara', 
        'Brigham Young University', 'California State University Bakersfield',
       'University of Incarnate Word', 'Cal Poly', 'University of the Pacific']

    team = st.selectbox(
        'Team:',
        team_list
    )
    
    show_final = final[(final['Team'] == team) & (final['Gender'] == gen2)].drop(columns=['Gender', 'Team'])
    show_final = show_final[show_final['Name'].str.contains(team) == False]

    st.write('Number of events per swimmer:')
    st.table(show_final)


