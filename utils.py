 import matplotlib.pyplot as plt
 import numpy as np
 
 def prepare_input_data(elements, temperature, pressure, has_water):
     """
     Prepares the input data for the AI model.  This is a placeholder;
     you'll need to adapt this to your specific model's requirements.
     """
     # Create a dictionary to represent the input data
     input_data = {
         "elements": elements,
         "temperature": temperature,
         "pressure": pressure,
         "has_water": has_water
     }
     return input_data
 
 def generate_visualization(prediction):
     """
     Generates a simple bar chart visualization of the prediction.
     Again, this is a placeholder.  You can create more sophisticated
     visualizations based on your data and model.
     """
     # Create a bar chart
     fig, ax = plt.subplots()
     ax.bar(["Life Probability"], [prediction["probability"]])
     ax.set_ylim(0, 1)  # Probability between 0 and 1
     ax.set_ylabel("Probability")
     ax.set_title("Life Prediction")
     return fig