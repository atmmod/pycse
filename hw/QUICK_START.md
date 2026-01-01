# Quick Start Guide - hw01_python_fundamentals with Otter-Grader

## For Students

### Setup (5 minutes)

1. **Upload to Google Drive**:
   ```
   My Drive/
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

2. **Open in Colab**:
   - Go to Google Drive
   - Right-click `hw01_python_fundamentals.ipynb`
   - Select "Open with" → "Google Colaboratory"

3. **Run Setup Cells**:
   - **Cell 1** (Drive mount): Authorize and update `tests_path` if needed
   - **Cell 2** (Otter setup): Wait for installation

4. **Start Working**:
   - Complete exercises
   - Run test cells to check work
   - Get instant feedback!

### Working on Homework

```python
# 1. Write your code
def calculate_pressure(V, n, T):
    R = 0.08206
    return (n * R * T) / V

# 2. Run the test cell
# ✓ All tests passed for Exercise 1a!

# 3. Move to next exercise
```

### Submit

Run the final cell to:
- Check all your tests
- Generate submission zip
- Download and submit

---

## For Instructors

### What Was Implemented

✅ Google Drive mount cell for test file access
✅ Otter-grader setup with Drive integration
✅ 8 test files (72 auto-graded points)
✅ Student setup instructions
✅ Complete documentation

### Files Created

```
hw/
├── hw01_python_fundamentals.ipynb       # Main notebook (modified)
├── tests/                                # New test directory
│   └── ex*.py (8 files)                 # Test files
├── COLAB_SETUP_INSTRUCTIONS.md          # Detailed student guide
├── GOOGLE_COLAB_IMPLEMENTATION.md       # Implementation details
└── QUICK_START.md                       # This file
```

### Key Features

- **No local setup**: Everything works in Colab
- **Immediate feedback**: Students see results instantly
- **Professional tests**: Otter-grader format
- **Gradescope ready**: Same tests can be used
- **Easy maintenance**: Update tests independently

### Testing Before Release

```bash
# 1. Open notebook in Colab
# 2. Upload tests folder to your Drive
# 3. Run setup cells
# 4. Verify all tests load
# 5. Test with sample solutions
```

### Grading Options

**Option 1: Auto-grading only (72 points)**
- Students run final cell
- Download submission zip
- You grade manually

**Option 2: Gradescope integration (100 points)**
- Use `otter assign` to create autograder
- Upload to Gradescope
- Automatic grading + manual reflection review

---

## Quick Reference

### Test Structure
- 8 test files in `tests/` directory
- Each uses `@test_case` decorators
- Points: 12, 6, 12, 6, 12, 6, 10, 8 (72 total)
- Reflection questions: 28 points (manual)

### Student Workflow
1. Mount Drive → 2. Setup Otter → 3. Code → 4. Test → 5. Submit

### Common Issues

| Issue | Solution |
|-------|----------|
| "Tests not found" | Check `tests_path` variable |
| "Module not found" | Run setup cell |
| "Permission denied" | Re-authorize Drive |
| Tests fail | Read error message carefully |

---

## Documentation

- **Full setup guide**: `COLAB_SETUP_INSTRUCTIONS.md`
- **Implementation details**: `GOOGLE_COLAB_IMPLEMENTATION.md`
- **Otter docs**: https://otter-grader.readthedocs.io

---

## Success!

✓ Notebook ready for Google Colab
✓ Tests configured and working
✓ Documentation complete
✓ Ready to deploy to students
