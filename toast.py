import streamlit as st
import time

if st.button('Lets cook it'):
    st.toast('find the egg',icon='🥚')
    time.sleep(.5)
    st.toast('fry it', icon='🍳')
    time.sleep(.5)
    st.toast('ENJOY THE MEAL!', icon='😋')