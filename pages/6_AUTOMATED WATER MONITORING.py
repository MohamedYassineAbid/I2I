import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(page_title="AI-Driven Water Quality Monitoring", layout="wide")

# Custom CSS for light theme and animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
    background-color: #FFFFFF;
    color: #000000;
}

.stApp {
    background: #FFFFFF;
    background-size: 40px 40px;
    animation: move-bg 10s linear infinite;
}

@keyframes move-bg {
    0% {background-position: 0 0;}
    100% {background-position: 40px 40px;}
}

h1, h2, h3 {
    color: #4CAF50;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    background-color: #45a049;
    transform: scale(1.05);
}

.element {
    position: fixed;
    width: 50px;
    height: 50px;
    border: 2px solid rgba(76, 175, 80, 0.3);
    border-radius: 50%;
    pointer-events: none;
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
}

.element:nth-child(1) { top: 10%; left: 10%; animation: float 6s infinite; }
.element:nth-child(2) { top: 20%; right: 10%; animation: float 8s infinite; }
.element:nth-child(3) { bottom: 10%; left: 15%; animation: float 10s infinite; }
.element:nth-child(4) { bottom: 20%; right: 15%; animation: float 7s infinite; }

@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
    100% { transform: translateY(0px) rotate(360deg); }
}

.fade-in {
    animation: fadeIn 1.5s;
}

@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

.st-emotion-cache-1v0mbdj.e115fcil1 {
    border-color: #4CAF50;
}

</style>

