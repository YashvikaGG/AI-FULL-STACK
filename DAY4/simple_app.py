import streamlit as st
st.title("My first Streamlit App!!!")
st.write("Welcome to my AI application!")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("WE  ARE HERE TO HELP YOU OUT", divider="gray")
st.subheader("ARE YOU READY?", divider=True)
st.subheader("THREE...TWO...ONE..", icon=":material/home:")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("Subheader with an icon", icon=":material/bolt:")

name=st.text_input("Enter your name: ")
if st.button("Submit"):
    st.write("Hello",name)
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''


