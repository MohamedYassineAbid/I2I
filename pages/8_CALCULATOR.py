import streamlit as st

# Function to calculate the aquaponics system
def calculate_aquaponics(available_space, fish_type, quantity_fish, tank_size, plant_bed_size, plant_type, quantity_plant, avg_temp):
    # Fish data (adjusted for better growth rates and feed conversion ratios)
    fish_data = {
        "Tilapia": {"growth_rate": 2.0, "feed_conversion_ratio": 1.4, "optimal_temp": 28},
        "Catfish": {"growth_rate": 1.8, "feed_conversion_ratio": 1.5, "optimal_temp": 26},
        "Trout": {"growth_rate": 1.5, "feed_conversion_ratio": 1.2, "optimal_temp": 14},
        "Salmon": {"growth_rate": 1.3, "feed_conversion_ratio": 1.1, "optimal_temp": 12}
    }

    # Plant data (adjusted for better growth rates)
    plant_data = {
        "Lettuce": {"growth_rate": 0.8, "nutrient_uptake": 0.8, "optimal_temp": 22},
        "Tomatoes": {"growth_rate": 0.6, "nutrient_uptake": 1.2, "optimal_temp": 25},
        "Basil": {"growth_rate": 0.7, "nutrient_uptake": 0.9, "optimal_temp": 24},
        "Spinach": {"growth_rate": 0.9, "nutrient_uptake": 0.7, "optimal_temp": 20}
    }

    # Costs and prices (adjusted for better profitability)
    fish_cost = 8  # cost per fish (in dollars)
    plant_cost = 3  # cost per plant (in dollars)
    water_bed_cost = 80  # cost per water bed (in dollars)
    fish_selling_price = 25  # selling price per fish (in dollars)
    plant_selling_price = 10  # selling price per plant (in dollars)

    # Calculate system capacity (adjusted for more realistic density)
    max_fish = min(quantity_fish, available_space // (tank_size // 20))
    max_plants = min(quantity_plant, available_space // (plant_bed_size // 10))

    # Calculate growth and production (adjusted for more realistic growth)
    fish_growth = max_fish * fish_data[fish_type]["growth_rate"] * (1 - abs(avg_temp - fish_data[fish_type]["optimal_temp"]) / 200)
    plant_growth = max_plants * plant_data[plant_type]["growth_rate"] * (1 - abs(avg_temp - plant_data[plant_type]["optimal_temp"]) / 200)

    # Calculate costs (adjusted feed cost calculation)
    total_fish_cost = fish_cost * max_fish
    total_plant_cost = plant_cost * max_plants
    total_water_bed_cost = (available_space // plant_bed_size) * water_bed_cost
    feed_cost = fish_growth * fish_data[fish_type]["feed_conversion_ratio"] * 1.5  # Assuming $1.5 per kg of feed

    # Calculate revenues (adjusted for more realistic yield)
    fish_revenue = fish_growth * fish_selling_price * 0.9  # Assuming 90% of fish reach market size
    plant_revenue = plant_growth * plant_selling_price * 0.95  # Assuming 95% of plants are marketable

    # Calculate profits
    total_cost = total_fish_cost + total_plant_cost + total_water_bed_cost + feed_cost
    total_revenue = fish_revenue + plant_revenue
    profit = total_revenue - total_cost

    # Calculate efficiency
    system_efficiency = (fish_growth / max_fish + plant_growth / max_plants) / 2

    return {
        "max_fish": max_fish,
        "max_plants": max_plants,
        "fish_growth": fish_growth,
        "plant_growth": plant_growth,
        "total_cost": total_cost,
        "feed_cost": feed_cost,
        "fish_revenue": fish_revenue,
        "plant_revenue": plant_revenue,
        "total_revenue": total_revenue,
        "profit": profit,
        "system_efficiency": system_efficiency,
        "total_fish_cost": total_fish_cost,
        "total_plant_cost": total_plant_cost,
        "total_water_bed_cost": total_water_bed_cost
    }

# Set page config
st.set_page_config(page_title="Aquaponics System Calculator", layout="wide")

# Streamlit app
st.title("Aquaponics System Calculator")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("System Parameters")
    available_space = st.number_input("Available Space (in square feet):", min_value=10, value=500)
    fish_type = st.selectbox("Type of Fish:", ["Tilapia", "Catfish", "Trout", "Salmon"])
    quantity_fish = st.number_input("Quantity of Fish:", min_value=1, value=200)
    tank_size = st.number_input("Fish Tank Size (in gallons):", min_value=10, value=1000)

with col2:
    st.subheader("Plant and Environment")
    plant_type = st.selectbox("Type of Plant:", ["Lettuce", "Tomatoes", "Basil", "Spinach"])
    quantity_plant = st.number_input("Quantity of Plants:", min_value=1, value=500)
    plant_bed_size = st.number_input("Plant Bed Size (in square feet):", min_value=10, value=100)
    avg_temp = st.slider("Average Temperature (in Celsius):", min_value=0, max_value=40, value=25)

# Calculate button
if st.button("Calculate"):
    result = calculate_aquaponics(
        available_space, fish_type, quantity_fish, tank_size, plant_bed_size,
        plant_type, quantity_plant, avg_temp
    )

    # Display results
    st.subheader("Aquaponics System Analysis")

    # Create three columns for results
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("System Efficiency", f"{result['system_efficiency']:.2%}")
        st.metric("Fish Growth", f"{result['fish_growth']:.2f} kg")

    with col2:
        st.metric("Plant Growth", f"{result['plant_growth']:.2f} kg")

    # Additional insights
    st.subheader("System Insights")
    st.write(f"Your aquaponics system can support up to {result['max_fish']} {fish_type} and {result['max_plants']} {plant_type} plants.")
    st.write(f"The system's efficiency is {result['system_efficiency']:.2%}, which is influenced by the chosen fish and plant types, as well as the environmental conditions.")

    st.info("Note: This calculator provides estimates based on general data. Actual results may vary depending on specific conditions and management practices.")

