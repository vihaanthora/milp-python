# MILP python
This repository consists the code accompanying the report drawn under CS 307 Optimization Algorithm & Techniques course. The topic of the report is Milk Industry Profit Maximization. 

### Tech Stack Used
1. Python - for coding LP models
2. JSON - for storing data

### Files Breakdown
The following parts comprise the code of the project.
- `simplex.py` - The matrix based simplex method that runs by iterating over Basic Feasible Points.
- `tableau_simplex.py` - This class uses the tableau method to find the optimal solution.
- `data.py` - To generate and process data that goes into the constraints. It involves random data creation and reshaping functions. It also dumps the output into `dump.json`.
- `json2np.py` - Convert json input to np arrays to feed into the simplex models.
- `dump.json` - Consists of the test case input in a json format, that can be used to test the models.
- `main.py` - Main class that consists of the driver functions.

### Running the Code
Follow the following steps to setup and run the code.
1. Create virtual environment and install the dependencies.
```sh
python3 -m venv /path/to/new/virtual/environment
pip install -r /path/to/requirements.txt
```
2. Create sample data and dump it as `dump.json`
```bash
python3 data.py
```
3. Run the models and generate output
```bash
python3 main.py
```

### Inference
Paste the graphs here @gaurav.

### Contributors
- Gaurav Jain (200001023)
- Vihaan Thora (200001079)

### Acknowledgements
We would like to express our gratitude to Dr. Kapil Ahuja, Professor, CSE, Indian Institute of Technology, Indore. We have learned immensely by completing his course and preparing this project for the adjoining lab course. 