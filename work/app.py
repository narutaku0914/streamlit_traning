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

API_KEY = st.secrets["API_KEY"]

API_URL = (
    "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
)

headers = {"Authorization": f"Bearer {API_KEY}"}

with st.sidebar:
    selected = option_menu(
        "",
        ["Demo", "Unlocked Mode"],
        icons=["bi-joystick", "bi-key-fill"],
        menu_icon="",
        default_index=0,
    )


label_widget = st_tags(
            label="",
            text="Add labels - 3 max",
            value=["Transactional", "Informational"],
            suggestions=[
                "Navigational",
                "Transactional",
                "Informational",
                "Positive",
                "Negative",
                "Neutral",
            ],
            maxtags=3,
        )

MAX_LINES = 5
text = st.text_area(
            "Enter keyphrase to classify",
            sample,
            height=200,
            key="2",
            help="At least two keyphrases for the classifier to work, one per line, "
            + str(MAX_LINES)
            + " keyphrases max as part of the demo",
        )
lines = text.split("\n")  # A list of lines
linesList = []
for x in lines:
    linesList.append(x)
linesList = list(dict.fromkeys(linesList))  # Remove dupes
linesList = list(filter(None, linesList))  # Remove empty


if len(linesList) > MAX_LINES:
    st.info(
        f"🚨 Only the first "
        + str(MAX_LINES)
        + " keyprases will be reviewed. Unlock that limit by switching to 'Unlocked Mode'"
    )
