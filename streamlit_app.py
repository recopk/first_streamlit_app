import streamlit
streamlit.title('🥣 My parents new healthy menu')
streamlit.header('🍞 Breakfast Menu')
streamlit.text('🥑 Omega 3 & Oatmeal')
streamlit.text('🐔 hard boiled free range egg')
streamlit.text('🥗 best healthy drinks made with yougurt')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
# lets put a pick list
streamlit.multiselect('Pick a list:',list(my_fruit_list))
