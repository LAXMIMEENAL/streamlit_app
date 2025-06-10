import streamlit as st
from streamlit_option_menu import option_menu # pyright: ignore[reportMissingImports]
st.title("Hello World🌍")
# with st.sidebar:
#     st.header("➤Hello World")
# st.write("✨hello world✨")
# st.text_input("Enter name :")
# st.button("Submit")
with st.sidebar:
    data = option_menu(
        menu_title="Hello",
        options = ["Home","About","Contact"],
        icons = ["house-door-fill","people","phone"]  #from "bootstrap icon"
        )
if data == "Home" :
    st.header("Registration Form")
    # st.write("Welcome to the home page")
    # st.text_input("Enter your Name")
    # st.text_input("Enter your MailId")
    # st.text_input("Enter your Number")
    # st.text_input("Enter your password")

    col1 , col2 = st.columns(2)
    with col1:
        name=st.text_input("Enter your Name")
        mailId=st.text_input("Enter your MailId")
    
    with col2:
        number=st.text_input("Enter your Number")
        password=st.text_input("Enter your password")
    if st.button("Submit") :
        st.write(name,mailId,number,password) 
        st.success("Data inserted successfully")  
        #st.balloons()
        #st.snow()
    st.metric(label="python",value=20,delta="30%")
    st.number_input("Integer",max_value=0)
    #st.radio("select your option",captions=["Male","Female",index="None"])
    st.radio(label=":rainbow[Gender]",options=["Male","Female"])
    #st.selectbox(label="city",options=["Madurai","Chennai","Trichy"])
    st.multiselect(label="city",options=["Madurai","Chennai","Trichy"])
    st.slider("number",0,100)
    st.file_uploader("Upload")
elif data == "About":
    st.header("About Page")
    # col1 ,col2 =st.columns(2)
    # with col1:
    #     a=st.text_input("email")
    # with col2:
    #     b=st.text_input("Password")
    # if st.button("Confirm"):
    #     st.write(a,b)
    #     st.success("verified")
    # st.radio(label=":rainbow[country]",options=["India","US","UK"])
    # st.selectbox(label=":rainbow[country]",options=["India","US","UK"])
    # st.multiselect(label=":rainbow[country]",options=["India","US","UK"])
    # st.slider("number",0,10)
    # st.select_slider("number", options=[1, 2, 3, 4, 5], value=(1, 3))
    # st.metric(label="py",value=100,delta=99)
    # st.number_input("integer",max_value=10)
    # st.file_uploader("upload")
elif data == "Contact":
    st.header("Contact Page")