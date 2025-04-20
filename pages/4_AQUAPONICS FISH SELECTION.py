import streamlit as st
import time

def set_custom_css():
    st.markdown("""
    <style>
    .stApp {
        background: #FFFFFF;
        background-attachment: fixed;
    }
    .fade-in {
        animation: fadeIn 1.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    
    @keyframes swim {
        0%, 100% { transform: translateX(0) rotateY(0deg); }
        25% { transform: translateX(50px) rotateY(0deg); }
        50% { transform: translateX(100px) rotateY(180deg); }
        75% { transform: translateX(50px) rotateY(180deg); }
    }
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: black !important;
    }
    .streamlit-expanderContent {
        background-color: rgba(0, 0, 0, 0.2) !important;
        color: black !important;
    }
    h1, h2, h3, p {
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    set_custom_css()
    st.title("🐠 Aquaponic Fish Selection 🌿")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.write("""
    Welcome to the world of Aquaponic Fish Selection! Choosing the right fish species is crucial
    for a successful aquaponics system. Let's dive into the factors to consider and some popular fish options.
    """)
    st.markdown('<div class="swim-animation"></div>', unsafe_allow_html=True)
    st.header("🧐 Factors to Consider")
    factors = [
        "Water Temperature 🌡",
        "pH Levels 📊",
        "Space Requirements 📏",
        "Oxygen Needs 💨",
        "Growth Rate 📈",
        "Market Demand 🛒"
    ]
    for factor in factors:
        st.write(f"• {factor}")
    st.header("🐟 Popular Aquaponic Fish Species")
    fish_species = {
        "Tilapia 🐠": {
            "scientific_name": "Oreochromis niloticus",
            "pros": ["Adaptable to various conditions", "Fast growth rate", "Disease resistant"],
            "cons": ["May require heating in cooler climates", "Can be aggressive"],
            "optimal_temp": "20-30°C (68-86°F)",
            "pH_range": "6.5-8.5"
        },
        "Trout 🎣": {
            "scientific_name": "Oncorhynchus mykiss",
            "pros": ["Thrive in cooler water", "High-value fish", "Efficient feed conversion"],
            "cons": ["Require high oxygen levels", "Sensitive to water quality"],
            "optimal_temp": "10-18°C (50-64°F)",
            "pH_range": "6.5-8.5"
        },
    }
    for species, details in fish_species.items():
        with st.expander(species):
            st.write(f"*Scientific Name:* {details['scientific_name']}")
            st.write(f"*Optimal Temperature:* {details['optimal_temp']}")
            st.write(f"*pH Range:* {details['pH_range']}")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Pros ✅")
                for pro in details["pros"]:
                    st.write(f"• {pro}")
            with col2:
                st.subheader("Cons ❌")
                for con in details["cons"]:
                    st.write(f"• {con}")
            time.sleep(0.5)
    st.markdown('</div>', unsafe_allow_html=True)
    st.header("🌟 Conclusion")
    st.write("""
    Selecting the right fish species is crucial for the success of your aquaponics system. Consider
    factors like water temperature, pH levels, and space requirements when making your choice.
    Remember, a thriving fish population leads to healthy plants and a productive aquaponics ecosystem!
    """)

if __name__ == "__main__":
    main()

