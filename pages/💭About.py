import streamlit as st
from pathlib import Path
from streamlit_extras.stylable_container import stylable_container

current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "styles.css"

st.set_page_config(page_title="About Wikipedia Speedrun", page_icon="💭")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


'hi there,'

''

'thank you for trying out wikipedia speedrun. i had a lot of fun making this game, and i hope you had fun playing it!'

''

'the main technologies used in this project were streamlit, wikipedia, and selenium. i used streamlit for the frontend, wikipedia for its API, and selenium to webscrape the wikipedia pages. the site uses a tokyo night / robbyrussel theme.'

''

st.markdown("""<p>please check out the github repository  :   <a href="https://github.com/soumil101/WikipediaSpeedrun" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="20" fill="gray" class="bi bi-github" viewBox="0 0 16 16">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
</svg></a></p>""", unsafe_allow_html=True)

''

'the next steps are to add a timer and more nuanced leaderboard. feel free to contribute. any additional ideas are welcome!'

''

'contact:'
st.write("<a href='mailto:soumilgad@gmail.com' style='color: white;'>soumilgad@gmail.com</a>", unsafe_allow_html=True)

# with stylable_container(
#     key="footer",
#     css_styles="""
#         .wrapper {
#             margin-top: -96px;
#             margin-bottom: -160px;
#             min-height: 100vh;
#         }
#         .footer {
#             font-size: 12px;
#             color: gray;
#             position: absolute;
#             bottom: 0;
#             padding: 0;
#         }
#         """,
# ):
#     st.markdown("""<div class="wrapper"><div class="footer">Made with <3 by Soumil</div></div>""", unsafe_allow_html=True)