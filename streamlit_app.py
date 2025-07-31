import streamlit as st
import model  # Assuming your AI model is in a file named 'model.py'
import utils
# Set page configuration
st.set_page_config(
    page_title="Elemental Life Prediction",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add a title and description
st.title("Elemental Life Prediction")
st.write("Enter the elemental composition of a hypothetical planet to predict the likelihood of life.")

# Sidebar for user inputs
with st.sidebar:
    st.header("Planet Configuration")

    # Input fields for elemental composition
    element_input = st.text_input("Enter elements (comma-separated):", "C, H, O, N")
    elements = [e.strip() for e in element_input.split(",")]

    temperature = st.slider("Temperature (°C)", -200, 200, 25)
    pressure = st.slider("Pressure (atm)", 0.1, 100.0, 1.0)
    has_water = st.checkbox("Presence of Water", value=True)

    if st.button("Predict Life"):
        # Process the inputs
        input_data = utils.prepare_input_data(elements, temperature, pressure, has_water)

        # Make prediction using the AI model
        prediction = model.predict_life(input_data)

        # Display the prediction
        st.header("Prediction")
        st.write(f"Probability of Life: {prediction['probability']:.2f}")
        st.write(f"Potential Life Forms: {prediction['description']}")

        # Add a visualization (example)
        st.header("Visualization")
        # Assuming utils.generate_visualization returns a matplotlib figure
        fig = utils.generate_visualization(prediction)
        st.pyplot(fig)

# Add some info/disclaimer at the bottom
st.markdown("---")
st.write("This is a hypothetical prediction based on a simplified AI model.  The results are for entertainment and educational purposes only.")