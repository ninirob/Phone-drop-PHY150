# N Roberts
# PHY 150 Project Two

# Phone Drop Data Visual
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Constants
g = 9.8  # m/s^2 (acceleration due to gravity)

# Masses (in kg)
mass_phone_only = 0.176  # kg
mass_silicone = 0.224  # kg
mass_hard_plastic = 0.207  # kg
mass_rubber = 0.266  # kg

# Forces due to gravity (F = m * g)
F_gravity_phone_only = mass_phone_only * g
F_gravity_silicone = mass_silicone * g
F_gravity_hard_plastic = mass_hard_plastic * g
F_gravity_rubber = mass_rubber * g

# Impact forces (from prior calculations, in Newtons)
force_phone_only = 95.30
force_silicone = 24.29
force_hard_plastic = 37.40
force_rubber = 18.06

# Collision times (seconds)
collision_time_phone_only = 0.01
collision_time_silicone = 0.05
collision_time_hard_plastic = 0.03
collision_time_rubber = 0.08

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 8))

# Ground line
ax.axhline(0, color='black', linewidth=2)
ax.text(2.5, -0.1, 'Ground', color='black', fontsize=12, ha='center')

# Set axis limits
ax.set_ylim(-1, 2)
ax.set_xlim(-1, 6)

# Phone dimensions
phone_width = 0.3
phone_height = 0.05
drop_height = 1.5  # Drop height (meters)

# Positions for phones
phone_positions = [0.4, 1.6, 2.8, 4.0]
phone_colors = ['lightblue', 'lightgreen', 'orange', 'lightcoral']
phone_masses = [mass_phone_only, mass_silicone, mass_hard_plastic, mass_rubber]
impact_forces = [force_phone_only, force_silicone, force_hard_plastic, force_rubber]
gravity_forces = [F_gravity_phone_only, F_gravity_silicone, F_gravity_hard_plastic, F_gravity_rubber]
materials = ['Phone Only', 'Silicone', 'Hard Plastic', 'Rubber']

# Draw phones and forces
for x, color, mass, f_grav, f_impact, material in zip(phone_positions, phone_colors, phone_masses, gravity_forces, impact_forces, materials):
    # Draw phone
    ax.add_patch(patches.Rectangle((x, drop_height), phone_width, phone_height, color=color, zorder=5))
    ax.text(x + phone_width / 2, drop_height + 0.1, f'{material}\n{mass:.3f} kg', color='black', fontsize=10, ha='center')

    # Gravity force (falling)
    ax.arrow(x + phone_width / 2, drop_height, 0, -0.3, head_width=0.05, head_length=0.05, fc='blue', ec='blue', zorder=6)
    ax.text(x + phone_width / 2, drop_height - 0.4, f'F_gravity = {f_grav:.2f} N', color='blue', fontsize=10, ha='center')

    # Impact force at ground
    ax.arrow(x + phone_width / 2, 0, 0, 0.5, head_width=0.05, head_length=0.05, fc='red', ec='red', linestyle='dashed', zorder=7)
    ax.text(x + phone_width / 2, 0.6, f'F_impact = {f_impact:.2f} N', color='red', fontsize=10, ha='center')

# Dashed line for drop height reference
ax.axhline(drop_height, linestyle='dashed', color='gray', alpha=0.6)
ax.text(-0.9, drop_height + 0.04, f'Drop Height = {drop_height} m', fontsize=10, color='black')

# Labels and legend
ax.set_title('Phone Drop with Different Case Materials', fontsize=14)
ax.set_xlabel('Position (m)', fontsize=12)
ax.set_ylabel('Height (m)', fontsize=12)

# Legend
handles = [
    patches.Patch(color='lightblue', label='Phone Only'),
    patches.Patch(color='lightgreen', label='Silicone Case'),
    patches.Patch(color='orange', label='Hard Plastic Case'),
    patches.Patch(color='lightcoral', label='Rubber Case'),
    plt.Line2D([0], [0], color='blue', lw=2, label='F_gravity'),
    plt.Line2D([0], [0], color='red', lw=2, linestyle='dashed', label='F_impact')
]
ax.legend(handles=handles, loc='lower right', fontsize=10)

# Collision Time Bar Chart
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.bar(materials, [collision_time_phone_only, collision_time_silicone, collision_time_hard_plastic, collision_time_rubber], color=['lightblue', 'lightgreen', 'orange', 'lightcoral'])
ax2.set_title('Collision Time Comparison', fontsize=14)
ax2.set_xlabel('Material', fontsize=12)
ax2.set_ylabel('Collision Time (s)', fontsize=12)
ax2.set_ylim(0, 0.1)

# Show both plots
plt.show()