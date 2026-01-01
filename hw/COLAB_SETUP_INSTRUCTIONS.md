# Google Colab Setup Instructions for hw01_python_fundamentals.ipynb

## Overview
This homework notebook uses **otter-grader** for automated testing and grading. To use it in Google Colab, you need to upload both the notebook and the tests directory to your Google Drive.

## Setup Steps

### 1. Upload Files to Google Drive

1. Download or clone this entire `hw` folder to your computer
2. Open Google Drive (drive.google.com)
3. Create a folder structure in your Google Drive. For example:
   - `My Drive/CHBE2250/hw/`
4. Upload the following to this folder:
   - `hw01_python_fundamentals.ipynb` (the homework notebook)
   - `tests/` folder (contains all the test files: ex1a.py, ex1b.py, etc.)

Your Google Drive structure should look like:
```
My Drive/
  └── CHBE2250/  (or your course folder name)
      └── hw/
          ├── hw01_python_fundamentals.ipynb
          └── tests/
              ├── ex1a.py
              ├── ex1b.py
              ├── ex2a.py
              ├── ex2b.py
              ├── ex3a.py
              ├── ex3b.py
              ├── ex4a.py
              └── ex4b.py
```

### 2. Open the Notebook in Google Colab

1. In Google Drive, navigate to the folder containing your notebook
2. Double-click `hw01_python_fundamentals.ipynb`
3. If prompted, select "Open with Google Colaboratory"
4. If you don't see this option, right-click the file → "Open with" → "Google Colaboratory"

### 3. Configure the Tests Path

1. **Run the first code cell** (the Google Drive mount cell)
2. Click the authorization link that appears
3. Sign in with your Google account and authorize Colab to access your Drive
4. **Important:** Update the `tests_path` variable in the first cell to match your Google Drive structure

   For example, if you uploaded to `My Drive/CHBE2250/hw/tests`, change:
   ```python
   tests_path = '/content/drive/MyDrive/hw/tests'
   ```
   to:
   ```python
   tests_path = '/content/drive/MyDrive/CHBE2250/hw/tests'
   ```

5. Run the cell again to verify the tests directory is found

### 4. Run the Setup Cell

1. **Run the second code cell** (otter-grader setup)
2. This will install otter-grader and initialize it with your tests
3. You should see: `✓ Otter-grader initialized with tests from: /content/drive/MyDrive/.../tests`

### 5. Complete Your Homework

Now you can work through the exercises! After completing each exercise:

1. Write your code in the provided code cells
2. Run the TEST CELL to check your work
3. The test will show ✓ if correct or provide error messages if something needs fixing
4. You can run the test cells as many times as you need

### 6. Generate Your Submission

When you've completed all exercises:

1. Scroll to the bottom of the notebook
2. Run the final submission cell
3. Download the generated zip file
4. Submit the zip file according to your instructor's instructions

## Troubleshooting

### "Tests directory not found"
- Make sure you uploaded the `tests` folder to Google Drive
- Check that the `tests_path` variable matches your actual Google Drive folder structure
- Remember that Google Drive folder names are case-sensitive

### "Module 'otter' not found"
- Make sure you ran the setup cell (second code cell)
- If it still doesn't work, try restarting the runtime: Runtime → Restart runtime

### Test files not loading
- Verify that all 8 test files (ex1a.py through ex4b.py) are in the tests folder
- Make sure the tests folder is in the same parent directory as the notebook
- Check that you granted Colab permission to access your Google Drive

### Permission errors
- Re-run the Google Drive mount cell
- Make sure you authorized Colab to access your Drive
- Try disconnecting and reconnecting to the runtime

## Tips

- Save your work frequently (File → Save or Ctrl+S / Cmd+S)
- You can run cells in any order, but it's best to run them top-to-bottom
- If something goes wrong, try: Runtime → Restart runtime and run all
- The notebook autosaves to your Google Drive every few minutes
- You can work on this from any computer by opening it from Google Drive

## Questions?

If you encounter issues not covered here, please:
1. Check the error message carefully
2. Make sure all setup cells ran successfully
3. Verify your Google Drive folder structure
4. Ask your instructor or TA for help
