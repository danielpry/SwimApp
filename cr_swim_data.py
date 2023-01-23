import pandas as pd
import numpy as np

def cr_swim_data():
    # load data
    score = pd.read_csv('Report.csv')

    # clean data
    score = score[['="RANK"', '="full_name_computed"', '="full_desc"', '="team_short_name"',  '="swim_time"']]
    score['="RANK"'] = score['="RANK"'].str.replace('="', '')
    score['="full_desc"'] = score['="full_desc"'].str.replace('="', '')
    score['="team_short_name"'] = score['="team_short_name"'].str.replace('="', '')
    score['="swim_time"'] = score['="swim_time"'].str.replace('="', '')
    score['="RANK"'] = score['="RANK"'].str.replace('"', '')
    score['="full_desc"'] = score['="full_desc"'].str.replace('"', '')
    score['="team_short_name"'] = score['="team_short_name"'].str.replace('"', '')
    score['="swim_time"'] = score['="swim_time"'].str.replace('"', '')
    score_mod = score.rename(columns={'="RANK"': 'Place', '="full_name_computed"': 'Name', 
                        '="full_desc"': 'Event', '="team_short_name"': 'Team',
                        '="swim_time"': 'Time'})


    # add points
    score_mod.loc[score_mod['Place'] == '1', 'Points'] = 20
    score_mod.loc[score_mod['Place'] == '2', 'Points'] = 17
    score_mod.loc[score_mod['Place'] == '3', 'Points'] = 16
    score_mod.loc[score_mod['Place'] == '4', 'Points'] = 15
    score_mod.loc[score_mod['Place'] == '5', 'Points'] = 14
    score_mod.loc[score_mod['Place'] == '6', 'Points'] = 13
    score_mod.loc[score_mod['Place'] == '7', 'Points'] = 12
    score_mod.loc[score_mod['Place'] == '8', 'Points'] = 11
    score_mod.loc[score_mod['Place'] == '9', 'Points'] = 9
    score_mod.loc[score_mod['Place'] == '10', 'Points'] = 7
    score_mod.loc[score_mod['Place'] == '11', 'Points'] = 6
    score_mod.loc[score_mod['Place'] == '12', 'Points'] = 5
    score_mod.loc[score_mod['Place'] == '13', 'Points'] = 4
    score_mod.loc[score_mod['Place'] == '14', 'Points'] = 3
    score_mod.loc[score_mod['Place'] == '15', 'Points'] = 2
    score_mod.loc[score_mod['Place'] == '16', 'Points'] = 1
    score_mod.fillna(0, inplace=True)

    # add gender
    score_mod['Gender'] = None
    for i, val in enumerate(score_mod['Event']):
        if 'Female' in val:
            score_mod['Gender'].loc[i] = 'Female'
        if 'Male' in val:
            score_mod['Gender'].loc[i] = 'Male'

    score_mod['Event'] = score_mod['Event'].str.replace(' Female', '')
    score_mod['Event'] = score_mod['Event'].str.replace(' Male', '')

    # drop unneeded events
    for i, val in enumerate(score_mod['Event']):
        if val in ['1000 Freestyle SCY', '50 Backstroke SCY', '50 Breaststroke SCY', '50 Butterfly SCY', '100 Individual Medley SCY']:
            score_mod.drop(i, inplace=True)
    score_mod['Event'].unique()

    # adding diving and relays
    d1 = {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['Jacqueline Samaniego', 'Tessa Watkins', 'Alexia Jackson', 'Hailey Johnson', 'Isabelle Lombardi', 'Emma Lund', 'Isabella Plantz', 'Summer Taylor'], 
        'Event':['1 Meter', '1 Meter', '1 Meter', '1 Meter', '1 Meter', '1 Meter', '1 Meter', '1 Meter'], 
        'Team':['Cal Poly', 'Brigham Young University', 'Brigham Young University', 'Brigham Young University', 'University of Hawaii', 'University of Hawaii', 'University of Hawaii', 'University of Incarnate Word'], 
        'Time':['298.80', '292.50', '264.50', '263.35', '259.90', '253.65', '247.90', '246.38'], 
        'Points':[20, 17, 16, 15, 14, 13, 12, 11], 
        'Gender':['Female','Female','Female','Female','Female','Female','Female','Female']}
    df1 = pd.DataFrame(data=d1)

    d2= {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['Alexia Jackson', 'Tessa Watkins', 'Emma Lund', 'Hailey Johnson', 'Chloe Brown', 'Kellyann Lim', 'Summer Taylor', 'Annika Donez'], 
        'Event':['3 Meter', '3 Meter', '3 Meter', '3 Meter', '3 Meter', '3 Meter', '3 Meter', '3 Meter'], 
        'Team':['Brigham Young University', 'Brigham Young University', 'University of Hawaii', 'Brigham Young University', 'California State University Bakersfield', 'Cal Poly', 'University of Incarnate Word', 'University of Hawaii'], 
        'Time':['336.05','315.00','290.60','282.45','268.50','255.55','250.13','248.35'], 
        'Points':[20, 17, 16, 15, 14, 13, 12, 11], 
        'Gender':['Female','Female','Female','Female','Female','Female','Female','Female']}
    df2 = pd.DataFrame(data=d2)

    d3 = {'Place':['1','2','3','4','5','6','7'], 
        'Name':['Elma Lund', 'Alexia Jackson', 'Sophia DeBergh', 'Annika Donez', 'Isabelle Lombardi', 'Tessa Watkins', 'Isabella Plantz'], 
        'Event':['Platform','Platform','Platform','Platform','Platform','Platform','Platform'], 
        'Team':['University of Hawaii', 'Brigham Young University', 'Brigham Young University', 'University of Hawaii', 'University of Hawaii', 'Brigham Young University', 'University of Hawaii'], 
        'Time':['278.00','252.80','203.80','194.90','178.20','174.45','170.20'], 
        'Points':[20, 17, 16, 15, 14, 13, 12], 
        'Gender':['Female','Female','Female','Female','Female','Female','Female']}
    df3 = pd.DataFrame(data=d3)

    d4 = {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['Mickey Strauss', 'Max Powell', 'Dyson Modica', 'Chase Hindmarsh', 'Juan Gonzalez', 'Mackaby Pennington', 'Cody Dreesen', 'Lyndon Kov'], 
        'Event':['1 Meter', '1 Meter', '1 Meter', '1 Meter', '1 Meter', '1 Meter', '1 Meter', '1 Meter'], 
        'Team':['Brigham Young University', 'Cal Poly', 'California State University Bakersfield', 'Brigham Young University', 'University of Hawaii', 'University of Hawaii', 'Brigham Young University', 'University of Incarnate Word'], 
        'Time':['371.03','369.90','362.75','333.55','332.30','327.60','303.80','302.40'], 
        'Points':[20, 17, 16, 15, 14, 13, 12, 11], 
        'Gender':['Male','Male','Male','Male','Male','Male','Male','Male']}
    df4 = pd.DataFrame(data=d4)

    d5 = {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['Mickey Strauss', 'Max Powell', 'Dyson Modica', 'Chase Hindmarsh', 'Juan Gonzalez', 'Mackaby Pennington', 'Nathan Marshall', 'Dawson Mozisek'], 
        'Event':['3 Meter', '3 Meter', '3 Meter', '3 Meter', '3 Meter', '3 Meter', '3 Meter', '3 Meter'], 
        'Team':['Brigham Young University', 'Cal Poly', 'California State University Bakersfield', 'Brigham Young University', 'University of Hawaii', 'University of Hawaii', 'Brigham Young University', 'University of Incarnate Word'], 
        'Time':['391.95','386.80','368.30','346.88','343.20','304.30','288.53','283.58'], 
        'Points':[20, 17, 16, 15, 14, 13, 12, 11], 
        'Gender':['Male','Male','Male','Male','Male','Male','Male','Male']}
    df5 = pd.DataFrame(data=d5)
    df5

    d6 = {'Place':['1','2','3','4','5'], 
        'Name':['Mackaby Pennington', 'Juan Gonzalez', 'Mickey Strauss', 'Carter Davis', 'Cody Dreesen'], 
        'Event':['Platform','Platform','Platform','Platform','Platform'], 
        'Team':['University of Hawaii', 'University of Hawaii', 'Brigham Young University', 'Brigham Young University', 'Brigham Young University'], 
        'Time':['338.05','321.10','319.30','283.80','243.10'], 
        'Points':[20, 17, 16, 15, 14], 
        'Gender':['Male','Male','Male','Male','Male']}
    df6 = pd.DataFrame(data=d6)

    d7 = {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['University of Incarnate Word', 'Brigham Young University', 'UC Santa Barbara', 'University of Hawaii', 'California State University Bakersfield', 'UC San Diego', 'Cal Poly', 'University of the Pacific'], 
        'Event':['200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay'], 
        'Team':['University of Incarnate Word', 'Brigham Young University', 'UC Santa Barbara', 'University of Hawaii', 'California State University Bakersfield', 'UC San Diego', 'Cal Poly', 'University of the Pacific'], 
        'Time':['1:19.52', '1:19.65', '1:19.94', '1:20.95', '1:21.05', '1:21.14', '1:22.21', '1:22.71'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22], 
        'Gender':['Male','Male','Male','Male','Male','Male','Male','Male']}
    df7 = pd.DataFrame(data=d7)

    d8 = {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['UC Santa Barbara', 'University of Hawaii', 'Brigham Young University', 'University of Incarnate Word', 'UC San Diego', 'California State University Bakersfield', 'University of the Pacific', 'Cal Poly'], 
        'Event':['400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay'], 
        'Team':['UC Santa Barbara', 'University of Hawaii', 'Brigham Young University', 'University of Incarnate Word', 'UC San Diego', 'California State University Bakersfield', 'University of the Pacific', 'Cal Poly'], 
        'Time':['2:52.96', '2:54.41', '2:55.06', '2:55.28', '2:57.18', '2:59.53', '3:01.39', '3:02.32'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22], 
        'Gender':['Male','Male','Male','Male','Male','Male','Male','Male']}
    df8 = pd.DataFrame(data=d8)

    d9 = {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['UC Santa Barbara', 'UC San Diego', 'Brigham Young University', 'University of Incarnate Word', 'California State University Bakersfield', 'University of Hawaii', 'University of the Pacific', 'Cal Poly'], 
        'Event':['800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay'], 
        'Team':['UC Santa Barbara', 'UC San Diego', 'Brigham Young University', 'University of Incarnate Word', 'California State University Bakersfield', 'University of Hawaii', 'University of the Pacific', 'Cal Poly'], 
        'Time':['6:31.27', '6:33.66', '6:34.65', '6:36.91', '6:36.98', '6:44.53', '6:44.69', '6:58.02'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22], 
        'Gender':['Male','Male','Male','Male','Male','Male','Male','Male']}
    df9 = pd.DataFrame(data=d9)

    d10 = {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['UC Santa Barbara', 'Brigham Young University', 'University of Incarnate Word', 'University of Hawaii', 'UC San Diego', 'California State University Bakersfield', 'Cal Poly', 'University of the Pacific'], 
        'Event':['200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay'], 
        'Team':['UC Santa Barbara', 'Brigham Young University', 'University of Incarnate Word', 'University of Hawaii', 'UC San Diego', 'California State University Bakersfield', 'Cal Poly', 'University of the Pacific'], 
        'Time':['1:26.63', '1:26.74', '1:27.87', '1:28.08', '1:29.13', '1:29.45', '1:31.66', '1:32.90'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22], 
        'Gender':['Male','Male','Male','Male','Male','Male','Male','Male']}
    df10 = pd.DataFrame(data=d10)

    d11 = {'Place':['1','2','3','4','5','6','7','8'], 
        'Name':['Brigham Young University', 'UC Santa Barbara', 'University of Incarnate Word', 'UC San Diego', 'California State University Bakersfield', 'University of Hawaii', 'University of the Pacific', 'Cal Poly'], 
        'Event':['400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay'], 
        'Team':['Brigham Young University', 'UC Santa Barbara', 'University of Incarnate Word', 'UC San Diego', 'California State University Bakersfield', 'University of Hawaii', 'University of the Pacific', 'Cal Poly'], 
        'Time':['3:10.23', '3:10.38', '3:11.53', '3:15.32', '3:15.69', '3:15.81', '3:19.29', '3:20.47'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22], 
        'Gender':['Male','Male','Male','Male','Male','Male','Male','Male']}
    df11 = pd.DataFrame(data=d11)

    d12 = {'Place':['1','2','3','4','5','6','7','8', '9', '10'], 
        'Name':['University of Hawaii', 'UC San Diego', 'Brigham Young University', 'University of California, Davis', 'University of San Diego', 'UC Santa Barbara', 'California State University Bakersfield', 'University of the Pacific', 'Cal Poly', 'University of Incarnate Word'], 
        'Event':['200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay','200 Free Relay'], 
        'Team':['University of Hawaii', 'UC San Diego', 'Brigham Young University', 'University of California, Davis', 'University of San Diego', 'UC Santa Barbara', 'California State University Bakersfield', 'University of the Pacific', 'Cal Poly', 'University of Incarnate Word'], 
        'Time':['1:29.63', '1:30.00', '1:32.85', '1:33.59', '1:33.99', '1:34.30', '1:35.75', '1:35.93', '1:36.33', '1:36.82'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22, 18, 14], 
        'Gender':['Female','Female','Female','Female','Female','Female','Female','Female','Female','Female']}
    df12 = pd.DataFrame(data=d12)

    d13 = {'Place':['1','2','3','4','5','6','7','8', '9', '10'], 
        'Name':['University of Hawaii', 'UC San Diego', 'Brigham Young University', 'University of California, Davis', 'UC Santa Barbara', 'California State University Bakersfield', 'University of the Pacific', 'University of San Diego', 'Cal Poly', 'University of Incarnate Word'], 
        'Event':['400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay','400 Free Relay'], 
        'Team':['University of Hawaii', 'UC San Diego', 'Brigham Young University', 'University of California, Davis', 'UC Santa Barbara', 'California State University Bakersfield', 'University of the Pacific', 'University of San Diego', 'Cal Poly', 'University of Incarnate Word'], 
        'Time':['3:16.45', '3:21.44', '3:23.43', '3:24.48', '3:25.46', '3:25.96', '3:26.67', '3:29.59', '3:30.82', '3:32.36'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22, 18, 14], 
        'Gender':['Female','Female','Female','Female','Female','Female','Female','Female','Female','Female']}
    df13 = pd.DataFrame(data=d13)

    d14 = {'Place':['1','2','3','4','5','6','7','8', '9', '10'], 
        'Name':['University of Hawaii', 'UC San Diego', 'UC Santa Barbara', 'California State University Bakersfield', 'University of California, Davis', 'University of Incarnate Word', 'University of the Pacific', 'Brigham Young University', 'Cal Poly', 'University of San Diego'], 
        'Event':['800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay','800 Free Relay'], 
        'Team':['University of Hawaii', 'UC San Diego', 'UC Santa Barbara', 'California State University Bakersfield', 'University of California, Davis', 'University of Incarnate Word', 'University of the Pacific', 'Brigham Young University', 'Cal Poly', 'University of San Diego'], 
        'Time':['7:15.43', '7:19.69', '7:25.12', '7:31.64', '7:32.47', '7:36.60', '7:37.52', '7:38.12', '7:43.14', '7:44.14'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22, 18, 14], 
        'Gender':['Female','Female','Female','Female','Female','Female','Female','Female','Female','Female']}
    df14 = pd.DataFrame(data=d14)

    d15 = {'Place':['1','2','3','4','5','6','7','8', '9', '10'], 
        'Name':['University of Hawaii', 'UC San Diego', 'Brigham Young University', 'UC Santa Barbara', 'University of California, Davis', 'California State University Bakersfield', 'University of San Diego', 'Cal Poly', 'University of the Pacific', 'University of Incarnate Word'], 
        'Event':['200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay','200 Medley Relay'], 
        'Team':['University of Hawaii', 'UC San Diego', 'Brigham Young University', 'UC Santa Barbara', 'University of California, Davis', 'California State University Bakersfield', 'University of San Diego', 'Cal Poly', 'University of the Pacific', 'University of Incarnate Word'], 
        'Time':['1:38.56', '1:38.79', '1:41.32', '1:42.07', '1:42.09', '1:42.90', '1:44.42', '1:44.81', '1:45.36', '1:45.63'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22, 18, 14], 
        'Gender':['Female','Female','Female','Female','Female','Female','Female','Female','Female','Female']}
    df15 = pd.DataFrame(data=d15)

    d16 = {'Place':['1','2','3','4','5','6','7','8', '9', '10'], 
        'Name':['University of Hawaii', 'UC San Diego', 'UC Santa Barbara', 'Brigham Young University', 'California State University Bakersfield', 'University of California, Davis', 'University of the Pacific', 'University of San Diego', 'University of Incarnate Word', 'Cal Poly'], 
        'Event':['400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay','400 Medley Relay'], 
        'Team':['University of Hawaii', 'UC San Diego', 'UC Santa Barbara', 'Brigham Young University', 'California State University Bakersfield', 'University of California, Davis', 'University of the Pacific', 'University of San Diego', 'University of Incarnate Word', 'Cal Poly'], 
        'Time':['3:36.43', '3:38.45', '3:42.29', '3:42.69', '3:44.95', '3:45.00', '3:51.99', '3:52.27', '3:53.27', '3:54.04'], 
        'Points':[40, 34, 32, 30, 28, 26, 24, 22, 18, 14], 
        'Gender':['Female','Female','Female','Female','Female','Female','Female','Female','Female','Female']}
    df16 = pd.DataFrame(data=d16)
    score_mod = pd.concat([score_mod, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16], ignore_index=True)

    # divide points if tied
    a = score_mod.duplicated(subset=['Place', 'Event', 'Gender'])
    err = a[a == True].index
    for i in err:
        score_mod.loc[i, ('Points')] = score_mod.loc[i]['Points']/2
        score_mod.loc[i-1, ('Points')] = score_mod.loc[i-1]['Points']/2

    # save to csv
    top_men = score_mod[score_mod['Gender'] == 'Male'].reset_index().drop(columns='index')
    top_women = score_mod[score_mod['Gender'] == 'Female'].reset_index().drop(columns='index')
    top_men.to_csv('MPSF_men.csv')
    top_women.to_csv('MPSF_women.csv')


    # function to score
    def score(df, gender):
        for event in df['Event'].unique():
            df[df['Event'] == event].groupby('Team')['Points'].sum().sort_values(ascending=False).to_csv(event + '_'+ gender + '_points.csv')
        return


    # scoing for men and women
    score(top_men, 'men')
    score(top_women, 'women')