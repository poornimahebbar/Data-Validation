import pandas as pd
from Scripts.db_connection import get_db_data
from Scripts.validation import validate_data
from datetime import datetime


# Load data
df_db = get_db_data()
df_excel = pd.read_excel("data/Orderdetailsdata.xlsx")

db_cols = list(df_db.columns)
excel_cols = list(df_excel.columns)

for col_db, col_excel in zip(db_cols, excel_cols):
    if col_db != col_excel:
        print(f"Mismatch → DB: {col_db} | Excel: {col_excel}")

# Run validation
mismatch, value_diff = validate_data(df_db, df_excel)

# Save report
with pd.ExcelWriter("output/validation_report.xlsx") as writer:
    mismatch.to_excel(writer, sheet_name="Missing_Extra", index=False)
    value_diff.to_excel(writer, sheet_name="Value_Differences", index=False)

print("Validation Completed ✅")
print("\n📊 DATA VALIDATION REPORT")
print("="*40)
print(f"Total Records (DB): {len(df_db)}")
print(f"Total Records (Excel): {len(df_excel)}")
print(f"Missing / Extra Records: {len(mismatch)}")
print(f"Value Mismatches: {len(value_diff)}")
print(f"Mismatch %: {(len(mismatch)/len(df_db))*100:.2f}%")
print(f"Value Diff %: {(len(value_diff)/len(df_db))*100:.2f}%")
print(f"Run Time: {datetime.now()}")
print("="*40)