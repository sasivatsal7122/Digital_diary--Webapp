import streamlit as st
from streamlit_ace import st_ace,THEMES
import datetime
import database as db

from streamlit_option_menu import option_menu

st.set_page_config(page_title="Digital Diary",page_icon='📚',layout="wide")

st.markdown("<h1 align='center'>Welcome Digital Diary</h1><br><br>", unsafe_allow_html=True)
user_option = option_menu(None, ["Write MY Diary", "Read My Diary"], 
icons=['box-arrow-in-left', 'box-arrow-in-right'], 
menu_icon="cast", default_index=0, orientation="horizontal")
st.markdown("<br><br>", unsafe_allow_html=True)


def read():
    pass

def write():
    st.subheader("Write about your day here")
    c1, c2 = st.columns([3, 1])
    c2.subheader("Parameters")
    with c1:
        user_post = st_ace(
            value='', 
            placeholder='Start writing here',
            language='plain_text',
            theme=c2.selectbox("Theme", options=THEMES, index=35),
            font_size=c2.slider("Font size", 5, 24, 14),
            tab_size=c2.slider("Tab size", 1, 8, 4),
            show_gutter=c2.checkbox("Show gutter", value=True),
            wrap=c2.checkbox("Wrap enabled", value=True),
            readonly=False,
            min_lines=30,
            key="ace"
        )
    d = c2.date_input(
     "Choose date",
     datetime.datetime.now())
    s1,s2,s3 = st.columns(3)
    save_data = s2.button("Save Data")
    if save_data:
        with open('tempinfo.txt') as f:
            x = f.read()
        userkey = str(x)+str(d)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        db.create_newpost(userkey,user_post,d,current_time)           
        st.success("Data Saved Successfully")
            
if __name__ == "__main__":
    write()

