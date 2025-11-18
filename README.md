# Lab1-nshutilancelot3

This small project contains two helper scripts to collect and manage course grades:

- `grade-generator.py` — an interactive Python script to enter assignments, categories, grades and weights, compute weighted totals and GPA, and export a `grades.csv` file.
- `organizer.sh` — a shell script that archives any `.csv` files in the project root into an `archive/` folder and logs the archived content to `organizer.log`.

**Requirements**

- **Python 3** to run `grade-generator.py`.
- A POSIX shell (e.g. `bash`) to run `organizer.sh`.

**How It Works**

- `grade-generator.py` prompts you to enter assignment information:
	- Assignment name (must be unique and not empty)
	- Category: `FA` (Formative, max total weight 60) or `SA` (Summative, max total weight 40)
	- Grade (0–100)
	- Weight (positive integer; cannot exceed remaining total or category remaining weight)
- The script keeps track of remaining weight (100 total: 60 FA + 40 SA), computes weighted scores, prints a results summary (formative/summative totals, GPA, pass/fail status, and suggested resubmissions), and writes `grades.csv` with columns: `Assignment`, `Category`, `Grade`, `Weight`.

- `organizer.sh` finds all `.csv` files in the current directory, logs each file's content and archive metadata to `organizer.log`, then moves the file into `archive/` with a timestamped name (e.g. `grades-20251118-142530.csv`). The script creates `archive/` if it does not exist.

**Usage**

Run the grade generator (interactive):

```bash
python3 grade-generator.py
```

Sample interaction flow:

- Enter assignment name (unique)
- Enter category (`FA` or `SA`)
- Enter grade (e.g. `88.5`)
- Enter weight (integer; will prompt if exceeds remaining weight)
- When finished, the script prints a results block and writes `grades.csv` in the current directory.

Archive CSV files using the organizer script:

```bash
# Make organizer executable once (optional)
chmod +x organizer.sh

# Run it
./organizer.sh
```

After running, archived CSVs appear in `archive/` and `organizer.log` contains a copy of each archived file and a timestamped entry.

**Files**

- `grade-generator.py` — interactive grade input and CSV export.
- `organizer.sh` — archives `.csv` files into `archive/` and logs details to `organizer.log`.
- `organizer.log` — created/updated by `organizer.sh` (appended entries).

**Notes & Tips**

- `grade-generator.py` will overwrite `grades.csv` if it already exists and notifies you before doing so.
- The script enforces category caps: formative (`FA`) total weight <= 60, summative (`SA`) total weight <= 40.
- If you prefer non-interactive workflows, you can edit the scripts to accept arguments or consume a prepared CSV; feel free to ask if you want that added.

If you want, I can run a quick smoke test (enter sample data) and show the generated `grades.csv` and archive behavior. 
