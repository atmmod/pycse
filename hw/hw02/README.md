# Homework 02: Integration and Differential Equations

## Overview

This homework covers numerical integration and solving ordinary differential equations (ODEs), based on material from lecture notebooks 02-05.

**Topics covered:**
- Numerical integration (trapezoid method, cumtrapz)
- First-order differential equations (solve_ivp)
- Systems of first-order ODEs
- Higher-order ODEs (converted to systems of first-order)
- Event detection

**Estimated completion time:** 3 hours for proficient students using AI assistance

**Total points:** 100 (4 exercises × 25 points each)

## Files

- `hw02_integration_and_odes.ipynb` - Student version (incomplete, for students to complete)
- `hw02_integration_and_odes_sol.ipynb` - Solution version (complete implementations)
- `tests/` - Otter-grader test files for autograding
- `otter_config.json` - Otter-grader configuration
- `autograder.zip` - Generated autograder for Gradescope

## Exercises

### Exercise 1: Heat Exchanger Energy Balance (25 pts)
**Topic:** Numerical integration

Students calculate total heat transfer in a counter-current heat exchanger using:
- Part A: Trapezoid method integration
- Part B: Cumulative heat transfer profile
- Part C: Reflection on measurement accuracy

**Key concepts:** Integration of experimental data, cumtrapz, visualization

---

### Exercise 2: CSTR with First-Order Reaction (25 pts)
**Topic:** First-order ODE with events

Students model a continuous stirred tank reactor:
- Part A: Solve ODE for concentration vs time
- Part B: Use event function to find time to 95% of steady state
- Part C: Reflection on process design trade-offs

**Key concepts:** solve_ivp, event functions, steady-state analysis

---

### Exercise 3: Two-Tank Bioreactor System (25 pts)
**Topic:** Systems of coupled ODEs

Students analyze a two-stage bioreactor for pharmaceutical production:
- Part A: Solve system of 4 coupled ODEs (biomass and product in 2 tanks)
- Part B: Calculate product yield
- Part C: Reflection on multi-stage bioprocessing

**Key concepts:** Coupled ODE systems, mass balances, process optimization

---

### Exercise 4: Damped Oscillations in Level Control (25 pts)
**Topic:** Higher-order ODEs

Students analyze tank level control dynamics:
- Part A: Convert 2nd-order ODE to system, solve for 3 damping ratios
- Part B: Detect oscillation period using events
- Part C: Reflection on control system design

**Key concepts:** 2nd-order ODEs, damped oscillations, control theory

## For Students

### Google Colab Setup

1. Upload the notebook to Google Colab
2. Run the setup cells to install required packages
3. Work through each exercise
4. Run test cells to check your work
5. Download and submit to Gradescope

### Required Libraries

- numpy
- scipy (integrate module)
- matplotlib
- otter-grader

## For Instructors

### Gradescope Setup

1. Create new Programming Assignment in Gradescope
2. Upload `autograder.zip`
3. Configure autograder settings:
   - Language: Python
   - Timeout: 300 seconds (5 minutes)
   - Total points: 100

### Grading Breakdown

Each exercise:
- Autograded code: 18 points
- Manual grading (reflections): 7 points

### Regenerating Autograder

If you modify the solution notebook or tests:

```bash
cd hw/hw02
otter generate autograder -c otter_config.json -t tests
```

This will regenerate `autograder.zip`

## Learning Objectives

After completing this homework, students will be able to:

1. Apply numerical integration methods to engineering data
2. Set up and solve first-order ODEs using solve_ivp
3. Formulate and solve systems of coupled differential equations
4. Convert higher-order ODEs to systems of first-order ODEs
5. Use event functions to detect specific conditions during integration
6. Interpret numerical solutions in the context of chemical engineering processes
7. Critically analyze trade-offs in process design and control

## Engineering Applications

This homework emphasizes real chemical and biomolecular engineering applications:

- **Heat exchanger design** - Thermal energy balance
- **Chemical reactor modeling** - CSTR dynamics and startup
- **Bioprocess engineering** - Two-stage bioreactor optimization
- **Process control** - Tank level control and damping

## Notes

- Students are encouraged to use AI tools but must understand all code
- Reflection questions must be answered independently (not using AI)
- Solutions use chemical engineering notation and units throughout
- All problems are based on realistic engineering scenarios
