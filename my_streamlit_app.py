import pandas as pd
import seaborn as sns
import streamlit as st

st.title('Hello Wilders, welcome to my application!')

st.write("Enjoy the life!")

country = st.text_input("Please give me your country:")
country_length = len(country)
st.write("Do you know that their is ",country_length,"characters in ", country)

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_car = pd.read_csv(link)


country_choice = st.sidebar.selectbox(
    "Which continent?",
    (" ","Europe", "Japan", "US"))

st.title('Here is the database of car sold in ')

# st.radio(label, options, index=0, format_func=special_internal_function, 
# 	key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, 
# 	horizontal=False, captions=None, label_visibility="visible")

# Here we use "magic commands":
df_car[df_car['continent'].str.contains(country_choice)]



import seaborn as sns
import matplotlib.pyplot as plt
# Figure 
viz_correlation = sns.heatmap(df_car.drop(columns = ['continent']).corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

# Graphique
st.set_option('deprecation.showPyplotGlobalUse', False)
fig, ax = plt.subplots()
ax.scatter(x=df_car[df_car['continent'].str.contains(country_choice)]['year'],
	 y=df_car[df_car['continent'].str.contains(country_choice)]['mpg'])
plt.xlabel('Année')
plt.ylabel('Miles per Gallon (MPG)')
plt.title('MPG par année')
st.pyplot()


# Pour afficher le lien vers l'API (ou executer l'API)
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\virtual_env\Scripts\activate
# streamlit run my_streamlit_app.py
