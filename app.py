import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


def main():
    st.title("Ml Exercise")
    path1= "https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv"
    df1 =pd.read_csv(path1)
    st.dataframe(df1)
    st.dataframe(df1.corr())

    fig = plt.figure(figsize=(10,8))
    sns.heatmap(df1.corr(), annot=True)
    

    




if __name__=="__main__":
    main()