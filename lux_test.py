import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import pandas as pd
import lux
st.set_page_config(layout = "wide")
with st.sidebar:
    files = st.file_uploader("Upload data", type =["csv"])
if  files !=None:
    @st.cache_data(show_spinner = False)
    def app():
        st.title('Analysis of Happy Planet Index Dataset')
        st.write('Check out these cool visualizations!')
        df = pd.read_csv(files)#df = pd.read_csv("https://raw.githubusercontent.com/lux-org/lux-datasets/master/data/hpi.csv")
        export_file = 'visualizations.html'
        html_content = df.save_as_html(output=True)
        #st.write(html_content)
        components.html(html_content,  height=320)

    app()