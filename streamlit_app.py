import streamlit
streamlit.title('🥣 My parents new healthy menu')
streamlit.header('🍞 Breakfast Menu')
streamlit.text('🥑 Omega 3 & Oatmeal')
streamlit.text('🐔 hard boiled free range egg')
streamlit.text('🥗 best healthy drinks made with yougurt')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#intro requests section calling API calls
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?',fruit_choice)
streamlit.write('The user entered ', fruit_choice)
# improves the text 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# data output
streamlit.dataframe(fruityvice_normalized)

