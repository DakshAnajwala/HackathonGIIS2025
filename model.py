import numpy as np

def predict_life(input_data, event=None):
    """
    A more sophisticated model to predict the probability of life.

    This model calculates a base potential from available building blocks
    and then modulates it with environmental factors like temperature and pressure.

    Args:
        input_data (dict): A dictionary containing planet parameters.
        event (str, optional): A catastrophic event to apply. Defaults to None.

    Returns:
        dict: A dictionary with 'probability' and 'description' of life.
    """
    description_parts = []

    # Extract data from the input dictionary
    elements = set(e.strip().upper() for e in input_data["elements"])
    temperature = input_data["temperature"]
    pressure = input_data["pressure"]
    has_water = input_data["has_water"]

    # --- Step 1: Assess fundamental prerequisites ---

    # Water is a non-negotiable prerequisite for life as we know it.
    if not has_water:
        return {
            "probability": 0.01,
            "description": "❌ No liquid water detected. This is a major barrier for carbon-based life."
        }

    # Base probability starts high if water is present.
    base_probability = 0.5
    description_parts.append("✅ Liquid water is present, a universal solvent and key for known biological processes.")

    # Check for essential elements
    if {'C', 'H', 'O', 'N'}.issubset(elements):
        base_probability += 0.4  # Max potential requires CHON
        description_parts.append("✅ The core 'CHON' elements for organic chemistry are available.")
    else:
        base_probability -= 0.3  # Significantly reduce potential without CHON
        description_parts.append("❌ Missing one or more of the core 'CHON' elements, hindering the formation of complex organic molecules.")

    # Bonus for secondary elements
    if {'P', 'S'}.issubset(elements):
        base_probability += 0.1
        description_parts.append("✅ Key secondary elements (P, S) are present, vital for DNA and proteins.")

    # Clamp base probability between 0 and 1
    base_probability = max(0, min(1, base_probability))

    # --- Step 2: Apply environmental multipliers ---

    # Temperature Factor (using a Gaussian curve for a smooth falloff)
    # Optimal temperature around 25°C, with a standard deviation of 50°C.
    optimal_temp = 25
    temp_std_dev = 50
    temp_factor = np.exp(-0.5 * ((temperature - optimal_temp) / temp_std_dev) ** 2)

    if temp_factor > 0.9:
        description_parts.append(f"✅ Temperature ({temperature}°C) is in the optimal range for complex life.")
    elif temp_factor > 0.3:
        description_parts.append(f"⚠️ Temperature ({temperature}°C) is outside the optimal range, but could support extremophiles.")
    else:
        description_parts.append(f"❌ Temperature ({temperature}°C) is extreme, severely limiting the possibility of life.")

    # Pressure Factor
    pressure_factor = 1.0
    if 0.5 <= pressure <= 10:
        description_parts.append(f"✅ Atmospheric pressure ({pressure} atm) is suitable for maintaining liquid water and stable conditions.")
    elif pressure > 10:
        pressure_factor = 0.6  # Significant penalty for non-ideal pressure
        description_parts.append(f"⚠️ High atmospheric pressure ({pressure} atm) poses significant challenges for complex life.")
    else:  # pressure < 0.5
        pressure_factor = 0.6  # Significant penalty for non-ideal pressure
        description_parts.append(f"⚠️ Low atmospheric pressure ({pressure} atm) makes it difficult to maintain liquid water on the surface.")

    # --- Step 3: Calculate final probability ---
    final_probability = base_probability * temp_factor * pressure_factor

    # --- Step 4: Apply one-time event modifiers ---
    if event:
        event_description = ""
        if event == "Asteroid Impact":
            final_probability *= 0.1  # 90% reduction
            event_description = "💥 An asteroid impact has likely caused a mass extinction event, devastating the biosphere."
        elif event == "Pandemic Outbreak":
            # A pandemic is only devastating if there's complex life to infect
            if final_probability > 0.2:
                final_probability *= 0.3  # 70% reduction
                event_description = "🦠 A virulent pandemic is sweeping the planet, causing an ecosystem collapse."
            else:
                event_description = "🦠 A pandemic was introduced, but found no complex life to infect."
        elif event == "Super-Volcano Eruption":
            final_probability *= 0.5  # 50% reduction
            event_description = "🌋 A super-volcano has erupted, blanketing the atmosphere in ash and triggering a volcanic winter."

        if event_description:
            description_parts.append(event_description)

    # Join the reasoning parts into a single string, separated by newlines for readability
    final_description = "\n\n".join(description_parts)

    return {
        "probability": final_probability,
        "description": final_description or "Conditions are not favorable for life."
    }