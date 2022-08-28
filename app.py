import streamlit as st
import pandas as pd
import pickle
import sklearn
teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']
st.title("IPL MATCH PREDICTION")
pipe=pickle.load(open("iplprediction.pkl","rb"))
col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox("Select the batting team",teams)
with col2:
    bowling_team=st.selectbox("select the bowling team",teams)
city=st.selectbox("select the city",cities)
col3,col4=st.columns(2)
with col3:
    target=st.number_input("Target")
with col4:
    score=st.number_input("Score")
col5,col6=st.columns(2)
with col5:
    overs=st.number_input("overs completed")
with col6:
    wickets=st.number_input("wickets fall")
if st.button("predict Probabibilty"):
    runs_left=target-score
    balls_left=120-(overs*6)
    wickets_left=10-wickets
    crr=score/overs
    rrr=(runs_left*6)/balls_left
    predict=pipe.predict_proba(pd.DataFrame([[batting_team,bowling_team,city,runs_left,balls_left,wickets_left,target,crr,rrr]],columns=["batting_team","bowling_team","city","runs_left","balls_left","wik_left","total_runs_x","currate","runrate"]))
    st.text("Match win by "+bowling_team+" is "+str(predict[0][0]))
    st.text("Match win by "+batting_team+" is "+ str(predict[0][1]))
