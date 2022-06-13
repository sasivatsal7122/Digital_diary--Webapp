import streamlit as st
import streamlit_authenticator as stauth
import sqlite3


def user_login():
    #Connecting to sqlite
    conn = sqlite3.connect('user_record.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    USERNAME_LS = cursor.execute('''SELECT USERNAME FROM USERS''')
    NAME_LS = cursor.execute('''SELECT UNAME FROM USERS''')
    EMAIL_LS = cursor.execute('''SELECT USER_EMAIL FROM USERS''')
    PASSWORDS_LS = cursor.execute('''SELECT PASS_WORD FROM USERS''')

    authenticator = stauth.Authenticate(NAME_LS,USERNAME_LS,PASSWORDS_LS,
        'QUEEENELIZEBETH','sasivatsal',cookie_expiry_days=5)
    
    name, authentication_status, username = authenticator.login('Login','main')
    
    if authentication_status:
        authenticator.logout('Logout', 'main')
        
    elif authentication_status == False:
        st.error('Username/password is incorrect')
   
    elif authentication_status == None:
        st.warning('Please enter your username and password')

