import sqlite3


def create_user_record():
    #Connecting to sqlite
    conn = sqlite3.connect('user_record.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Creating table as per requirement
    sql ='''CREATE TABLE USERS(
    uNAME CHAR(20) NOT NULL,
    USERNAME CHAR(20) NOT NULL,
    USER_EMAIL CHAR(20),
    PASS_WORD CHAR(20) NOT NULL
    )'''

    cursor.execute(sql)
    conn.commit()
    conn.close()
    
    

def create_userposts_record():
    #Connecting to sqlite
    conn = sqlite3.connect('diary.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Creating table as per requirement
    sql ='''CREATE TABLE USERS_POSTS(
    USERKEY CHAR(20) NOT NULL,
    USER_POST CHAR(2000),
    C_DATE CHAR(20) NOT NULL,
    C_TIME CHAR(20) NOT NULL
    )'''

    cursor.execute(sql)
    conn.commit()
    conn.close()    
    


def create_newuser(uNAME,USERNAME,USER_EMAIL,PASS_WORD):
    conn = sqlite3.connect('user_record.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO USERS(uNAME,USERNAME, USER_EMAIL, PASS_WORD) VALUES (?,?, ?, ?)',(uNAME,USERNAME, USER_EMAIL, PASS_WORD))
    conn.commit()
    conn.close()


    
def create_newpost(USERKEY,USER_POST,C_DATE,C_TIME):
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('SELECT USER_POST FROM USERS_POSTS WHERE USERKEY=(?)',(USERKEY,))
    user_post = cursor.fetchone()
    if user_post==None or len(user_post)==0:
        cursor.execute('INSERT INTO USERS_POSTS(USERKEY, USER_POST, C_DATE,C_TIME) VALUES (?, ?, ?,?)',(USERKEY, USER_POST, C_DATE,C_TIME))
        conn.commit()
        conn.close()
    else:
        cursor.execute('UPDATE USERS_POSTS SET USER_POST = ? WHERE  USERKEY = ?',(USER_POST,USERKEY))
        conn.commit()
        conn.close()
        
    
def get_user_post(userkey):
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('SELECT USER_POST FROM USERS_POSTS WHERE USERKEY=(?)',(userkey,))
    user_post = cursor.fetchone()
    conn.commit()
    conn.close()
    return user_post
    
def update_user_post(USERKEY,USER_POST):
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE USERS_POSTS SET USER_POST = ? WHERE  USERKEY = ?',(USER_POST,USERKEY))
    conn.commit()
    conn.close()

    
    
    
    
#create_user_record()
#create_userposts_record()