import streamlit as st
import model  # Assuming your AI model is in a file named 'model.py'
import utils  # Helper functions

# --- Page Configuration ---
st.set_page_config(
    page_title="Elemental Life Prediction",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
# --- Sidebar for User Inputs ---
with st.sidebar:
    st.header("🪐 Planet Configuration")
 
    # A list of common elements for the multiselect
    POSSIBLE_ELEMENTS = [
        'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 
        'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Fe'
    ]
    DEFAULT_ELEMENTS = ['C', 'H', 'O', 'N', 'P', 'S']
 
    st.subheader("Select Present Elements")
 
    # --- Initialize session state for checkboxes on first run ---
    # This ensures that the default values are set only once.
    if 'elements_initialized' not in st.session_state:
        for element in POSSIBLE_ELEMENTS:
            st.session_state[f"elem_{element}"] = (element in DEFAULT_ELEMENTS)
        st.session_state['elements_initialized'] = True

    # --- Add Select/Deselect All buttons ---
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Select All", use_container_width=True, key="select_all"):
            for element in POSSIBLE_ELEMENTS:
                st.session_state[f"elem_{element}"] = True
    with c2:
        if st.button("Deselect All", use_container_width=True, key="deselect_all"):
            for element in POSSIBLE_ELEMENTS:
                st.session_state[f"elem_{element}"] = False

    # --- Create a grid of checkboxes for element selection ---
    selected_elements = []
    # Define the number of columns for the grid
    grid_cols = 5
    cols = st.columns(grid_cols)

    # Iterate over elements and create a checkbox in the grid
    for i, element in enumerate(POSSIBLE_ELEMENTS):
        with cols[i % grid_cols]:
            # The value is now managed by session state via the key
            is_checked = st.checkbox(element, key=f"elem_{element}")
            if is_checked:
                selected_elements.append(element)
 
    temperature = st.slider("Average Surface Temperature (°C)", -200, 300, 25)
    pressure = st.slider("Atmospheric Pressure (atm)", 0.0, 100.0, 1.0, step=0.1)
    has_water = st.checkbox("Presence of Liquid Water", value=True)
 
    # The prediction button
    predict_button = st.button("Predict Life Likelihood", type="primary", use_container_width=True, key="predict")
 
    # --- Event Trigger Section ---
    # This section only appears if a planet has been generated
    if st.session_state.get("prediction_result"):
        st.markdown("---")
        st.header("☄️ Trigger Event")
        event_type = st.selectbox(
            "Select an event to unleash:",
            ("Asteroid Impact", "Pandemic Outbreak", "Super-Volcano Eruption"),
            index=None,
            placeholder="Select a cataclysm...",
            key="event_selector"
        )
        
        if st.button("Unleash Event", use_container_width=True, key="unleash"):
            if event_type:
                # Re-run prediction with the selected event
                event_prediction = model.predict_life(st.session_state.input_data, event=event_type)
                st.session_state.prediction_result = event_prediction
                st.toast(f"Event triggered: {event_type}!", icon="💥")
                st.rerun()
# --- Main Panel for Title and Results ---
st.title("Elemental Life Prediction 🌌")
st.write(
    "Configure a hypothetical planet's conditions in the sidebar and click "
    "the button to predict the likelihood of life based on a simplified model."
)
 
# Initialize session state to store the prediction
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None
if 'input_data' not in st.session_state:
    st.session_state.input_data = None
 
# If the button is clicked, run the prediction and store the result
if predict_button:
    # Process the inputs
    input_data = utils.prepare_input_data(selected_elements, temperature, pressure, has_water)
 
    # Make prediction using the AI model
    prediction = model.predict_life(input_data)
    
    # Store the result in session state
    st.session_state.prediction_result = prediction
    st.session_state.input_data = input_data
 
# Display the prediction result if it exists in the session state
if st.session_state.prediction_result:
    prediction = st.session_state.prediction_result
    input_data = st.session_state.input_data
    
    st.markdown("---")
    st.header("Prediction Results")
 
    # Use columns for a cleaner layout
    col1, col2 = st.columns([2, 3])
 
    with col1:
        # Display the probability as a metric
        st.metric(
            label="Probability of Life",
            value=f"{prediction['probability']:.0%}",
        )

        # Display the visualization
        st.subheader("Visualization")
        fig = utils.generate_visualization(prediction)
        st.pyplot(fig)

    with col2:
        st.subheader("Interactive Planet Model")
        globe_fig = utils.generate_3d_globe(input_data)
        st.plotly_chart(globe_fig, use_container_width=True)

    # Display the reasoning below the columns to use the full width
    st.subheader("Reasoning Breakdown")
    st.info(prediction['description'])

# --- Disclaimer ---
st.markdown("---")
st.info(
    "**Disclaimer:** This is a hypothetical prediction based on a simplified AI model. "
    "The results are for entertainment and educational purposes only and do not represent "
    "actual scientific predictions."
)