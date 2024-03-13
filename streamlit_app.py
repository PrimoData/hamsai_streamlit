import streamlit as st
import replicate
import time
import os

# Configure Streamlit Page
page_icon = "https://pbs.twimg.com/profile_images/1764746187754606593/lwhMyQ2P_400x400.jpg"
st.set_page_config(page_title="$HAMSAI Generator", page_icon=page_icon)

# Read Custom CSS
with open("assets/css/style.css", "r") as f:
    css_text = f.read()
custom_css = f"<style>{css_text}</style>"
st.markdown(custom_css, unsafe_allow_html=True)

# Heading
st.title("$HAMSAI Generator")
st.caption("Unofficial image generator for the $HAMSAI crypto project on Solana (https://hamsters.ai/).")
powered_by = """
<div style="display: flex; align-items: center; margin-bottom:0px">
    <span style="font-size: 12px; margin-right: 4px; font-style: italic;">Powered by:</span>
    <img src="https://www.sequoiacap.com/wp-content/uploads/sites/6/2022/06/replicate-logo-black-transparent.svg" alt="OpenAI logo" height="16" style="margin-right: 4px;"> 
    <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" alt="OpenAI logo" height="20" style="margin-right: 4px;">
    <img src="https://s3.us-west-2.amazonaws.com/cube365-prod/related-content/9b767197-769f-44ea-9b17-9c93606799be.png" alt="OpenAI logo" height="16" style="margin-right: 4px;">
</div>
"""
st.markdown(powered_by, unsafe_allow_html=True)
st.divider()


# Generate image of $HAMSAI using Replicate API
def generate_image_hamsai(prompt):
    prompt = prompt.replace("$HAMSAI", "TOK").replace("$HAMSAI", "TOK")
    print(f"submitted {prompt}")
    output = replicate.run(
        "primodata/hamsai:9c4193f928f28f60f92cd1c0321b60236d694c2837d4fb5b56b687c70c67b762",
        input={"prompt": prompt},
    )
    return output[0]


prompt = st.text_input(
    "Generate an image of $HAMSAI using natural language.",
    help="",
)
with st.expander("Examples:"):
    city = st.button("$HAMSAI in a city.")

generate_image = st.button("Generate Image")


if generate_image:
    # check if prompt contains '$HAMSAI'
    if "$hamsai" not in prompt.lower():
        st.error("'$HAMSAI' needs to be in your prompt.")
    else:
        with st.spinner(text="Generating. This could take a minute..."):
            image_url = generate_image_hamsai(prompt)
        st.image(image_url)


# Examples
if city:
    with st.spinner(text="Generating. This could take a minute..."):
        time.sleep(5)
    st.image(
        "https://replicate.delivery/pbxt/brfa9nhCnaUZKKPllfjMbc5DxzmJImeJTY5apiPWJC4i2XfJB/out-0.png"
    )
