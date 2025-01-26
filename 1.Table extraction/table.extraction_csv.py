import pandas as pd
#Read all the tables from this website using read_html // use lxml to take this function work

simpson = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes")
#print(simpson[2])

#Read the csv files from this webstie  https://football-data.co.uk/englandm.php
#Read csvn file from the website https://football-data.co.uk/mmz4281/2122/E0.csv

df_premier = pd.read_csv("https://football-data.co.uk/mmz4281/2122/E0.csv")
print(df_premier)

#rename column

df_premier.rename(columns={"FTHG" : "Test" , 
                           "FTAG" : "Test2"} , inplace=True)

print(df_premier)