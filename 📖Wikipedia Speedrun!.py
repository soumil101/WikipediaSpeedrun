import streamlit as st
import wikipedia
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from PIL import Image
from io import BytesIO
from wikipedia.exceptions import DisambiguationError
import pandas as pd

# Define the filename for the leaderboard CSV file
LEADERBOARD_FILENAME = "leaderboard.csv"

current_dir = Path(__file__).parent
css_file = current_dir / "styles" / "styles.css"

st.set_page_config(page_title="Wikipedia Speedrun", page_icon="📚")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Function to capture a screenshot of a Wikipedia page
def capture_page_screenshot(title):
    options = Options()
    options.headless = True  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=options)
    try:
        url = wikipedia.page(title).url
        driver.get(url)
        screenshot = driver.get_screenshot_as_png()
        return Image.open(BytesIO(screenshot))
    except Exception as e:
        return None
    finally:
        driver.quit()

# Function to generate a summary of a Wikipedia page
def generate_summary(title):
    page = wikipedia.page(title)
    summary = page.summary
    return summary

# Function to generate a random Wikipedia page
def generate_title():
    while True:
        title = wikipedia.random()
        return title

# Function to generate two random Wikipedia pages through every error lol
def generate_random_pages():
    page_titles = []
    page_urls = []
    
    while len(page_titles) < 2:
        try:
            title = generate_title()
            page_titles.append(title)
            page_urls.append(wikipedia.page(title).url)
        except Exception as e:
            continue
    
    return page_titles, page_urls

# Function to add a new entry to the leaderboard CSV file
def add_to_leaderboard():
    if st.session_state.name == "":
        st.session_state.name = "Anonymous"
    if st.session_state.time == 0:
        st.error("Time not entered. Entry not recorded")
        return
    new_entry = {"Name": st.session_state.name, "Start Page": st.session_state.start_page, "End Page": st.session_state.end_page, "Time (s)": st.session_state.time}
    new_df = pd.DataFrame([new_entry])
    new_df.to_csv("leaderboard.csv", mode='a', index=False, header=False)


# Main content
st.markdown("<left><h1 style='color: #E77D8F; font-family: cursive;'>Wikipedia Speedrun!</h1></left>", unsafe_allow_html=True)
st.markdown("<left><p>Welcome to Wikipedia Speedrun! Begin by pressing the Generate! button below. You'll then see 2 wikiepedia pages pop up. The goal is to get from one page to the other using only links within the wikipedia pages for traversal. No command F'ing! And the only context you get about each page are the summaries that are generated as well. Optionally, if you like, you can add your speedrun to our Leaderboard! If you're feeling competitive, browse the leaderboards and try to beat someone else's time on their page route! </p></left>", unsafe_allow_html=True)
st.markdown("<left><p style='color: gray; font-size: small;'>If there are any errors, just regenerate. Proper error handling will come later</p></left>", unsafe_allow_html=True)


# Button to generate random Wikipedia pages, capture screenshots, and generate summaries
if st.button("Generate!"):
    with st.spinner("Generating random Wikipedia pages..."):
        # Initialize variables to hold page titles and URLs
        page_titles, page_urls = generate_random_pages()

        # Create two columns for displaying the pages side by side
        col1, col2 = st.columns(2)

        # Fetch and display the Wikipedia pages along with screenshots and summaries
        for i, title in enumerate(page_titles):
            page_url = wikipedia.page(title).url

            # Capture a screenshot of the page
            screenshot = capture_page_screenshot(title)

            # Generate a summary of the page
            summary = generate_summary(title)

            # Display the screenshot if available, or a placeholder
            if screenshot:
                with col1 if i % 2 == 0 else col2:
                    st.image(screenshot, use_column_width=True)
            else:
                st.warning("Failed to capture the page screenshot.")

            # Display the page title as a link
            with col1 if i % 2 == 0 else col2:
                st.subheader(f"[{title}]({page_url})")
                st.write(summary)

    with st.expander("Add Entry to Leaderboard"):
        with st.form("leaderboard_form"):
            name = st.text_input(label="Name", key="name")
            start_page = st.text_input(label="Starting Page", key="start_page", value=page_urls[0])
            end_page = st.text_input(label="Ending Page", key="end_page", value=page_urls[1])
            time = st.number_input(label="Time (in seconds)", key="time", step=1)
            
            submit_form = st.form_submit_button(label="Add to Leaderboard", on_click=add_to_leaderboard)
            if submit_form:
                st.success(f"Entry added to leaderboard. {name} took {time} seconds to get from {start_page} to {end_page}.")