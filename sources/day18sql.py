import pandas as pd
import sqlite3

#task 1
conn = sqlite3.connect("Downloads/internship.db")
df=pd.read_sql_query("SELECT interns.name AS intern_name,interns.track,mentors.mentor_name FROM interns INNER JOIN mentors ON interns.track = mentors.track;", conn)
print(df)
print("-"*90)


#task 2

df=pd.read_sql_query("SELECT * FROM interns WHERE track = 'Data Science' AND stipend > 5000;", conn)
print(df)
print("-"*90)

df=pd.read_sql_query("SELECT track, AVG(stipend) AS avg_stipend FROM interns GROUP BY track;", conn)
print(df)
print("-"*90)