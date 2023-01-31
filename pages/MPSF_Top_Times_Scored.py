import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

# defining helper funcs
def getEvents(df, team):
    lst = []
    for i in df[(df['Team'] == team)]['Name'].unique():
        for j in df[(df['Team'] == team) & (df['Name'] == i)]['Event'].unique():
            x = [i, j]
            lst.append(x)
    return(lst)

def toSeconds(a):
    try:
        x = datetime.strptime(a,'%M:%S.%f')
        time = x.minute*60+x.second+x.microsecond/1000000
    except:
        time = float(a)
    return(time)

def seconds_to_mm_ss_ms(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    milliseconds = str(seconds).split('.')[1]
    return '{:02d}:{:02d}.{}'.format(minutes, remaining_seconds, milliseconds)

def GetCustomLineup(df, query):
        df['Time'] = df['Time'].apply(lambda x : toSeconds(x))
        df.drop(columns=['Place', 'Points'], inplace=True)

        final = pd.DataFrame()
        for q in query:
                df_concat = df[(df['Name'].isin([q[0]])) & (df['Event'].isin([q[1]]))]
                final = pd.concat([final, df_concat], ignore_index=True)

        final2 =pd.DataFrame()
        for e in final['Event'].unique():
                f2 = final[final['Event'] == e].sort_values(by='Time', ascending=True)
                f2['Place'] = f2['Time'].rank(ascending=True)
                final2 =pd.concat([final2, f2], ignore_index=True)

        final2['Place'] = final2['Place'].astype(int)

        # add points
        final2.loc[final2['Place'] == 1, 'Points'] = 20
        final2.loc[final2['Place'] == 2, 'Points'] = 17
        final2.loc[final2['Place'] == 3, 'Points'] = 16
        final2.loc[final2['Place'] == 4, 'Points'] = 15
        final2.loc[final2['Place'] == 5, 'Points'] = 14
        final2.loc[final2['Place'] == 6, 'Points'] = 13
        final2.loc[final2['Place'] == 7, 'Points'] = 12
        final2.loc[final2['Place'] == 8, 'Points'] = 11
        final2.loc[final2['Place'] == 9, 'Points'] = 9
        final2.loc[final2['Place'] == 10, 'Points'] = 7
        final2.loc[final2['Place'] == 11, 'Points'] = 6
        final2.loc[final2['Place'] == 12, 'Points'] = 5
        final2.loc[final2['Place'] == 13, 'Points'] = 4
        final2.loc[final2['Place'] == 14, 'Points'] = 3
        final2.loc[final2['Place'] == 15, 'Points'] = 2
        final2.loc[final2['Place'] == 16, 'Points'] = 1
        final2.fillna(0, inplace=True)

        # divide points if tied
        a = final2.duplicated(subset=['Place', 'Event', 'Gender'])
        err = a[a == True].index
        for i in err:
                final2.loc[i, ('Points')] = final2.loc[i]['Points']/2
                final2.loc[i-1, ('Points')] = final2.loc[i-1]['Points']/2

        final2['Time'] = final2['Time'].apply(lambda x : seconds_to_mm_ss_ms(x))
        return(final2)


# front end of website
with st.container():
    st.title('MPSF Top Times Scored')
    
    custom = st.checkbox('Select to choose custom line ups')
    
    gen = st.selectbox(
        'Gender:',
        ('Men', 'Women')
    )
    if gen == 'Men':
        gen2 = 'Male'
    if gen == 'Women':
        gen2 = 'Female'

    top_times = pd.read_csv('MPSF_' + gen.lower() + '.csv', index_col=False).drop(columns='Unnamed: 0')

    if custom:
        if gen == 'Men':
            BYU = st.multiselect(
                'Brigham Young University',
                getEvents(top_times, 'Brigham Young University')
            )
            UCSB = st.multiselect(
                'UC Santa Barbara',
                getEvents(top_times, 'UC Santa Barbara')
            )
            UIW = st.multiselect(
                'University of Incarnate Word',
                getEvents(top_times, 'University of Incarnate Word')
            )
            UCSD = st.multiselect(
                'UC San Diego',
                getEvents(top_times, 'UC San Diego')
            )
            UH = st.multiselect(
                'University of Hawaii',
                getEvents(top_times, 'University of Hawaii')
            )
            CSUB = st.multiselect(
                'California State University Bakersfield',
                getEvents(top_times, 'California State University Bakersfield')
            )
            CP = st.multiselect(
                'Cal Poly',
                getEvents(top_times, 'Cal Poly')
            )
            UOP = st.multiselect(
                'University of the Pacific',
                getEvents(top_times, 'University of the Pacific')
            )
            query = BYU+UCSB+UIW+UCSD+UH+CSUB+CP+UOP
            top_times = GetCustomLineup(top_times, query)

        if gen == 'Women':
            BYUW = st.multiselect(
                'Brigham Young University',
                getEvents(top_times, 'Brigham Young University')
            )
            UCSBW = st.multiselect(
                'UC Santa Barbara',
                getEvents(top_times, 'UC Santa Barbara')
            )
            UIWW = st.multiselect(
                'University of Incarnate Word',
                getEvents(top_times, 'University of Incarnate Word')
            )
            UCSDW = st.multiselect(
                'UC San Diego',
                getEvents(top_times, 'UC San Diego')
            )
            UHW = st.multiselect(
                'University of Hawaii',
                getEvents(top_times, 'University of Hawaii')
            )
            CSUBW = st.multiselect(
                'California State University Bakersfield',
                getEvents(top_times, 'California State University Bakersfield')
            )
            CPW = st.multiselect(
                'Cal Poly',
                getEvents(top_times, 'Cal Poly')
            )
            UOPW = st.multiselect(
                'University of the Pacific',
                getEvents(top_times, 'University of the Pacific')
            )
            USDW = st.multiselect(
                'University of San Diego',
                getEvents(top_times, 'University of San Diego')
            )
            UCDW = st.multiselect(
                'University of California, Davis',
                getEvents(top_times, 'University of California, Davis')
            )
            query = BYUW+UCSBW+UIWW+UCSDW+UHW+CSUBW+CPW+UOPW+USDW+UCDW
            top_times = GetCustomLineup(top_times, query)
    
        st.write('Click arrow below to expand all queried entries')
        st.write(query)

    event = st.selectbox(
        'Event:',
        ('50 Fr', '100 Fr', '200 Fr', '500 Fr', '1650 Fr',
        '100 Bk', '200 Bk', '100 Br', '200 Br', '100 Fly',
        '200 Fly', '200 IM', '400 IM', '200 Medley Relay',
        '400 Medley Relay', '200 Free Relay', '400 Free Relay',
        '800 Free Relay', '1 Meter', '3 Meter', 'Platform')
    )

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
        st.table(top_times[top_times['Event'] == '50 Freestyle SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '100 Fr':
        st.table(top_times[top_times['Event'] == '100 Freestyle SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '200 Fr':
        st.table(top_times[top_times['Event'] == '200 Freestyle SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '500 Fr':
        st.table(top_times[top_times['Event'] == '500 Freestyle SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '1650 Fr':
        st.table(top_times[top_times['Event'] == '1650 Freestyle SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '100 Bk':
        st.table(top_times[top_times['Event'] == '100 Backstroke SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '200 Bk':
        st.table(top_times[top_times['Event'] == '200 Backstroke SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '100 Br':
        st.table(top_times[top_times['Event'] == '100 Breaststroke SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '200 Br':
        st.table(top_times[top_times['Event'] == '200 Breaststroke SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '100 Fly':
        st.table(top_times[top_times['Event'] == '100 Butterfly SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '200 Fly':
        st.table(top_times[top_times['Event'] == '200 Butterfly SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '200 IM':
        st.table(top_times[top_times['Event'] == '200 Individual Medley SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '400 IM':
        st.table(top_times[top_times['Event'] == '400 Individual Medley SCY'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '200 Medley Relay':
        st.table(top_times[top_times['Event'] == '200 Medley Relay'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '400 Medley Relay':
        st.table(top_times[top_times['Event'] == '400 Medley Relay'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '200 Free Relay':
        st.table(top_times[top_times['Event'] == '200 Free Relay'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '400 Free Relay':
        st.table(top_times[top_times['Event'] == '400 Free Relay'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '800 Free Relay':
        st.table(top_times[top_times['Event'] == '800 Free Relay'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '1 Meter':
        st.table(top_times[top_times['Event'] == '1 Meter'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == '3 Meter':
        st.table(top_times[top_times['Event'] == '3 Meter'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    if event == 'Platform':
        st.table(top_times[top_times['Event'] == 'Platform'].groupby('Team')['Points'].sum().sort_values(ascending=False))
    
    
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
