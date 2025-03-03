import streamlit as st

def name_to_bytes(name: str) -> list:
    return list(name.encode("utf-8"))

# Streamlit UI with enhanced styling
st.set_page_config(page_title="Name to Bytes Converter", page_icon="🔤", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
        }
        .description {
            text-align: center;
            font-size: 18px;
            color: #333;
            margin-bottom: 20px;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 2px solid #4CAF50;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>🔤 Name to Bytes Converter</h1>", unsafe_allow_html=True)
st.markdown("""
<p class='description'>
Easily convert your name into **UTF-8 byte values**! This tool is perfect for encoding, security, or data processing.
Just enter your name below and get the byte representation instantly! 🚀
</p>
""", unsafe_allow_html=True)

# Initialize session state for name history if not exists
if "name_history" not in st.session_state:
    st.session_state.name_history = []

# User input
name = st.text_input("Enter your name:")

if st.button("Convert"):
    if name:
        byte_representation = name_to_bytes(name)
        st.session_state.name_history.append((name, byte_representation))

# Display conversion history
if st.session_state.name_history:
    st.markdown("## Conversion History")
    for n, b in st.session_state.name_history:
        st.success(f"**{n}:** {b}")
