import streamlit as st
import yt_dlp
import  pytube
# Streamlit app
tabs = st.sidebar.radio("Select  the  platform:", ("Youtube", "Facebook", "instagram"))
if tabs=="Youtube":
    st.title("Welcome ")
    # Get YouTube video URL from user input
    video_url = st.text_input("Enter YouTube video URL")
    if  video_url !="":
        ken = pytube.YouTube(video_url)
    # Check if the URL is provided
        card_style = """
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            background-color: white;
            margin: 10px;
        """

        # Create a card layout
        col1, col2, col3 = st.columns(3)

        # Card 1
        with col1:
            st.markdown('<div style="{}">Title: {} </div>'.format(card_style, ken.title), unsafe_allow_html=True)
        # st.write("This is the content of Card 1.")

        # Card 2
        with col2:
            st.markdown('<div style="{}">Author: {}</div>'.format(card_style,ken.author), unsafe_allow_html=True)
        # st.write("This is the content of Card 2.")

        # Card 3
        with col3:
            st.markdown('<div style="{}">No of views: {}</div>'.format(card_style, ken.views), unsafe_allow_html=True)

        ######
        card_style2 = """
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            background-color: white;
            margin: 10px;
        """
        st.markdown("""
        <div style='{}'>
        <iframe width="560" height="315" src="{}" frameborder="0" allowfullscreen></iframe>
    """.format(card_style2,ken.thumbnail_url), unsafe_allow_html=True)

    if video_url:
        # Set options for download
        ydl_opts = {
            'format': 'bestvideo[height=720][ext=mp4]+bestaudio[ext=m4a]/best[height=480][ext=mp4]+bestaudio[ext=m4a]',
            'outtmpl': '%(id)s.%(ext)s',
        }

        # Create a YTDL object
        ydl = yt_dlp.YoutubeDL(ydl_opts)

        # Extract video information
        info_dict = ydl.extract_info(video_url, download=False)

        # Get the available formats
        formats = info_dict.get('formats', [])

        # Find the 480p format with sound
        format_480p = next((f for f in formats if f.get('height') == 480 and f.get('acodec') is not None), None)
        if format_480p:
            download_link_480p = format_480p['url']
            st.markdown("### 480p Download Link:")
            st.markdown(f"Video download [Here]({download_link_480p})")
            st.markdown(f""" ``` Bash
            {download_link_480p}
            """)


        # Find the 720p format with sound
        format_720p = next((f for f in formats if f.get('height') == 720 and f.get('acodec') is not None), None)
        if format_720p:
            download_link_720p = format_720p['url']
            st.markdown("### 720p Download Link:")
            st.markdown(f"Video download [Here]({download_link_720p})")
            st.markdown(f""" ``` Bash
            {download_link_720p}
            """)
if tabs=="Facebook":
    st.markdown("# Facebook video download  site")
    url = st.text_input("Paste  your  link here:")
    card_style2 = """
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
        background-color: white;
        margin: 10px;
    """

    if  url!="":
        options = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]",
            "merge_output_format": "mp4"}
        with yt_dlp.YoutubeDL(options) as  ytdl:
            try:
                with ytdl:
                    info = ytdl.extract_info(url, download = False)
                    if  "entries" in info:
                        video = info["entries"][0]
                    else:
                        video = info
                    link_d = []
                    for  i in video["formats"]:
                        link_d.append(i["url"])

                    link1  = link_d[2]
                    link2 = link_d[3]
                    button_style="""
                        <style>
                        .custom-button {
                        display: inline-block;
                        padding: 10px 20px;
                        font-size: 16px;
                        font-weight: bold;
                        border: none;
                        border-radius: 5px;
                        background-color: #ffc107;
                        color: #fff;
                        box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
                        transition: all 0.3s ease-in-out;
                        }

                        .custom-button:hover {
                        background-color: #ffa000;
                        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.4);
                        transform: translateY(-3px);
                        cursor: pointer;
                        </style>
                        }
                    """
                    st.markdown("""
                    <div style='{}'>
                    <b> Download  low quality:</a><br/>
                    <a href="{}">Download Here</a>
                    </div>
                """.format(card_style2, link1), unsafe_allow_html=True)
                    st.markdown("""
                    <div style='{}'>
                    <b> Download  High quality:</a><br/>
                    <a href="{}">Download Here</a>
                    </div>
                """.format(card_style2, link2), unsafe_allow_html=True)
                    card_style2 = """
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
                        background-color: white;
                        margin: 10px;
                    """
                    st.markdown("""
                    <div style='{}'>
                    Click on anylink to download  the  video.
                    </div>
                    """.format(card_style2), unsafe_allow_html=True)
            except ConnectionRefusedError as e:
                st.error("Failed  to fecth the  video!")
if  tabs=="instagram":
    st.info("Not  implimemted Error!")
