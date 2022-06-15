import streamlit as st
from streamlit_option_menu import option_menu
import ckrett as ck
import database as db
import streamlit_authenticator as stauth
import sqlite3
import app_dashboard
import random
import string


def run_login():
    st.set_page_config(page_title="Digital Diary",page_icon='📚',layout="wide")
    st.title("Welcome To Digital Diary")

    st.markdown("<p><TT>Designed and Developed by <a style='text-decoration:none;color:red' target='_blank' href='https://github.com/sasivatsal7122'>B.Sasi Vatsal</a></TT></p>", unsafe_allow_html=True)

    login_type = st.sidebar.selectbox('Choose Option',
                            ('Sign-in', 'Sign-Up'))
    if login_type=='Sign-Up':
        user_option = option_menu(None, ["Sign-Up"], 
        icons=['box-arrow-in-left', 'box-arrow-in-right'], 
        menu_icon="cast", default_index=0, orientation="horizontal")

        if user_option=='Sign-Up':
            st.header("Haven't Sign up yet?")
            sign_up_username = st.text_input("What do you want your username too be ?",'eg: darkrider69')
            name = st.text_input("What is your name ?  ")
            email = st.text_input("What is your Email ?  ")
            sign_up_password = st.text_input("Enter Your Password :  ",type="password")
            sign_up_password = ck.syph(sign_up_password)
            create_acc = st.button("Create My Account")
            
            if create_acc:
                conn = sqlite3.connect('user_record.db')

                #Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                    
                cursor.execute('''SELECT USERNAME FROM USERS''')
                USERNAME_LS = cursor.fetchall()
                USERNAME_LS = [item for t in USERNAME_LS for item in t]
                
                cursor.execute('''SELECT uNAME FROM USERS''')
                NAME_LS = cursor.fetchall()
                NAME_LS = [item for t in NAME_LS for item in t]
                
                if sign_up_username not in USERNAME_LS and name not in NAME_LS:
                    random_username = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
                    db.create_newuser(random_username,name,sign_up_username,email,sign_up_password)
                    st.success(f"{sign_up_username}/{name} your account has been created successfully !")
                    st.balloons()
                else:
                    st.error("Your Account already exists, please sign in")
                
    else:
        #Connecting to sqlite
        conn = sqlite3.connect('user_record.db')

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        cursor.execute('''SELECT USERNAME FROM USERS''')
        USERNAME_LS = cursor.fetchall()
        USERNAME_LS = [item for t in USERNAME_LS for item in t]
        
        cursor.execute('''SELECT uNAME FROM USERS''')
        NAME_LS = cursor.fetchall()
        NAME_LS = [item for t in NAME_LS for item in t]
        
        cursor.execute('''SELECT USER_EMAIL FROM USERS''')
        EMAIL_LS = cursor.fetchall()
        EMAIL_LS = [item for t in EMAIL_LS for item in t]
        
        cursor.execute('''SELECT PASS_WORD FROM USERS''')
        PASSWORDS_LS = cursor.fetchall()
        PASSWORDS_LS = [ck.dsyph(item) for t in PASSWORDS_LS for item in t]
        
        
        hashed_passwords = stauth.Hasher(PASSWORDS_LS).generate()
        
        authenticator = stauth.Authenticate(NAME_LS,USERNAME_LS,hashed_passwords,
            'QUEEENELIZEBETH','satyasasivatsal',cookie_expiry_days=5)
        
        name, authentication_status, username = authenticator.login('Login','main')
        
        if authentication_status:
            authenticator.logout('Logout', 'sidebar')
            app_dashboard.main(username,name)
            
        elif authentication_status == False:
            st.error('Username/password is incorrect')
            
    
        elif authentication_status == None:
            st.warning('Please enter your username and password')