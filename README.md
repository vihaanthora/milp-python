# MILP python
This repository consists the code accompanying the report drawn under CS 307 Optimization Algorithm & Techniques course. The topic of the report is Milk Industry Profit Maximization. 

### Tech Stack
1. Python - for coding LP models
2. JSON - for storing data

### Project hierarchy
The following parts comprise the code of the project.
- `simplex.py` - The matrix based simplex method that runs by iterating over Basic Feasible Points.
- `tableau_simplex.py` - This class uses the tableau method to find the optimal solution.
- `data.py` - To generate and process data that goes into the constraints. It involves random data creation and reshaping functions. It also dumps the output into `dump.json`.
- `json2np.py` - Convert json input to np arrays to feed into the simplex models.
- `main.py` - Main file that consists of the driver functions.
- `wrapper.py` - Wrapper file for driver functions
- `data/` - Consists of the test case inputs/outputs in json format, that can be used to test the models.

### Pre-requisites
Create virtual environment and install the dependencies.
```bash
$ python -m venv /path/to/new/virtual/environment
$ pip install -r requirements.txt
```

### Usage
Run the models and generate output
```bash
$ python main.py -m method {1,2} -i input-file -o output-file
# Example
$ python main.py -i data/inp1.json -o data/out1.json
```

### Random Data Generation
In absence of data, Pseduo-Random data can be generated by supplying custom parameters
```bash
$ python input_generator -n n -m m -t t -o output-file
```

### Contributors
- Gaurav Jain (200001023)
- Vihaan Thora (200001079)

### Acknowledgements
We would like to express our gratitude to Dr. Kapil Ahuja, Professor, CSE, Indian Institute of Technology, Indore. 
We have learned immensely by completing his course and preparing this project for the adjoining lab course.
