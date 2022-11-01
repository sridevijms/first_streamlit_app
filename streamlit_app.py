
import streamlit;
import pandas

streamlit.title("my Test page in streamlit")
streamlit.header("my Test page in header")
streamlit.subheader("my Test page in subheader")
streamlit.text("my Test page in text1")
streamlit.text("my Test page in text2")

streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑Hard-Boiled Free-Range Egg')
streamlit.text('   🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

