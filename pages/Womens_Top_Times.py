import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
from regex import search

#############################
# Defining Functions        #
#############################

def Get_Team_times(team, gender, event, course, season):
    time_url = 'https://www.swimcloud.com/team/{}/times/?page=1&gender={}&event={}&course={}&season={}'
    # making a GET request
    r = requests.get(time_url.format(team, gender, event, course, season))
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_="c-table-clean--responsive")

    # getting data
    times =[]
    for c in s.find_all('a'):
        times.append(c.text.strip())

    # cleaning data
    times = [e for e in times if e not in ('', 'JRS', 'R', 'X', 'A', 'U', 
                                            'P66', 'PQT', 'OPEN', 'YMCA',
                                            'RQAL', 'B', 'CL-B', 'QUAL', 'None',
                                            'NICA', 'NICB')]

            # remove values conataining \n
    for i in times:
        if search('\n', i):
            times.remove(i)
        else:
            pass

    # cleaning data
    times = list(filter(lambda x: x != '', times))
    times = [times[i:i+3] for i in range(0, len(times), 3)]

    # creating df
    times_df = pd.DataFrame(times, columns=['Swimmer', 'Meet', 'Time'])
    times_df['Event'] = event
    times_df['Team'] = team  
    teams_dict = {73: 'Virginia', 105: 'Texas', 102: 'Southern California', 174: 'Louisville', 
                127: 'Auburn', 394: 'NC State', 117: 'Florida', 65: 'Alabama', 89: 'Michigan', 
                47: 'Arkansas', 92: 'Indiana', 431: 'Missouri', 124: 'Georgia', 
                44: 'Tennessee', 112: 'Stanford', 77: 'Florida State', 110: 'California', 
                393: 'Ohio State', 56: 'Louisiana State', 176: 'Kentucky', 98: 'Wisconsin', 
                280: 'Duke', 60: 'North Carolina', 401: 'Northwestern', 80: 'Texas A&M', 
                107: 'UCLA', 87: 'Arizona State', 95: 'South Carolina', 27: 'Purdue', 43: 'Rutgers'}
    event_dict = {7200 : '200 Med Relay', 7400 : '400 Med Relay', 11000 : '1000 FR', 
                11650 : '1650 FR', 1200 : '200 FR', 2100 : '100 BK', 
                3100 : '100 BR', 4200 : '200 FL', 150 : '50 FR', 
                1100 : '100 FR', 2200 : '200 BK', 3200 : '200 BR', 
                1500 : '500 FR', 4100 : '100 FL', 5200 : '200 IM', 
                5400 : '400 IM', 6200 : '200 FR Relay', 6400 : '400 FR Relay'}
    times_df1 = times_df.replace({'Event': event_dict})
    times_df1 = times_df1.replace({'Team': teams_dict})
    return(times_df1)


def GetTopTimes():
        teams = [73, 105, 102, 174, 127, 394, 117, 65, 89, 47, 92, 431, 124, 
                44, 112, 77, 110, 393, 56, 176, 98, 280, 60, 401, 80, 107, 87,
                95, 27, 43]

        events = [7200, 11000, 1200, 2100, 3100, 4200, 150, 1100,
                2200, 3200, 1500, 4100, 5200, 6200]

        team_times = pd.DataFrame()
        for i in teams:
                for j in events:
                        try: 
                                x = Get_Team_times(i, 'F', j, 'Y', 26)
                                team_times = pd.concat([team_times, x])
                        except:
                                pass
        team_times = team_times[team_times.index <= 4]
        team_times.reset_index(inplace=True)
        final = team_times.pivot(index=['Team', 'index'], columns='Event', values='Time').replace(np.nan, '', regex=True)
        final.to_excel('pages\midseason_toptimes.xlsx')
        return(final)

############################
# Front End                #
############################

with st.container():
    st.title('Top Times for Women')
    st.write('Click button below to generate table (will take a couple minutes)')
    if st.button('Update Times'):
        GetTopTimes()
        st.table(pd.read_excel('pages\midseason_toptimes.xlsx'))