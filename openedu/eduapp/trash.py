import requests
import pandas as pd
from time import sleep

# Define the target URL
url = "https://students.kuccps.net/programmes/"

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'application/json',
}

try:
    # Send GET request
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes
    
    # Parse JSON response
    data = response.json()
    
    # Check if data is properly structured
    if isinstance(data, list) and len(data) > 0:
        # Create DataFrame
        df = pd.DataFrame(data)
        
        # Display first few rows
        print("Successfully retrieved data. First few rows:")
        display(df.head())
        
        # Clean and transform data
        # Expand nested 'institutions' column
        if 'institutions' in df.columns:
            # Convert list of institutions to comma-separated string
            df['institutions'] = df['institutions'].apply(
                lambda x: ', '.join([i.get('name', '') for i in x]) if isinstance(x, list) else x
            )
        
        # Save to CSV
        csv_filename = 'kuccps_programmes.csv'
        df.to_csv(csv_filename, index=False)
        
        # Save to Excel
        excel_filename = 'kuccps_programmes.xlsx'
        df.to_excel(excel_filename, index=False)
        
        print(f"\nSuccessfully saved data to {csv_filename} and {excel_filename}")
        
    else:
        print("Received unexpected data format from the server")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except ValueError as e:
    print(f"Failed to parse JSON response: {e}")
except Exception as e:
    print(f"An error occurred: {e}")