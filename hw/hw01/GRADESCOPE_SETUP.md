# Gradescope Autograder Setup for HW01

This directory contains the necessary files for setting up autograding on Gradescope for `hw01_python_fundamentals.ipynb`.

## Files Created

1. **`autograder.zip`** - The main file to upload to Gradescope
   - Contains all test files from the `tests/` directory
   - Includes otter-grader configuration
   - Includes requirements for the autograding environment

2. **`otter_config.json`** - Otter-grader configuration file
   - Accepts any `.ipynb` file (`"notebook": "*.ipynb"`)
   - Configured for direct notebook submission (`"zips": false`)
   - Sets up Gradescope-specific settings
   - Configures points and display options

3. **`requirements.txt`** - Python package requirements
   - Lists required packages (otter-grader, numpy, matplotlib)
   - Used by Gradescope to set up the autograding environment

## How to Set Up on Gradescope

1. Go to your Gradescope course
2. Create a new Programming Assignment
3. Configure the assignment:
   - Assignment Name: "Homework 1: Python Fundamentals"
   - Total Points: 100
   - Upload `autograder.zip` as the autograder
4. Set the submission format to accept `.ipynb` files
5. Configure any additional settings (due date, late policy, etc.)

## Test Files Included

The autograder includes tests for:
- **ex1a** (12 points) - Gas law calculations function
- **ex1b** (6 points) - Array operations with temperatures
- **ex2a** (12 points) - Heat capacity calculation function
- **ex3a** (12 points) - Dilution calculator with flexible parameters
- **ex3b** (6 points) - Serial dilution analysis
- **ex4a** (10 points) - Time-dependent concentration calculations

**Note:** Reflection questions (Part C of each exercise) are not auto-graded and must be manually graded on Gradescope.

## Regenerating the Autograder Zip

If you need to update the autograder (e.g., after modifying test files):

```bash
cd hw/
otter generate -t tests/ -o autograder.zip -c otter_config.json -r requirements.txt
```

## Manual Grading Components

The following components require manual grading (total: 40 points):
- Exercise 1, Part C: Critical reflection (7 points)
- Exercise 2, Part C: Critical reflection (7 points)
- Exercise 3, Part C: Critical reflection (7 points)
- Exercise 4, Part C: Critical reflection (7 points)
- Exercise 2, Part B: Plotting (6 points)
- Exercise 4, Part B: Multi-line plotting (8 points)
- AI Usage Documentation (not graded, but required)

Set up manual grading rubrics on Gradescope for these components.

## Student Submission Process

Students should:
1. Complete the notebook in Google Colab or Jupyter
2. Run all cells to ensure tests pass
3. Download the `.ipynb` file (File > Download > Download .ipynb)
4. Upload the `.ipynb` file directly to Gradescope

**Important:** Students submit the `.ipynb` file directly, NOT a zip file. The autograder is configured to accept notebook files with `"zips": false` in the configuration.

The autograder will automatically run the test cases and assign points for the auto-graded portions.
