# Homework 02: Integration and ODEs - Assignment Summary

## Created Files

### Main Assignment Files
- **hw02_integration_and_odes.ipynb** - Student version (to distribute to students)
- **hw02_integration_and_odes_sol.ipynb** - Instructor solution version (with complete code)
- **README.md** - Complete documentation for students and instructors

### Autograding Files
- **autograder.zip** - Upload this to Gradescope for automatic grading
- **otter_config.json** - Otter-grader configuration
- **tests/** - Directory containing 8 test files (ex1a.py through ex4b.py)
- **create_solution.py** - Script used to generate solution notebook

## Assignment Structure

### Exercise 1: Heat Exchanger Energy Balance (25 points)
**Learning objectives:** Numerical integration, trapezoid method, cumulative integration

**Chemical Engineering Application:** Counter-current heat exchanger design
- Given temperature difference data at 6 positions along 10m exchanger
- Calculate total heat transfer using np.trapz
- Compute cumulative heat transfer profile using cumtrapz
- Plot and analyze results

**Autograded parts:**
- ex1a (10 pts): Calculate Q_total_trapz using trapezoid integration
- ex1b (8 pts): Calculate Q_cumulative array and create plot

**Manual grading:**
- Part C (7 pts): Reflection on measurement accuracy and data density

---

### Exercise 2: CSTR with First-Order Reaction (25 points)
**Learning objectives:** First-order ODEs, solve_ivp, event functions

**Chemical Engineering Application:** Continuous stirred tank reactor startup
- Model mole balance: dCA/dt = (q/V)(CA_in - CA) - k*CA
- Solve from startup (CA=0) to quasi-steady state
- Find time to reach 95% of steady state using events

**Autograded parts:**
- ex2a (12 pts): Implement dCAdt function and solve ODE, plot results
- ex2b (6 pts): Use event function to find t_95

**Manual grading:**
- Part C (7 pts): Reflection on flow rate effects and process startup

---

### Exercise 3: Two-Tank Bioreactor System (25 points)
**Learning objectives:** Systems of coupled ODEs, bioprocess modeling

**Chemical Engineering Application:** Two-stage pharmaceutical bioreactor
- Tank 1: Growth phase (high μ, low q)
- Tank 2: Production phase (low μ, high q)
- 4 coupled ODEs for biomass (X) and product (P) in each tank
- Analyze steady-state concentrations and product yield

**Autograded parts:**
- ex3a (15 pts): Implement dYdt system, solve 4 coupled ODEs, create 2 subplots
- ex3b (3 pts): Calculate product_yield = (F_out * P2) / (F_in * X_in)

**Manual grading:**
- Part C (7 pts): Reflection on two-stage vs single-stage design

---

### Exercise 4: Damped Oscillations in Level Control (25 points)
**Learning objectives:** Higher-order ODEs, control systems, oscillation analysis

**Chemical Engineering Application:** Tank level control system dynamics
- 2nd-order ODE: d²h/dt² + 2ζωₙ(dh/dt) + ωₙ²h = 0
- Convert to system of 1st-order ODEs
- Compare underdamped (ζ=0.2), critically damped (ζ=1.0), overdamped (ζ=2.0)
- Detect oscillation period using event functions

**Autograded parts:**
- ex4a (12 pts): Implement dXdt, solve for 3 damping ratios, plot all on same graph
- ex4b (6 pts): Use event detection to find oscillation period

**Manual grading:**
- Part C (7 pts): Reflection on control system design choices

---

## Points Distribution

| Exercise | Code (Auto) | Reflection (Manual) | Total |
|----------|-------------|---------------------|-------|
| 1 | 18 | 7 | 25 |
| 2 | 18 | 7 | 25 |
| 3 | 18 | 7 | 25 |
| 4 | 18 | 7 | 25 |
| **Total** | **72** | **28** | **100** |

## Topics Covered (From Lectures 02-05)

### From Lecture 02 (Integration)
- numpy.trapz for integrating data
- scipy.integrate.cumtrapz for cumulative integration
- scipy.integrate.quad for function integration
- Applications to engineering calculations (heat transfer, reactor volumes)

### From Lecture 03 (First-Order ODEs - Part 1)
- solve_ivp for solving ODEs
- Dense output and evaluation points (t_eval)
- Event functions for detecting conditions
- Terminal events to stop integration

### From Lecture 04 (First-Order ODEs - Part 2)
- Systems of coupled first-order ODEs
- Tank mixing problems with multiple tanks
- Plotting multiple solutions
- Phase portraits and direction fields

### From Lecture 05 (Nth-Order ODEs)
- Converting 2nd-order ODEs to systems of 1st-order
- Damped harmonic oscillator
- Event detection for finding maxima/minima
- Comparing solutions with different parameters

## Key Features

### 1. Chemical Engineering Focus
All problems use realistic ChemE/BioE applications:
- Heat exchanger design (mass & energy balances)
- Chemical reactor modeling (kinetics, residence time)
- Bioprocess engineering (cell growth, product formation)
- Process control (level control, damping)

### 2. Progressive Difficulty
- Ex1: Straightforward integration of data
- Ex2: Single ODE with events
- Ex3: System of 4 coupled ODEs
- Ex4: Higher-order ODE with parameter studies

### 3. AI-Assisted Learning
- Students encouraged to use AI tools
- Must document AI usage
- Must understand all code
- Reflections require independent critical thinking

### 4. Comprehensive Assessment
- Autograded coding (72 pts)
- Manual graded reflections (28 pts)
- Tests both technical skills and conceptual understanding

## Gradescope Setup Instructions

1. Log in to Gradescope
2. Create new "Programming Assignment"
3. Name: "HW02: Integration and ODEs"
4. Upload `autograder.zip`
5. Set configuration:
   - Base image: Python
   - Timeout: 300 seconds
   - Total points: 100
6. Test with solution notebook
7. Release to students

## Student Instructions

1. Download `hw02_integration_and_odes.ipynb`
2. Open in Google Colab
3. Run setup cells to install packages
4. Complete all TODO sections
5. Run test cells to verify work
6. Answer reflection questions (no AI)
7. Document AI usage
8. Download .ipynb file
9. Upload to Gradescope

## Expected Completion Time

- Proficient student with AI: **3 hours**
  - Ex1: 30 min
  - Ex2: 45 min
  - Ex3: 60 min
  - Ex4: 45 min

- Struggling student: **4-5 hours**
- Advanced student: **2 hours**

## Common Issues & Solutions

### Issue: Students forget to define arrays as numpy arrays
**Solution:** Tests check `isinstance(x, np.ndarray)`

### Issue: Students don't extract values from arrays in ODE functions
**Solution:** Examples show proper extraction (e.g., `CA_val = CA[0]`)

### Issue: Event functions not working
**Solution:** Tests verify direction attribute is set

### Issue: Plots not showing proper labels
**Solution:** Tests are lenient on plotting; manual grading checks visualization

## Regenerating Materials

If you need to modify and regenerate:

```bash
# 1. Edit hw02_integration_and_odes_sol.ipynb
# 2. Update tests in tests/ directory if needed
# 3. Regenerate autograder:
cd hw/hw02
otter generate autograder -c otter_config.json -t tests
# 4. Upload new autograder.zip to Gradescope
```

## Files NOT to Distribute to Students

- hw02_integration_and_odes_sol.ipynb (instructor only)
- create_solution.py (helper script)
- autograder/ directory (generated)
- student/ directory (generated)

## Files to Distribute to Students

- hw02_integration_and_odes.ipynb (main assignment)
- README.md (optional, for reference)
