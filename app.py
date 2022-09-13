#import-----
from enum import auto
from pickletools import markobject
import tkinter
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

#Assests----
img = Image.open(r'Depression-bro (2).png')
img1 = Image.open(r'Depression-rafiki.png')
attribute = "People illustrations by Storyset"

#page styling-----
st.set_page_config(page_title= " 📊 Survey",
                    layout='wide')
# def local_css(filename):
#     with open(filename) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# local_css("style/style.css")

#Heading-----
st.title("Suicides in India (2000 to 2020)")
#Body---
with st.container():
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("""Suicide is a miserable act that takes the life of an individual. It is a tragedy that affects the members of their family, their friends and community. 
        People of any age and gender can be at a risk of suicide. Stressful life events (including financial crisis, harrassment, bullying etc.), mental disorders
        (including anxiety, depression), physical disorder are the various causes of suicide. Those who had direct or indirect exposure to family violence, abuse, suicidal behaviour, drug addiction
        or had previously attempted suicide are at high risk of attempting suicides.""")
        st.markdown("###")
        st.markdown("###")
        st.markdown("""
        In India, every year more than 1,00,000 people ends their own life by commiting suicide. The major method of suicide was hanging and consuming poisoning. The data used in this survey provides the overview
        from the year 2000 to 2020 for all the States & UT in India.""")
        st.markdown("###")
        st.markdown("###")
        st.markdown("""
        Dataset: (https://www.kaggle.com/datasets/allwynthomas2410/suicides-in-india-from-year-2000-to-2020)
        
        """)


    with right_column:
        st.image(img1,
        caption=attribute,
        use_column_width="always",
        width=400
        
)


# Load Dataframe

excel_file = "SuicideIndiaData.xlsx"
sheet_name = "Sheet1"

df = pd.read_excel(excel_file,
                    sheet_name= sheet_name,
                    engine='openpyxl',
                    usecols= "B:E",
                    header=0,
                    )

df_AgeVsDeath = pd.read_excel(excel_file,
                    sheet_name= sheet_name,
                    usecols= "G:H",
                    header=0)

df_YearVsDeath = pd.read_excel(excel_file,
                    sheet_name= sheet_name,
                    usecols= "W:X",
                    header=0,
                    
)

df_ContributingFactors = pd.read_excel(excel_file,
                    sheet_name= sheet_name,
                    usecols= "S:T",
                    header=0,
                    nrows=17,)

#Year Vs. Death

st.title("A total of 1,53,052 suicides cases were reported in the year of 2020.")
st.markdown("""This points an increase of 41% in comparison to the year of 2000. """)
st.line_chart(df_YearVsDeath,
                x="Year",
                y="Total_No_of_Suicides",
                use_container_width=True,
                
    )
st.markdown("###")
with st.container():
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("According to WHO, Suicide was the fourth leading cause of death among 15-29 year-olds globally in 2019.")
        st.markdown("""
        The age group (18 - below 30 years) and  (30 years -below 45 years) of age were the most vulnerable groups who commited to suicides, 
        accounted for 34.4% and 31.4% suicides respectively. """)


    with right_column:
        pie_chart_AD = px.pie(df_AgeVsDeath,
                        values="No . Of Deaths",
                        names="Age Group",
                        color_discrete_sequence=px.colors.sequential.RdBu
                        )
        
        st.plotly_chart(pie_chart_AD)

st.markdown("###")

#sidebar #Cause Of Death vs Total no of death
# st.sidebar.header('Search by filter: ')
#filter search
st.title("""Maharastra, Tamil Nadu, Madhya Pradesh, West Bengal and Karnataka - These 5 states together accounted for 50.4% of the total suicides reported in the country.""")
st.markdown("""Delhi reported the highest number of suicides among UTs, followed by Puducherry.""")
State = st.multiselect(
                            'Select the State / UT: ',
                            options=df["State_UT"].unique(),
                            default=df["State_UT"].unique()
)
Cause = st.multiselect(
                            'Select the cause: ',
                            options=df["Cause_Of_Suicide"].unique(),
                            default=df["Cause_Of_Suicide"].unique()
)
Category = st.multiselect(
                            'Select the category: ',
                            options=df["Category"].unique(),
                            default=df["Category"].unique()
)
df_selection = df.query(
    "State_UT == @State & Cause_Of_Suicide == @Cause & Category == @Category"
)



st.dataframe(df_selection)

st.header("###")
deaths_by_cause = (
    df.groupby(by=["Cause_Of_Suicide"]).sum()[["No_of_Deaths"]].sort_values(by="No_of_Deaths")
)

fig_deaths_by_cause = px.bar(
                    deaths_by_cause,
                    x="No_of_Deaths",
                    y=deaths_by_cause.index,
                    #title="<br>Cause Of Death vs. Total No Of Death</br>",
                    color_discrete_sequence=["#0083B8"] * len(deaths_by_cause),
                    template="plotly_white",
)

fig_deaths_by_cause.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)



st.title("""As reported by National Crime Records Bureau, The overall male : female ratio of suicide victims for the year 2021 was 72.5 : 27.4.""")
with st.container():    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("###")
        st.markdown("###")
        st.markdown("""
        which is more as compared to year 2020 (70.9: 29.1). The leading methods of adopting suicide were "Hanging"(57.0%) and "Consuming Poision"(25.1%). 
        The number of male victims were more than females in all means of suicide except those who committed suicides by ‘Fire/Selfimmolation’ where share of female victims was
more.
        """)
    with right_column:
        st.plotly_chart(fig_deaths_by_cause)
st.markdown("###")


#Contributing factors

with st.container():
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("‘Family Problems’(32%) and ‘Illness’(17%) were the major causes of suicides respectively during 2021.")
        st.markdown("""
                    Drug Abuse/ alcohol addiction, marraiage related issues, love affairs, bankruptcy or indebtedness, failure in examination,
                    unemplyoment were the other causes of suicide.
                    According National Crime Records Bureau, 'Family Problems'(3,233),‘Love Affairs’ (1,495) and ‘Illness’
                    (1,408) were the main causes of suicides among children (below 18 years of age).
                    """)
    with right_column:
        st.table(df_ContributingFactors)
st.markdown("###")




#footer
st.markdown("###")
st.markdown("###")
st.markdown("###")
st.markdown("###")
st.title("Suicide is NOT the answer")
with st.container():    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("###")
        st.markdown("###")
        st.markdown("""Sometimes, it may seems like the life has become a mess. The harassment, bullies cut a deep wound, results in feeling empty from inside. 
        The fear, abuse, violence stucks in your brain, makes you suffocate. You may feel alone even standing in a crowd. But commiting suicide will not give you relief.
        """)
        st.markdown("###")
        st.markdown("###")
        st.markdown("""In days when you feel down, you may try to talk to your friends. If someone has commited crime against you, try to speak up and ask for help. Here are the list
        of helpline number: (https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines). 
        """)
        st.title("Remember, You are not Alone. ")
        
    with right_column:
        st.image(img,
        caption=attribute,
        width=370

        )





