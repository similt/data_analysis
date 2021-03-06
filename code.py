import pandas as pd
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")
star_wars.columns
#Remove any rows where RespondentID is NaN
star_wars.dropna(subset = ["RespondentID"], inplace=True)
print(star_wars.shape)
star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].value_counts()
star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].value_counts(dropna=False)
def yesno(c): 
    if c=="Yes": 
        return True 
    elif c=="No": 
        return False 
star_wars["Have you seen any of the 6 films in the Star Wars franchise?"]=star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].apply(yesno)
star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"]=star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].apply(yesno)
clist=['Which of the following Star Wars films have you seen? Please select all that apply.','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8']
for c in clist:
    print(star_wars[c].value_counts(dropna=False))
#rename the columns 
star_wars.columns[3:9]
clist=['Which of the following Star Wars films have you seen? Please select all that apply.','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8']
nlist=['seen_1','seen_2','seen_3','seen_4','seen_5','seen_6']
print(type(nlist[0]))
for c in range(len(clist)):
    star_wars.rename(columns={clist[c]:nlist[c]},inplace=True)
import numpy as np
def yesnan(c): 
    if pd.isnull(c): 
        return False 
    else:
        return True 
#If the value is NaN, the respondent either didn't answer or didn't see the movie. We'll assume that they didn't see the movie.
for c in star_wars.columns[3:9]:
    star_wars[c]=star_wars[c].apply(yesnan)
 star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
 rlist=['Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14']
qlist=['ranking_1','ranking_2','ranking_3','ranking_4','ranking_5','ranking_6']
for c in range(len(rlist)):
    star_wars.rename(columns={rlist[c]:qlist[c]},inplace=True)
 
x=star_wars.columns[9:15]
m1=[]
for i in star_wars.columns[9:15]: 
    m1.append(star_wars[i].mean())
print(m1)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(x,m1,color='y')

seen=[]
lab=[]
for i in nlist: 
    #print(star_wars[i].notnull().sum())
    seen.append(star_wars[i].sum())
    lab.append(i)
fig, ax = plt.subplots()
ax.bar(lab,seen,color='y')
print(seen)

males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]


mseen=[]
for i in nlist: 
    #print(star_wars[i].notnull().sum())
    mseen.append(males[i].sum())
fig, ax = plt.subplots()
ax.bar(lab,mseen,color='y')
print(mseen)
fseen=[]
for i in nlist: 
    #print(star_wars[i].notnull().sum())
    fseen.append(females[i].sum())
fig, ax = plt.subplots()
ax.bar(lab,fseen,color='y')
print(fseen)

mrat=[]
for i in star_wars.columns[9:15]: 
    mrat.append(males[i].mean())
print(mrat)
fig, ax = plt.subplots()
ax.bar(x,mrat,color='y')

frat=[]
for i in star_wars.columns[9:15]: 
    frat.append(females[i].mean())
print(mrat)
fig, ax = plt.subplots()
ax.bar(x,frat,color='y')
