from urllib.error import URLerror
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

streamlit.header("Fruityvice Fruit Advice!")
try:
      fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
      if not fruit_choice:
          streamlit.error('please select a fruit to get info about')
      else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
streamlit.write('The user entered ', fruit_choice)
add_my_fruit = streamlit.text_input('What fruit would you like add?','Jackfruit')
streamlit.write('The user entered ', add_my_fruit)
#import requests

#streamlit.text(fruityvice_response.json())
# improves the text 

# data output

streamlit.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
