import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wikipedia Speedrun", page_icon="📚", layout="wide")

def add_to_leaderboard():
    if st.session_state.name == "":
        st.session_state.name = "Anonymous"
    if not st.session_state.start_page.startswith("https://en.wikipedia.org/wiki/") or not st.session_state.end_page.startswith("https://en.wikipedia.org/wiki/"):
        st.error("Invalid start or end page. Entry not recorded")
        return
    if st.session_state.time == 0:
        st.error("Time not entered. Entry not recorded")
        return
    new_entry = {"Name": st.session_state.name, "Start Page": st.session_state.start_page, "End Page": st.session_state.end_page, "Time (s)": st.session_state.time}
    new_df = pd.DataFrame([new_entry])
    new_df.to_csv("leaderboard.csv", mode='a', index=False, header=False)

# Main content
st.markdown("<center><h1>Leaderboard</h1></center>", unsafe_allow_html=True)
st.markdown("<center><p>Welcome to the Leaderboard <br> Columns in the table can be sorted by clicking the header. <br> Best of luck and no Lying/Cheating!</p></center>", unsafe_allow_html=True)

with st.expander("Add Your Own Entry!"):
    with st.form("leaderboard_form"):
        name = st.text_input(label="Name", key="name")
        start_page = st.text_input(label="Starting Page", key="start_page")
        end_page = st.text_input(label="Ending Page", key="end_page")
        time = st.number_input(label="Time (in seconds)", key="time", step=1)
        
        submit_form = st.form_submit_button(label="Add to Leaderboard", on_click=add_to_leaderboard)

leaderboard_df = pd.read_csv("leaderboard.csv")

st.dataframe(leaderboard_df, use_container_width=True, hide_index=True)
