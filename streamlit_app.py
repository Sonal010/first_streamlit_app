import streamlit
streamlit.title('Hi How are you')
streamlit.title('Hey')
streamlit.header('menu')
streamlit.text('1,2,3')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