<div class="element"></div>
<div class="element"></div>
<div class="element"></div>
<div class="element"></div>
""", unsafe_allow_html=True)

def main():
    # Title
    st.markdown('<h1 class="fade-in">Automated Water Quality Monitoring in Aquaponics using AI</h1>', unsafe_allow_html=True)

    # Introduction
    st.markdown('<p class="fade-in">Explore how AI revolutionizes water quality monitoring in aquaponics systems, ensuring optimal conditions for both fish and plants.</p>', unsafe_allow_html=True)

    # Simulated real-time data
    @st.cache_data
    def generate_data():
        dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="H")
        df = pd.DataFrame({
            "Date": dates,
            "pH": np.random.normal(7, 0.5, len(dates)),
            "Temperature": np.random.normal(25, 2, len(dates)),
            "Dissolved Oxygen": np.random.normal(6, 1, len(dates)),
            "Ammonia": np.random.normal(0.5, 0.2, len(dates)),
            "Nitrate": np.random.normal(10, 2, len(dates)),
            "Nitrite": np.random.normal(0.1, 0.05, len(dates)),
            "Electrical Conductivity": np.random.normal(1500, 200, len(dates))
        })
        return df

    data = generate_data()

    # Sidebar
    st.sidebar.header("Control Panel")
    parameter = st.sidebar.selectbox("Select Parameter", ["pH", "Temperature", "Dissolved Oxygen", "Ammonia", "Nitrate", "Nitrite", "Electrical Conductivity"])
    time_range = st.sidebar.slider("Select Time Range (Days)", 1, 30, 7)

    # Main content
    col1, col2 = st.columns([2, 1])

    with col2:
        st.markdown('<h2 class="fade-in">AI Predictions</h2>', unsafe_allow_html=True)

        if st.button("Generate AI Prediction"):
            with st.spinner("AI is analyzing the data..."):
                time.sleep(2)  # Simulating AI processing time
            st.success("AI Prediction Complete!")

            # Simulated AI prediction
            current_value = data[parameter].iloc[-1]
            prediction = current_value + np.random.normal(0, 0.1)

            st.metric(label=f"Current {parameter}", value=f"{current_value:.2f}")
            st.metric(label=f"Predicted {parameter} (Next 24 hours)", value=f"{prediction:.2f}", delta=f"{prediction-current_value:.2f}")

            # Additional AI insights
            st.markdown("### AI Insights")
            insights = [
                "Water quality is within optimal range.",
                f"Slight increase in {parameter.lower()} expected.",
                "No immediate action required.",
                "Next recommended water change: 3 days"
            ]
            for insight in insights:
                st.markdown(f"- {insight}")

    # Historical Trends
    st.markdown('<h2 class="fade-in">Historical Trends</h2>', unsafe_allow_html=True)

    # Calculate monthly averages
    monthly_data = data.set_index('Date').resample('M').mean().reset_index()

    fig = make_subplots(rows=2, cols=2, subplot_titles=("pH", "Temperature", "Dissolved Oxygen", "Ammonia"))

    fig.add_trace(go.Scatter(x=monthly_data['Date'], y=monthly_data['pH'], mode='lines+markers', name='pH'), row=1, col=1)
    fig.add_trace(go.Scatter(x=monthly_data['Date'], y=monthly_data['Temperature'], mode='lines+markers', name='Temperature'), row=1, col=2)
    fig.add_trace(go.Scatter(x=monthly_data['Date'], y=monthly_data['Dissolved Oxygen'], mode='lines+markers', name='Dissolved Oxygen'), row=2, col=1)
    fig.add_trace(go.Scatter(x=monthly_data['Date'], y=monthly_data['Ammonia'], mode='lines+markers', name='Ammonia'), row=2, col=2)

    fig.update_layout(height=800, title_text="Monthly Averages of Key Parameters", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='black'))
    fig.update_xaxes(showgrid=False, gridcolor='rgba(255,255,255,0.2)')
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.2)')

    st.plotly_chart(fig, use_container_width=True)

    # Alerts for parameter thresholds
    st.markdown('<h2 class="fade-in">Alerts</h2>', unsafe_allow_html=True)

    # Define thresholds for alerts
    thresholds = {
        "pH": (6.8, 7.2),
        "Temperature": (18, 30),
        "Dissolved Oxygen": (5, float('inf')),
        "Ammonia": (0, 0.02),
        "Nitrate": (0, 50),
        "Nitrite": (0, 0.1),
        "Electrical Conductivity": (1000, 2000)
    }

    # Check for alerts
    alerts = []
    recommendations = []
    for param, (low, high) in thresholds.items():
        current_value = data[param].iloc[-1]
        if current_value < low or current_value > high:
            alerts.append(f"Alert: {param} is out of range! Current value: {current_value:.2f}")
            recommendations.append(f"Recommendation for {param}: Adjust {param} to be within {low} and {high}.")

    # Display alerts
    if alerts:
        for alert in alerts:
            st.error(alert)
    else:
        st.success("All parameters are within the optimal range.")

    # Display recommendations
    if recommendations:
        st.markdown('<h2 class="fade-in">Recommendations</h2>', unsafe_allow_html=True)
        for recommendation in recommendations:
            st.warning(recommendation)

    # AI benefits
    st.markdown('<h2 class="fade-in">Benefits of AI in Aquaponics</h2>', unsafe_allow_html=True)
    benefits = [
        "24/7 Monitoring",
        "Early Problem Detection",
        "Predictive Maintenance",
        "Resource Optimization",
        "Improved Crop and Fish Yields",
        "Automated pH and Nutrient Balancing",
        "Energy Efficiency through Smart Controls",
        "Customized Feeding Schedules",
        "Disease Prevention and Early Detection"
    ]
    for benefit in benefits:
        st.markdown(f'<p class="fade-in">• {benefit}</p>', unsafe_allow_html=True)

    # Future Developments
    st.markdown('<h2 class="fade-in">Future Developments in AI-Driven Aquaponics</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="fade-in">
    <ul>
        <li>Integration with IoT devices for comprehensive system control</li>
        <li>Machine learning models for optimizing plant-fish combinations</li>
        <li>Computer vision for plant health monitoring and fish behavior analysis</li>
        <li>Blockchain integration for supply chain transparency and food traceability</li>
        <li>Advanced predictive models for yield optimization and resource allocation</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

