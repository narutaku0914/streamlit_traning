import streamlit as st
import pandas as pd

# Import for API calls
import requests

# Import for navbar
from streamlit_option_menu import option_menu

# Import for dynamic tagging
from streamlit_tags import st_tags, st_tags_sidebar

# Imports for aggrid
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode

# Import for loading interactive keyboard shortcuts into the app
# from dashboard_utils.gui import keyboard_to_url
# from dashboard_utils.gui import load_keyboard_class

st.set_page_config( page_title="Zero-Shot Text Classifier", page_icon="🤗")

# st.image("logo.png", width=350)
st.title("Zero-Shot Text Classifier")

with st.sidebar:
    selected = option_menu(
        "",
        ["Demo", "Unlocked Mode"],
        icons=["bi-joystick", "bi-key-fill"],
        menu_icon="",
        default_index=0,
    )

API_KEY = st.secrets["API_KEY"]

API_URL = (
        "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
    )

headers = {"Authorization": f"Bearer {API_KEY}"}

