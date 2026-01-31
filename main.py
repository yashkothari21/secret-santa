from service.csv_service import CSVService
from service.validation_service import ValidationService
from service.secret_santa_service import SecretSantaService

def main():
    try:
        print("Welcome to the Secret Santa Project!")
        
        filename = input("Enter the CSV filename to read (e.g., employees.csv): ").strip()
        data = CSVService.read_csv(filename)    
        if data:
            required_columns = ['Employee_Name', 'Employee_EmailID']
            if not ValidationService.validate_csv_data(data, required_columns):
                print("\nData format is incorrect. Please check the CSV file.")
                return
        else:
            print("No data found or file does not exist.")
            return

        # Optional: Read last year's data
        last_year_file = input("Enter the CSV filename for last year's result (Optional, press Enter to skip): ").strip()
        last_year_data = []

        if last_year_file:
            last_year_data = CSVService.read_csv(last_year_file)
            if last_year_data:
                required_cols_last_year = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
                if not ValidationService.validate_csv_data(last_year_data, required_cols_last_year):
                    print("\nLast year's data format is incorrect. Please check the CSV file.")
                    last_year_data = [] # Reset invalid data
            else:
                print("File does not exist or is empty.")
        
        # Generate Assignments
        print("Generating Secret Santa pairings...")
        assignments = SecretSantaService.assign_secret_santa(data, last_year_data)
        
        # Save assignments to file with auto-generated filename
        if assignments:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"secret_santa_assignments_{timestamp}.csv"
            CSVService.write_csv(output_file, assignments)
            print(f"Secret Santa assignment results stored in {output_file}")
        else:
            print("Failed to generate assignments.")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return

if __name__ == "__main__":
    main()
