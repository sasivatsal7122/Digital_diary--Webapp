from django.forms import PasswordInput
import streamlit as st
from streamlit_ace import st_ace,THEMES
import datetime

def main():
    st.markdown("<h1 align='center'>Digital Diary</h1></br></br>",unsafe_allow_html=True)
    st.subheader("Write about your day here")
    c1, c2 = st.columns([3, 1])
    c2.subheader("Parameters")
    with c1:
        user_code = st_ace(
            #language=c2.selectbox("Language mode",('python', 'java', 'c_cpp')),
            theme=c2.selectbox("Theme", options=THEMES, index=35),
            font_size=c2.slider("Font size", 5, 24, 14),
            tab_size=c2.slider("Tab size", 1, 8, 4),
            show_gutter=c2.checkbox("Show gutter", value=True),
            wrap=c2.checkbox("Wrap enabled", value=True),
            #auto_update=c2.checkbox("Auto update", value=False),
            min_lines=45,
            key="ace",
        )
    d = c2.date_input(
     "Choose date",
     datetime.datetime.now())
    s1,s2,s3 = st.columns(3)
    save_data = s2.button("Save Data")
    if save_data:
        pass
            
if __name__ == "__main__":
    main()

