from matplotlib.style import reload_library
import streamlit as st
from streamlit_ace import st_ace,THEMES
import datetime
from datetime import timedelta

from sympy import use
import database as db
from datetime import date

from streamlit_option_menu import option_menu

st.set_page_config(page_title="Digital Diary",page_icon='📚',layout="wide")

st.markdown("<h1 align='center'>Welcome Digital Diary</h1><br><br>", unsafe_allow_html=True)
user_option = option_menu(None, ["Write MY Diary", "Read My Diary"], 
icons=['box-arrow-in-left', 'box-arrow-in-right'], 
menu_icon="cast", default_index=0, orientation="horizontal")
st.markdown("<br><br>", unsafe_allow_html=True)

def read():
    st.subheader("Read Your Previous data")
    c1, c2 = st.columns([3, 1])
    c2.subheader("Parameters")
   
    today = date.today()
    Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
    Previous_Date_Formatted = Previous_Date.strftime ('%Y/%m/%d')
    
    user_input_date = c2.date_input(
     "Choose date",
     Previous_Date)
    
    reload_btn = c2.button("Show Data")
    if reload_btn:
    
        d = user_input_date.strftime('%Y-%m-%d')
        with open('tempinfo.txt') as f:
                x = f.read()
        
        userkey = str(x)+str(d)
        user_record_post = db.get_user_post(userkey)
        
        try: 
            
            with c1:
                user_post = st_ace(
                    value=f"{user_record_post[0]}", 
                    language='plain_text',
                    theme=c2.selectbox("Theme", options=THEMES, index=35),
                    font_size=c2.slider("Font size", 5, 24, 14),
                    tab_size=c2.slider("Tab size", 1, 8, 4),
                    show_gutter=c2.checkbox("Show gutter", value=True),
                    wrap=c2.checkbox("Wrap enabled", value=True),
                    readonly=False,
                    min_lines=30,
                    key="ace",
                    max_lines=None, 
                    show_print_margin=False, 
                    annotations=None, 
                )
            c2.info("You can edit your data in write section by jumping to the date you want to edit")

        except:
            pass
            with c1:
                user_post = st_ace(
                    value="You Dont Have any Record on this Date", 
                    language='plain_text',
                    theme=c2.selectbox("Theme", options=THEMES, index=35),
                    font_size=c2.slider("Font size", 5, 24, 14),
                    tab_size=c2.slider("Tab size", 1, 8, 4),
                    show_gutter=c2.checkbox("Show gutter", value=True),
                    wrap=c2.checkbox("Wrap enabled", value=True),
                    readonly=False,
                    min_lines=30,
                    key="ace",
                    max_lines=None, 
                    show_print_margin=False, 
                    annotations=None, 
                )

        
def write():
    st.subheader("Write about your day here")
    c1, c2 = st.columns([3, 1])
    c2.subheader("Parameters")
    today = date.today()
    current_date = today.strftime('%B %d, %Y')
    d = c2.date_input(
     "Choose date",
     datetime.datetime.now())
    save_data = st.button("Save Data")
    with c1:
        user_post = st_ace(
            value=f"Date: {current_date}", 
            placeholder='Start writing here',
            language='plain_text',
            theme=c2.selectbox("Theme", options=THEMES, index=35),
            font_size=c2.slider("Font size", 5, 24, 14),
            tab_size=c2.slider("Tab size", 1, 8, 4),
            show_gutter=c2.checkbox("Show gutter", value=True),
            wrap=c2.checkbox("Wrap enabled", value=True),
            readonly=False,
            min_lines=30,
            key="ace",
            max_lines=None, 
            show_print_margin=False, 
            annotations=None, 
        )
    
    if save_data:
        with open('tempinfo.txt') as f:
            x = f.read()
        userkey = str(x)+str(d)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        db.create_newpost(userkey,user_post,d,current_time)           
        st.success("Data Saved Successfully")
            
if user_option=='Write MY Diary':
    write()
else:
    read()

