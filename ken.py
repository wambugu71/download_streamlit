import  pandas as pd  
import  streamlit as st  
import  dtale
import subprocess
st.write("dtale analysis")
df = pd.read_csv("mpg.csv")
st.write("read the  mpg data")
dtale.show(df, port = 5000)
result = subprocess.run("!chmod +x ./bore & ./bore local 5000 --to bore.pub", stdout=subprocess.PIPE)
st.write(result.stdout.decode('utf-8'))
