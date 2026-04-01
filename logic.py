import csv

def get_employee_data(filepath="data.csv"):
    """Reads the CSV and returns headers and data rows separately."""
    headers = []
    rows = []
    
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            
            # Extract the first row as headers
            headers = next(reader)
            
            # Extract the rest as data rows
            for row in reader:
                rows.append(row)
                
    except FileNotFoundError:
        # We will handle the empty lists in the UI layer
        pass 
        
    return headers, rows