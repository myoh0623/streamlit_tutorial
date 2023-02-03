# <pythonfile>.ipynb notebook
# 프로그램 작성시에는 <pythonfile>.py
# python3 <pythonfile>.py
# streamlit run <streamlitapp>.py 

import streamlit as st
import pandas as pd
import numpy as np
# pip install pandas
# conda install pandas

def text():
    #Mark Down
    st.markdown('Markdown')
    st.markdown('Streamlit is **_really_ cool**.')
    st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
    st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

def dataframe1():
    df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))
    st.dataframe(df) # Same as st.write(df)

def temp_map():
    # 온도 출력
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    # 위도 경도에 맞는 지도를 출력
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.map(df)


def main():
    st.title("First_APP")

    st.sidebar.write('''
    # lab1
    # lab2
    - lab3
    - lab4
    ''')

    df = pd.DataFrame({
        "first_col":[1, 2, 3, 4],
        "second_col":[10, 20, 30, 40]
    })
    st.write(df)

    text()

    if st.checkbox("show dataframe"):
        dataframe1()

    temp_map()

if __name__ == "__main__":
    main()

