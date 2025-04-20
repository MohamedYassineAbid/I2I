import streamlit as st

PAGE_TITLE = "Aquaponics: The Future of Sustainable Farming"
PAGE_ICON = "🌱"
AQUAPONICS_ASSOCIATION_URL = "https://aquaponicsassociation.org/"

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
body {
    font-family: 'Poppins', sans-serif;
    background-color: #FFFFFF; /* White background */
    color: #000000; /* Black text */
}
h1, h2, h3 {
    font-weight: 600;
}
p, li {
    font-weight: 300;
    line-height: 1.6;
}
.stButton>button {
    color: #ffffff;
    background-color: #4CAF50;
    border-radius: 20px;
    padding: 10px 24px;
    font-size: 16px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #45a049;
    transform: scale(1.05);
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
}
.stApp {
    background-color: transparent;
    padding: 20px;
}
@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}
.fade-in {
    animation: fadeIn 1.5s;
}
</style>
"""

def load_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def render_header():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🌱 Welcome to the World of Aquaponics!")
    st.subheader("Cultivating Sustainability, One Fish at a Time")
    st.markdown('</div>', unsafe_allow_html=True)

def render_inspirational_quote():
    st.markdown(
        """
        <div class="fade-in" style='padding: 20px; background-color: rgba(255, 255, 255, 0.1); border-radius: 10px; text-align: center;'>
            <h3>"In the circle of life, every drop nurtures growth.<br>Aquaponics: Where fish and plants dance in harmony."</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_aquaponics_revolution():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("## 🌊 The Aquaponics Revolution")
    st.write(
        "Aquaponics is more than just a farming technique; it's a philosophy of sustainable living. "
        "By combining aquaculture (raising fish) and hydroponics (growing plants in water), we create "
        "a symbiotic ecosystem that mimics nature's perfect balance."
    )
    st.markdown('</div>', unsafe_allow_html=True)

def render_why_aquaponics_matters():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("## 🐠 Why Aquaponics Matters")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            - 🌍 Conserves water
            - 🌱 Produces organic food
            - 🐟 Supports local ecosystems
            """
        )
    with col2:
        st.markdown(
            """
            - 🏙️ Perfect for urban farming
            - 🌿 Reduces carbon footprint
            - 💚 Promotes sustainable living
            """
        )
    st.markdown('</div>', unsafe_allow_html=True)

def render_footer():
    st.markdown(
        """
        <div class="fade-in" style='text-align: center; padding: 20px;'>
            <p>Created with 💚 by Aquaponics Enthusiasts</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

    load_css()

    # Main content
    render_header()
    render_inspirational_quote()
    render_aquaponics_revolution()
    render_why_aquaponics_matters()
    render_footer()

if __name__ == "__main__":
    main()

