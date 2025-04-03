# READ ME - Physics 150 Project: Phone Drop Simulation with Different Case Materials
## Files:
- phone_drop_calculations.py
  - For equation and data calculations
- phone_drop_diagram.py
  - For diagrams to analyze data for which phone case is best for protection

## Setup and Requirements
	1.Python Version: Ensure you have Python 3.x installed.
	2.Libraries: The following libraries are required:
	•matplotlib for plotting graphs and visualizations.
    •You can install the required libraries using:
`pip install matplotlib`

    3.	Running the Code:
	•	Save the code as phone_drop_simulation.py and run it in your Python environment.
    Example Output:
    The console output will display the velocity before impact, deceleration, and impact force for each case material. The graphical output will show the phone drop simulation and a collision time comparison bar chart.
   
# Overview
This project simulates the physics of a phone dropping from a height of 1.5 meters with different case materials: 
phone only, silicone, hard plastic, and rubber. 
The simulation calculates: 
- the velocity just before impact 
- deceleration upon hitting the ground
- the impact force 
- the collision time for each material

The data is visualized through graphical plots, including the forces at play and a bar chart comparing collision times.
To determine which phone case is best for protection.

# Project Details
## Constants

- Acceleration due to gravity: `g = 9.8 m/s²`
- Height of the drop: `h = 1.5 m`

## Calculations

### 1. **Velocity before Impact**
The velocity before impact is calculated using the following formula derived from the kinematic equations of motion:

v = \sqrt{2gh}

Where:
- `g = 9.8 m/s²` (acceleration due to gravity)
- `h = 1.5 m` (height of the drop)

### 2. **Deceleration**
The deceleration for each phone (depending on the collision time) is calculated using the following equation:

a = \frac{v}{t}

Where:
- `v` is the velocity before impact
- `t` is the collision time

### 3. **Force of Impact**
The force of impact is calculated using Newton's second law:
F = ma

Where:
- `m` is the mass of the object (in kg)
- `a` is the deceleration (in m/s²)

### 4. **Time of Flight**
The time of flight is the time it takes for the object to fall, and it's calculated using:

t = \sqrt{\frac{2h}{g}} 

Where:
- `h = 1.5 m` (height)
- `g = 9.8 m/s²` (acceleration due to gravity)

## Results

For each material, the velocity before impact, deceleration, and force of impact are calculated as follows:

### Phone Only:
- Mass = `0.176 kg`
- Force of impact: `95.30 N`

### Silicone Case:
- Mass = `0.224 kg`
- Force of impact: `24.29 N`

### Hard Plastic Case:
- Mass = `0.207 kg`
- Force of impact: `37.40 N`

### Rubber Case:
- Mass = `0.266 kg`
- Force of impact: `18.06 N`

The time of flight for all cases is `0.553 s`.

### Impact Forces

- **Gravity Force**: This is the force acting due to gravity.
- **Impact Force**: This is the force experienced when the phone hits the ground.

### Collision Times
The bar chart shown after running the phone_drop_diagram.py code, compares the collision times for different materials.
