import pandas as pd

# Load the Excel file
df = pd.read_excel("Copy of Test data.xlsx")

# This is the cleaned data we'll build
rows = []

for idx, row in df.iterrows():
    name = row[0]  # First column is the name
    data = row[1:]  # Remaining columns are grouped in 4s (receipt date, no, shares, bank statement)
    
    # Iterate in chunks of 4
    for i in range(0, len(data), 4):
        try:
            receipt_date = data[i]
            receipt_no = data[i+1]
            shares = data[i+2]
            bank_status = data[i+3]
        except IndexError:
            # In case the last block is incomplete
            continue
        
        # Skip empty rows
        if pd.isna(receipt_date) and pd.isna(receipt_no) and pd.isna(shares):
            continue
        
        rows.append({
            "Name": name,
            "Receipt Date": receipt_date,
            "Receipt No": receipt_no,
            "Shares in KES": shares,
            "Bank Statement": bank_status
        })

# Create the new DataFrame
clean_df = pd.DataFrame(rows)

# Save to a new file
clean_df.to_excel("clean_receipts.xlsx", index=False)

print("✅ Done! Your cleaned data is now in 'clean_receipts.xlsx'")
files.download("clean_receipts.xlsx")
