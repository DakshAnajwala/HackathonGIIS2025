import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

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

def generate_3d_globe(input_data):
    """
    Generates an interactive 3D globe of the planet using Plotly.
    The planet's color and clouds are determined by the input data.
    """
    # Determine planet color based on conditions
    if not input_data['has_water']:
        planet_color = 'sandybrown' if input_data['temperature'] < 150 else 'darkred'
    else:
        planet_color = 'deepskyblue' if input_data['temperature'] > 0 else 'whitesmoke'

    # Generate sphere coordinates
    N = 100
    phi = np.linspace(0, 2 * np.pi, N)
    theta = np.linspace(0, np.pi, N)
    phi, theta = np.meshgrid(phi, theta)

    r_planet = 10
    x_planet = r_planet * np.cos(phi) * np.sin(theta)
    y_planet = r_planet * np.sin(phi) * np.sin(theta)
    z_planet = r_planet * np.cos(theta)

    # Create the planet surface using go.Surface for a solid look
    planet_surface = go.Surface(
        x=x_planet, y=y_planet, z=z_planet,
        colorscale=[[0, planet_color], [1, planet_color]], # Uniform color
        showscale=False,
        cmin=0, cmax=1,
        opacity=1.0,
        name="Planet Surface"
    )

    # Create a patchy cloud layer if conditions are right (not too hot)
    data = [planet_surface]
    if input_data['temperature'] < 80:
        r_clouds = 10.2
        x_clouds = r_clouds * np.cos(phi) * np.sin(theta)
        y_clouds = r_clouds * np.sin(phi) * np.sin(theta)
        z_clouds = r_clouds * np.cos(theta)
        
        # Use a procedural texture for patchy clouds
        cloud_texture = (np.sin(3 * phi) * np.cos(6 * theta))**2
        
        cloud_surface = go.Surface(
            x=x_clouds, y=y_clouds, z=z_clouds,
            surfacecolor=cloud_texture,
            colorscale=[[0, 'rgba(0,0,0,0)'], [0.5, 'rgba(0,0,0,0)'], [1, 'white']], # Mostly transparent
            showscale=False,
            cmin=0, cmax=1,
            opacity=0.5,
            name="Clouds"
        )
        data.append(cloud_surface)

    fig = go.Figure(data=data)

    # Configure layout for a clean "outer space" look
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='black'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
    return fig
