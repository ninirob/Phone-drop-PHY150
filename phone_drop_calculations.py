# N Roberts
# PHY 150 Project Two

# Phone Drop Calculations
import math

# Constants
g = 9.8  # m/s^2 (acceleration due to gravity)
h = 1.5  # m (height of the drop)

# Convert masses from oz to kg
oz_to_kg = 0.0283495  # conversion factor from ounces to kilograms

# Masses in oz and converted to kg
mass_phone_only = 6.2 * oz_to_kg  # kg (phone only)
mass_silicone = (6.2 + 1.7) * oz_to_kg  # kg (phone + silicone case)
mass_hard_plastic = (6.2 + 1.1) * oz_to_kg  # kg (phone + hard plastic case)
mass_rubber = (6.2 + 3.2) * oz_to_kg  # kg (phone + rubber case)

# Collision times (in seconds)
collision_time_phone_only = 0.01  # seconds
collision_time_silicone = 0.05  # seconds
collision_time_hard_plastic = 0.03  # seconds
collision_time_rubber = 0.08  # seconds

# Function to calculate velocity before impact (v = sqrt(2gh))
def calculate_velocity(g, h):
    return math.sqrt(2 * g * h)

# Function to calculate deceleration (a = v / t)
def calculate_deceleration(v, t):
    return v / t

# Function to calculate force of impact (F = m * a)
def calculate_impact_force(m, a):
    return m * a

# Function to calculate time of flight (t = sqrt(2h / g))
def calculate_time_of_flight(h, g):
    return math.sqrt(2 * h / g)

# Calculate velocity before impact for all cases
v = calculate_velocity(g, h)

# Calculate time of flight
time_of_flight = calculate_time_of_flight(h, g)

# Calculate deceleration for each case (using the provided collision times)
a_phone_only = calculate_deceleration(v, collision_time_phone_only)
a_silicone = calculate_deceleration(v, collision_time_silicone)
a_hard_plastic = calculate_deceleration(v, collision_time_hard_plastic)
a_rubber = calculate_deceleration(v, collision_time_rubber)

# Calculate force of impact for each case
F_phone_only = calculate_impact_force(mass_phone_only, a_phone_only)
F_silicone = calculate_impact_force(mass_silicone, a_silicone)
F_hard_plastic = calculate_impact_force(mass_hard_plastic, a_hard_plastic)
F_rubber = calculate_impact_force(mass_rubber, a_rubber)

# Print the results
print(f"Phone without case (mass = {mass_phone_only:.3f} kg):")
print(f"Velocity before impact: {v:.2f} m/s")
print(f"Deceleration: {a_phone_only:.2f} m/s^2")
print(f"Force of impact: {F_phone_only:.2f} N")
print("\n")

print(f"Phone with silicone case (mass = {mass_silicone:.3f} kg):")
print(f"Velocity before impact: {v:.2f} m/s")
print(f"Deceleration: {a_silicone:.2f} m/s^2")
print(f"Force of impact: {F_silicone:.2f} N")
print("\n")

print(f"Phone with hard plastic case (mass = {mass_hard_plastic:.3f} kg):")
print(f"Velocity before impact: {v:.2f} m/s")
print(f"Deceleration: {a_hard_plastic:.2f} m/s^2")
print(f"Force of impact: {F_hard_plastic:.2f} N")
print("\n")

print(f"Phone with rubber case (mass = {mass_rubber:.3f} kg):")
print(f"Velocity before impact: {v:.2f} m/s")
print(f"Deceleration: {a_rubber:.2f} m/s^2")
print(f"Force of impact: {F_rubber:.2f} N")

# Print time of flight for all cases
print(f"\nTime of flight (for all cases): {time_of_flight:.2f} seconds")