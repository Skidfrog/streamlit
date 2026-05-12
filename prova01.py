import streamlit as st
import pandas as pd
import matplotlib as plt
import mysql.connector
from mysql.connector import Error

st.title("hello world")

connection_config_dict = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'sprint4',
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
    }
connection = mysql.connector.connect(**connection_config_dict)


pedidos = pd.read_sql('select * from users', connection )

plt.plot(pedidos)
