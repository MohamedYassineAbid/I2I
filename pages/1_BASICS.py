import streamlit as st
import time

st.set_page_config(page_title="Aquaponics 101", page_icon="🌿", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        color: black;
    }
    .stMarkdown a {
        color: #32CD32;  /* Keep link color */
    }
    .big-font {
        font-size: 22px;
        color: black;  /* Changed to black */
    }
    .small-font {
        font-size: 18px;
        color: black;  /* Changed to black */
    }
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stImage {
        border-radius: 10px;
        border: 2px solid #32CD32;
    }
    .fade-in {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

content = {
    "title": "🌿 Aquaponics: The Future of Sustainable Farming 🐟",
    "definition": """
    Aquaponics is a sustainable method of farming that merges *aquaculture* (raising fish) and *hydroponics* (growing plants without soil). In this ecosystem:
    - Fish produce nutrient-rich waste.
    - Plants absorb these nutrients, cleaning the water for the fish.
    It's an amazing cycle of life! 🌱🐠
    """,
    "how_it_works": [
        "Fish release waste into the water.",
        "Bacteria convert waste into nutrients for plants.",
        "Plants filter and clean the water.",
        "Clean water is pumped back to the fish tank."
    ],
    "benefits": [
        "💧 *Water Conservation:* Uses 90% less water than traditional farming.",
        "🌱 *No Chemical Fertilizers:* Fish provide natural nutrients for plants.",
        "📆 *Year-Round Production:* Can be operated in any season with controlled environments.",
        "🔄 *Recycling:* Efficiently reuses water, reducing waste.",
        "🍽 *Dual Production:* Grows both fish and fresh produce in one system."
    ],
    "components": {
        "Fish Tank": "The tank where fish live and produce nutrient-rich waste.",
        "Grow Beds": "Beds where plants grow and absorb nutrients from fish waste.",
        "Water Pump": "Circulates water between the fish tank and grow beds.",
        "Filtration System": "Filters solid waste and aerates water for fish."
    },
    "types": {
        "1. Media-Based Aquaponics": "Utilizes a solid medium, like gravel or clay pellets, for plant roots.",
        "2. Nutrient Film Technique (NFT)": "Involves a thin film of nutrient-rich water flowing over plant roots.",
        "3. Deep Water Culture (DWC)": "Plants float on rafts in a nutrient-rich solution with their roots submerged.",
        "4. Vertical Aquaponics": "Incorporates vertical growing systems to maximize space usage.",
        "5. Hybrid Aquaponics": "Combines elements from different systems for improved efficiency."
    },
    "footer": "🌾 Join the #SustainableFarming Revolution! 🌾",
    "final_text": "📊 Your Sustainable Journey Starts Now! Tracking your progress in sustainability is important. Check how far you’ve come:"
}

st.markdown(f"<h1 class='fade-in'>{content['title']}</h1>", unsafe_allow_html=True)
st.header("What is Aquaponics? 🤔")
st.markdown(content["definition"], unsafe_allow_html=True)
st.header("🔄 How Aquaponics Works ")
steps = content["how_it_works"]
progress_bar = st.progress(0)
step_text = st.empty()
for i, step in enumerate(steps):
    progress_bar.progress((i + 1) * 25)
    step_text.markdown(f"<p class='small-font fade-in'>{step}</p>", unsafe_allow_html=True)
    time.sleep(1)
progress_bar.empty()
step_text.markdown("<p class='small-font fade-in'>Aquaponics is a beautifully symbiotic cycle! 🌍</p>", unsafe_allow_html=True)
st.header("🌟 Benefits of Aquaponics")
for benefit in content["benefits"]:
    st.markdown(f"<p class='small-font fade-in'>{benefit}</p>", unsafe_allow_html=True)
st.header("🔧 Key Components")
for component, description in content["components"].items():
    st.markdown(f"<strong>{component}</strong>: {description}", unsafe_allow_html=True)
st.header("🔍 Types of Aquaponics")
for type_, description in content["types"].items():
    st.markdown(f"<p class='small-font fade-in'>{type_}: {description}</p>", unsafe_allow_html=True)
st.markdown(f"<h4 class='fade-in'>{content['footer']}</h4>", unsafe_allow_html=True)
st.markdown(f"<p class='small-font fade-in'>{content['final_text']}</p>", unsafe_allow_html=True)
    
