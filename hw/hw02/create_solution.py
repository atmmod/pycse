#!/usr/bin/env python3
"""
Script to create solution notebook with complete code implementations
"""

import json

# Read the solution notebook
with open('hw02_integration_and_odes_sol.ipynb', 'r') as f:
    nb = json.load(f)

# Solutions for each exercise
solutions = {
    'ex1a_code': '''# AI assistance: No

# Given parameters
U = 250  # W/(m^2·K)
D = 0.05  # m

# Measured data
x = np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0])  # m
deltaT = np.array([45.0, 38.5, 32.8, 27.5, 22.9, 18.5])  # K

# Calculate the integrand
integrand = U * np.pi * D * deltaT

# Calculate total heat transfer using trapezoid method
Q_total_trapz = np.trapz(integrand, x)

print(f"Total heat transfer (trapezoid method): {Q_total_trapz:.2f} W")''',

    'ex1b_code': '''# AI assistance: No

# Calculate cumulative heat transfer
from scipy.integrate import cumtrapz

integrand = U * np.pi * D * deltaT
Q_cumulative = cumtrapz(integrand, x, initial=0)

# Plot cumulative heat transfer
plt.figure(figsize=(8, 5))
plt.plot(x, Q_cumulative, 'b-o', linewidth=2, markersize=6)
plt.xlabel('Position along heat exchanger (m)', fontsize=12)
plt.ylabel('Cumulative heat transfer (W)', fontsize=12)
plt.title('Cumulative Heat Transfer Profile', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Heat transferred in first 6 m: {Q_cumulative[3]:.2f} W")''',

    'ex2a_code': '''# AI assistance: No

# Parameters
V = 100  # L
q = 10  # L/min
CA_in = 2.0  # mol/L
k = 0.15  # 1/min

# Define ODE function
def dCAdt(t, CA):
    """Derivative of concentration in CSTR"""
    CA_val = CA[0]  # Extract value from array
    dCA = (q/V) * (CA_in - CA_val) - k * CA_val
    return [dCA]

# Solve ODE
CA0 = [0.0]  # initial condition
tspan = (0, 60)
t_eval = np.linspace(0, 60, 100)

sol = solve_ivp(dCAdt, tspan, CA0, t_eval=t_eval, method='RK45')

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(sol.t, sol.y[0], 'b-', linewidth=2)
plt.xlabel('Time (min)', fontsize=12)
plt.ylabel('Concentration of A (mol/L)', fontsize=12)
plt.title('CSTR Concentration Dynamics', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Store final concentration for testing
CA_final = sol.y[0, -1]
print(f"Final concentration at t=60 min: {CA_final:.4f} mol/L")''',

    'ex2b_code': '''# AI assistance: No

# Calculate steady-state concentration
CA_ss = CA_in / (1 + k*V/q)
CA_target = 0.95 * CA_ss

print(f"Steady-state concentration: {CA_ss:.4f} mol/L")
print(f"Target concentration (95% of SS): {CA_target:.4f} mol/L")

# Define event function
def reach_target(t, CA):
    """Event when CA reaches target value"""
    return CA[0] - CA_target

reach_target.terminal = True  # Stop integration when event occurs
reach_target.direction = 1  # Only detect when crossing from below

# Solve with event
sol_event = solve_ivp(dCAdt, tspan, CA0, events=reach_target, dense_output=True)

# Extract time when target was reached
t_95 = sol_event.t_events[0][0]

print(f"Time to reach 95% of steady state: {t_95:.2f} min")''',

    'ex3a_code': '''# AI assistance: No

# Parameters
V1 = 500  # L
V2 = 800  # L
mu1 = 0.3  # 1/hr
mu2 = 0.1  # 1/hr
q1 = 0.05  # g/(g*hr)
q2 = 0.25  # g/(g*hr)
F_in = 50  # L/hr
F_12 = 50  # L/hr
F_out = 50  # L/hr
X_in = 1.0  # g/L
P_in = 0.0  # g/L

# Define system of ODEs
def dYdt(t, Y):
    """System of ODEs for two-tank bioreactor"""
    X1, P1, X2, P2 = Y

    # Tank 1 derivatives
    dX1dt = mu1*X1 + (F_in/V1)*(X_in - X1) - (F_12/V1)*X1
    dP1dt = q1*X1 + (F_in/V1)*(P_in - P1) - (F_12/V1)*P1

    # Tank 2 derivatives
    dX2dt = mu2*X2 + (F_12/V2)*(X1 - X2) - (F_out/V2)*X2
    dP2dt = q2*X2 + (F_12/V2)*(P1 - P2) - (F_out/V2)*P2

    return [dX1dt, dP1dt, dX2dt, dP2dt]

# Initial conditions: [X1, P1, X2, P2]
Y0 = [0.1, 0.1, 0.1, 0.1]
tspan = (0, 50)
t_eval = np.linspace(0, 50, 200)

# Solve system
sol_bioreactor = solve_ivp(dYdt, tspan, Y0, t_eval=t_eval, method='RK45')

# Extract solutions for easier plotting
t = sol_bioreactor.t
X1 = sol_bioreactor.y[0]
P1 = sol_bioreactor.y[1]
X2 = sol_bioreactor.y[2]
P2 = sol_bioreactor.y[3]

# Create plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot biomass concentrations
ax1.plot(t, X1, 'b-', linewidth=2, label='Tank 1 (X₁)')
ax1.plot(t, X2, 'r-', linewidth=2, label='Tank 2 (X₂)')
ax1.set_xlabel('Time (hr)', fontsize=11)
ax1.set_ylabel('Biomass Concentration (g/L)', fontsize=11)
ax1.set_title('Biomass Dynamics in Two-Tank System', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot product concentrations
ax2.plot(t, P1, 'b-', linewidth=2, label='Tank 1 (P₁)')
ax2.plot(t, P2, 'r-', linewidth=2, label='Tank 2 (P₂)')
ax2.set_xlabel('Time (hr)', fontsize=11)
ax2.set_ylabel('Product Concentration (g/L)', fontsize=11)
ax2.set_title('Product Dynamics in Two-Tank System', fontsize=12)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Store final values for testing
X1_final = X1[-1]
P2_final = P2[-1]
print(f"Final biomass in Tank 1: {X1_final:.4f} g/L")
print(f"Final product in Tank 2: {P2_final:.4f} g/L")''',

    'ex3b_code': '''# AI assistance: No

# Calculate product yield
product_yield = (F_out * P2_final) / (F_in * X_in)

print(f"Overall product yield: {product_yield:.4f} g product / g biomass input")''',

    'ex4a_code': '''# AI assistance: No

# Parameters
omega_n = 0.5  # rad/min
h0 = 20  # cm
v0 = 0  # cm/min

# Define ODE system
def dXdt(t, X, zeta):
    """Second-order damped oscillator as system of first-order ODEs"""
    h, v = X
    dhdt = v
    dvdt = -2*zeta*omega_n*v - omega_n**2*h
    return [dhdt, dvdt]

# Initial conditions
X0 = [h0, v0]
tspan = (0, 30)
t_eval = np.linspace(0, 30, 300)

# Solve for three damping ratios
zeta_values = [0.2, 1.0, 2.0]
labels = ['Underdamped (ζ=0.2)', 'Critically damped (ζ=1.0)', 'Overdamped (ζ=2.0)']
colors = ['blue', 'green', 'red']
linestyles = ['-', '--', '-.']

plt.figure(figsize=(10, 6))

for i, zeta in enumerate(zeta_values):
    # Solve ODE for this zeta value using lambda function
    sol = solve_ivp(lambda t, X: dXdt(t, X, zeta), tspan, X0, t_eval=t_eval, method='RK45')

    if zeta == 0.2:
        sol_underdamped = sol  # Save for testing

    # Plot h vs t
    plt.plot(sol.t, sol.y[0], color=colors[i], linestyle=linestyles[i],
             linewidth=2, label=labels[i])

# Add labels, legend, grid
plt.xlabel('Time (min)', fontsize=12)
plt.ylabel('Level Deviation from Setpoint (cm)', fontsize=12)
plt.title('Tank Level Control Response for Different Damping Ratios', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle=':', linewidth=1, alpha=0.5)
plt.tight_layout()
plt.show()

# For testing: get final value for underdamped case
h_final_underdamped = sol_underdamped.y[0, -1]
print(f"Final deviation (underdamped): {h_final_underdamped:.4f} cm")''',

    'ex4b_code': '''# AI assistance: No

# Define event function to detect maxima
def find_maximum(t, X, zeta):
    """Event when velocity crosses zero (dh/dt = 0)"""
    h, v = X
    return v

find_maximum.direction = -1  # Detect when v goes from positive to negative (maximum)

# Solve with event detection
zeta = 0.2
sol_events = solve_ivp(lambda t, X: dXdt(t, X, zeta), tspan, X0,
                       events=lambda t, X: find_maximum(t, X, zeta),
                       dense_output=True, max_step=0.1)

# Extract times of maxima
t_maxima = sol_events.t_events[0]
print(f"Times of maxima: {t_maxima}")

# Calculate periods between consecutive maxima
periods = np.diff(t_maxima)
oscillation_period = np.mean(periods)

print(f"\\nAverage oscillation period: {oscillation_period:.4f} min")

# Compare with theoretical value
theoretical_period = 2 * np.pi / (omega_n * np.sqrt(1 - zeta**2))
print(f"Theoretical period: {theoretical_period:.4f} min")
print(f"Percent error: {abs(oscillation_period - theoretical_period)/theoretical_period * 100:.2f}%")'''
}

# Update the cells with solutions
for cell in nb['cells']:
    cell_id = cell.get('id', '')
    if cell_id in solutions:
        if cell['cell_type'] == 'code':
            cell['source'] = solutions[cell_id]

# Write the solution notebook
with open('hw02_integration_and_odes_sol.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)

print("Solution notebook created successfully!")
