import csv
import os
from typing import List, Dict, Any

class CSVService:
    """
    A service class to handle reading from and writing to CSV files.
    """

    @staticmethod
    def read_csv(file_path: str) -> List[Dict[str, Any]]:
        """
        Reads a CSV file and returns the content as a list of dictionaries.
        
        Args:
            file_path (str): The absolute or relative path to the CSV file.
            
        Returns:
            List[Dict[str, Any]]: A list where each item represents a row in the CSV.
        """
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return []

        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                data = [row for row in reader]
                return data
        except Exception as e:
            print(f"Error reading CSV file. Please check the file path and format.")
            return []

    @staticmethod
    def write_csv(file_path: str, data: List[Dict[str, Any]]):
        """
        Writes a list of dictionaries to a CSV file.
        
        Args:
            file_path (str): The destination path for the CSV file.
            data (List[Dict[str, Any]]): The data to write.
        """
        if not data:
            print("Warning: No data to write.")
            return

        try:
            # Extract headers from the first dictionary keys
            headers = data[0].keys()
            
            with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            print(f"Error writing CSV file")
