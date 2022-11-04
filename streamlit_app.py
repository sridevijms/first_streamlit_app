
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


def get_fruity_vice_date(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return (fruityvice_normalized)


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
my_fruit_list = my_fruit_list.set_index('Fruit')

# streamlit.multiselect("Pick some fruits New :", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected=streamlit.multiselect("Pick some fruits New :", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error('The user entered . Please select')
    else:
        # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        # # streamlit.write('The user entered ', fruit_choice)
        # # streamlit.text(fruityvice_response.json())
        # # write your own comment -what does the next line do?
        # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        # write your own comment - what does this do?
        backfromfunction=get_fruity_vice_date(fruit_choice)
        streamlit.dataframe(backfromfunction)
except URLError as e:
    streamlit.error()


# streamlit.stop()
#
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
#
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# streamlit.text("fruit_load_list:")
# streamlit.text(my_data_row)
#
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# streamlit.text("fruit_load_list in datagrame:")
# streamlit.dataframe(my_data_row)
#
#
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_rowa = my_cur.fetchall()
# streamlit.text("fruit_load_list in my_data_rowa:")
# streamlit.dataframe(my_data_rowa)


# add_my_fruit = streamlit.text_input('Testing frouts?','Kiwi')
# streamlit.write('Thanks for adding ', add_my_fruit)
#
# my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")

def get_fruite_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()

if streamlit.button('Get the fruit to load'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruite_load_list()
    streamlit.dataframe(my_data_rows)


def add_fruite_load_list(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
        return "thanks for adding "+new_fruit

add_my_fruit = streamlit.text_input('Testing frouts?')

if streamlit.button('Add the fruit to load'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=add_fruite_load_list(add_my_fruit)
    streamlit.text("Back from func"+my_data_rows)
