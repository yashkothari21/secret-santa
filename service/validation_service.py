from typing import List, Dict, Any

class ValidationService:
    """
    Service to validate data formats.
    """

    @staticmethod
    def validate_csv_data(data: List[Dict[str, Any]], required_columns: List[str]) -> bool:
        """
        Validates that the data contains the required columns.
        
        Args:
            data (List[Dict[str, Any]]): The data to validate.
            required_columns (List[str]): List of column names that must be present.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        required_set = set(required_columns)
        
        if not data:
            return False
        
        # Check if all rows hae the required keys
        for index, row in enumerate(data):
            missing = required_set - row.keys()
            if missing:
                print(f"Row {index + 1}: Missing columns {missing}")
                return False
            
            # Check if values for required columns are not empty
            for col in required_columns:
                val = row.get(col)
                if val is None or not str(val).strip():
                    print(f"Row {index + 1}: {col} is empty or None. Please check the CSV file.")
                    return False
                
        return True
