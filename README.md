# Elemental Life Prediction 🌌

This project is a web application built with Streamlit that predicts the probability of life on a hypothetical planet. Users can input various planetary conditions, and a simplified AI model provides a prediction and a basic visualization.

## ✨ Features

- **Interactive Web Interface**: A user-friendly interface built with Streamlit.
- **Custom Planet Configuration**: Input elemental composition, temperature, pressure, and the presence of water.
- **AI-Powered Predictions**: Utilizes a model to predict the probability of life based on the inputs.
- **Simple Visualization**: Displays the prediction as a clear bar chart.

## 🚀 How to Run

To get the application running on your local machine, follow these steps.

### Prerequisites

- Python 3.8+
- Conda

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/DakshGIIS/HackathonGIIS2025.git
    cd HackathonGIIS2025
    ```

2.  **Create and activate a Conda environment (recommended):**
    ```bash
    # Create a new conda environment (you can replace 'elemental-life' with your preferred name)
    conda create --name elemental-life python=3.9 -y
    
    # Activate the environment
    conda activate elemental-life
    ```

3.  **Install the required dependencies:**
    *(Note: You should create a `requirements.txt` file for this project)*
    ```bash
    pip install streamlit numpy matplotlib plotly
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run streamlit_app.py
    ```

    The application should now be open in your web browser!

## 📂 File Structure

```
├── streamlit_app.py    # Main Streamlit application file (UI)
├── model.py            # Contains the AI model for making predictions
├── utils.py            # Helper functions for data prep and visualization
└── README.md           # This file
```

## Disclaimer

This is a hypothetical prediction based on a simplified AI model. The results are for entertainment and educational purposes only and do not represent actual scientific predictions.