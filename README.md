# Secret Santa Assignment Generator

A Python-based Secret Santa assignment generator.

## Features


- **CSV Input/Output**: Easy data management through CSV files
- **Data Validation**: Comprehensive validation of input data format and content
- **Auto-generated Results**: Timestamped output files for easy tracking

## Prerequisites

- Python 3.x installed on your system

## Project Structure

```
secret-santa/
├── main.py                          # Main entry point
├── service/
│   ├── __init__.py                  # Package initializer
│   ├── csv_service.py               # CSV read/write operations
│   ├── validation_service.py        # Data validation logic
│   └── secret_santa_service.py      # Secret Santa assignment algorithm
└── README.md                        # This file
```

## Input File Format

### Employee List (Required)
Create a CSV file with the following columns:
- `Employee_Name`: Full name of the employee
- `Employee_EmailID`: Email address of the employee

**Example: `employees.csv`**
```csv
Employee_Name,Employee_EmailID
John Doe,john@example.com
Jane Smith,jane@example.com
Bob Johnson,bob@example.com
```

### Last Year's Results (Optional)
If you want to avoid repeating last year's pairings, provide a CSV file with:
- `Employee_Name`: Full name of the employee
- `Employee_EmailID`: Email address of the employee
- `Secret_Child_Name`: Name of the person they were assigned last year
- `Secret_Child_EmailID`: Email of the person they were assigned last year

**Example: `last_year_results.csv`**
```csv
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
John Doe,john@example.com,Bob Johnson,bob@example.com
Jane Smith,jane@example.com,John Doe,john@example.com
Bob Johnson,bob@example.com,Jane Smith,jane@example.com
```

## How to Run

1. **Navigate to the project directory:**

2. **Prepare your employee CSV file** with the required format (see above)

3. **Run the main script:**
   ```bash
   python main.py
   ```

4. **Follow the prompts:**
   - Enter the filename for your employee list (e.g., `employees.csv`)
   - Optionally enter the filename for last year's results (or press Enter to skip)

5. **Get your results:**
   - The program will generate assignments and save them to a timestamped CSV file
   - Example output: `secret_santa_assignments_20260131_152201.csv`

## Output File Format

The generated assignment file contains:
- `Employee_Name`: Name of the Secret Santa
- `Employee_EmailID`: Email of the Secret Santa
- `Secret_Child_Name`: Name of the person they should give a gift to
- `Secret_Child_EmailID`: Email of the person they should give a gift to

## Example Usage

```bash
$ python main.py
Welcome to the Secret Santa Project!
Enter the CSV filename to read (e.g., employees.csv): employees.csv
Enter the CSV filename for last year's result (Optional, press Enter to skip): 
Generating Secret Santa pairings...
Secret Santa assignment results stored in secret_santa_assignments_20260131_152201.csv
```

## Notes

- All CSV files should be in the same directory as `main.py` or provide the full path
- The output file is automatically saved in the project directory
- Each run creates a new timestamped file to preserve history
