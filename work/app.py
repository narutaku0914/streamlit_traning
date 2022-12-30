import streamlit as st

from streamlit_player import st_player, _SUPPORTED_EVENTS

def main():
  c1, c2 = st.columns([6, 4])

  with c2:
    st.subheader("Parameters")

    options = {
        "events": st.multiselect("Events to listen", _SUPPORTED_EVENTS, ["onProgress"]),
        "progress_interval": 1000,
        "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
        "playing": st.checkbox("Playing", False),
        "loop": st.checkbox("Loop", False),
        "controls": st.checkbox("Controls", True),
        "muted": st.checkbox("Muted", False),
    }

  with c1:
    url = st.text_input("First URL", "https://youtu.be/c9k8K1eII4g")
    event = st_player(url, **options, key="youtube_player")

    st.write(event)


if __name__ == "__main__":
  main()

