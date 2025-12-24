### My Tool - Execute trends_save.py and trends_plot.py, then clean up
### m01f_soln/my_tool.py
### 
### Author: Mike Smith
### Date: 2025-01-27
###
### This script executes the scraping and plotting workflow in sequence
### and removes the temporary CSV file when done.

import subprocess
import sys
import os

def main():
    csv_file = 'scraped_data.csv'
    
    try:
        print("Starting Google Trends scraping and plotting workflow...")
        print("=" * 50)

        # Step 1: Execute trends_save.py
        print("Step 1: Running trends_save.py...")
        result1 = subprocess.run([sys.executable, 'trends_save.py'], 
                               capture_output=False, text=True)
        
        if result1.returncode != 0:
            print(f"Error: trends_save.py failed with return code {result1.returncode}")
            return 1
        
        print("Step 1 completed successfully!")
        print("-" * 30)
        
        # Step 2: Execute trends_plot.py
        print("Step 2: Running trends_plot.py...")
        result2 = subprocess.run([sys.executable, 'trends_plot.py'], 
                               capture_output=False, text=True)
        
        if result2.returncode != 0:
            print(f"Error: trends_plot.py failed with return code {result2.returncode}")
            return 1
        
        print("Step 2 completed successfully!")
        print("-" * 30)
        
        # Step 3: Clean up temporary CSV file
        print("Step 3: Cleaning up temporary files...")
        if os.path.exists(csv_file):
            os.remove(csv_file)
            print(f"Removed temporary file: {csv_file}")
        else:
            print(f"Warning: {csv_file} not found (may have been already removed)")
        
        print("=" * 50)
        print("Workflow completed successfully!")
        print("Generated files:")
        print("- interest_data.png (plot)")
        
        return 0
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
