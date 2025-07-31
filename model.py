import random

def predict_life(input_data):
    """
    A simplified placeholder AI model to predict the probability of life.

    This model uses a basic rule-based system based on a few key factors
    for life as we know it.

    Args:
        input_data (dict): A dictionary containing planet parameters.

    Returns:
        dict: A dictionary with 'probability' and 'description' of life.
    """
    probability = 0.0
    description_parts = []

    # Extract data from the input dictionary
    elements = set(e.strip().upper() for e in input_data["elements"])
    temperature = input_data["temperature"]
    has_water = input_data["has_water"]

    # Rule 1: Presence of water is crucial
    if has_water:
        probability += 0.4
        description_parts.append("Water is present, a key ingredient for life.")
    else:
        return {
            "probability": 0.01,
            "description": "No liquid water detected, making carbon-based life highly unlikely."
        }

    # Rule 2: Check for essential elements (Carbon, Hydrogen, Oxygen, Nitrogen)
    if {'C', 'H', 'O', 'N'}.issubset(elements):
        probability += 0.4
        description_parts.append("The core elements for organic chemistry (C, H, O, N) are available.")

    # Rule 3: Check for a habitable temperature range
    if 0 <= temperature <= 100:
        probability += 0.2
        description_parts.append("The temperature is in a favorable range for complex organic molecules.")

    # Clamp probability between 0 and 1
    probability = max(0, min(1, probability))

    return {
        "probability": probability,
        "description": " ".join(description_parts) or "Conditions are not favorable for life."
    }