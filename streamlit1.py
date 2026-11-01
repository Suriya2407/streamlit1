import streamlit as st
#st.title("WELCOME TO MY WORLD")
#st.header("This is my second project")
#st.write("this is my streamlit project")
#st.markdown("What is your name?")
#st.caption("This is yours_bro")
import pandas as pd
import pandas as pd
from PIL import Image
st.title("INDIAN PREMIER LEAGUE")
mg=Image.open(r"c:\Users\gjaya\Downloads\ipl image.png")
st.image(mg,caption="IPLT20")
if st.checkbox("KINDLY VERIFY"):
    st.success("YOU ARE VERIFIED")
with st.expander("Welcome"):
    st.write("SIMPLE IDEA ABOUT THE IPL")
st.write("DOMINATING TEAMS IN THE IPL")
import pandas as pd
import pandas as pd
from PIL import Image
new_data={"TEAMS":["CSK","MI","KKR","RCB"],"CUPS HOLDED":[5,5,3,2]}
new_one=pd.DataFrame(new_data)
st.write(new_one)
data = {
    "Year": [
        2008, 2009, 2010, 2011, 2012, 2013,
        2014, 2015, 2016, 2017, 2018, 2019,
        2020, 2021, 2022, 2023, 2024, 2025, 2026
    ],

    "Winner": [
        "🏆 Rajasthan Royals",
        "🏆 Deccan Chargers",
        "🏆 Chennai Super Kings",
        "🏆 Chennai Super Kings",
        "🏆 Kolkata Knight Riders",
        "🏆 Mumbai Indians",
        "🏆 Kolkata Knight Riders",
        "🏆 Mumbai Indians",
        "🏆 Sunrisers Hyderabad",
        "🏆 Mumbai Indians",
        "🏆 Chennai Super Kings",
        "🏆 Mumbai Indians",
        "🏆 Mumbai Indians",
        "🏆 Chennai Super Kings",
        "🏆 Gujarat Titans",
        "🏆 Chennai Super Kings",
        "🏆 Kolkata Knight Riders",
        "🏆 Royal Challengers Bengaluru",
        "🏆 Royal Challengers Bengaluru"
    ],

    "Runner-Up": [
        "🦁 Chennai Super Kings",
        "🔴 Royal Challengers Bangalore",
        "🔵 Mumbai Indians",
        "🔴 Royal Challengers Bangalore",
        "🏆 Chennai Super Kings",
        "🦁 Chennai Super Kings",
        "🦁 Kings XI Punjab",
        "🦁 Chennai Super Kings",
        "🔴 Royal Challengers Bangalore",
        "🟣 Rising Pune Supergiant",
        "🟠 Sunrisers Hyderabad",
        "🦁 Chennai Super Kings",
        "🔵 Delhi Capitals",
        "🟣 Kolkata Knight Riders",
        "🩷 Rajasthan Royals",
        "🔵 Gujarat Titans",
        "🟠 Sunrisers Hyderabad",
        "🔴 Punjab Kings",
        "🔵 Gujarat Titans"
    ],

    "Margin of Victory": [
        "3 wickets", "6 runs", "22 runs", "58 runs",
        "5 wickets", "23 runs", "3 wickets", "41 runs",
        "8 runs", "1 run", "8 wickets", "1 run",
        "5 wickets", "27 runs", "7 wickets", "5 wickets",
        "8 wickets", "6 runs", "5 wickets"
    ]
}

df = pd.DataFrame(data)

st.write(df)
name=st.text_input("enter your captain").upper()
st.text("hints: ONLY NICK_NAMES FOR THE GOATED 3 CAPTAINS ")
if name=="THALA".upper():
    st.success("GOATED CAPTAIN🦁👑🏏💥")
if name=="KING".upper():
    st.success("HE IS THE RUN MACHINE🏏💥")
if name=="HITMAN".upper():
    st.success("HE IS UNBEATEN👑🏏💥 ")

runs=st.slider(150,287)
if runs==49:
    st.write("THIS IS THE LOWEST TOTAL IN THE IPL")
if runs==287:
    st.write("THIS IS THE HIGHEST TOTAL IN THE IPL")   
box=st.selectbox("CHOOSE YOUR TEAM",["CSK","RCB","MI","RR","KKR","GT","KXIP","SRH","DC","LSG"])
st.write("your selected team is",box)
ch=st.radio("YOUR FAVOURITE AMONG THESE FOUR",["RCB","CSK","MI","SRH"])
st.write("your favourite one is",ch)
st.write("2026 CHAMPIONS")
st.video(r"D:\streamlit tutorial\video\RCB_2026.mp4")
st.sidebar.title("INDIAN PREMIER LEAGUE")
st.sidebar.write("THE 2026 CHAMPIONS")
image2=st.sidebar.image(r"c:\Users\gjaya\Downloads\rcb.jpg")
#UP=st.file_uploader("Upload only the csv file",type=['CSV'])

#import time
#my_bar=st.progress(0)
#for i in range(100):
    #time.sleep(0.3)
    #my_bar.progress(i+1)
if st.button("Click this"):
    st.text("The captains")
    st.image(r"C:\Users\gjaya\Downloads\captains.jpg") 


