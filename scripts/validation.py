import pandas as pd

def validate_data(df_db, df_excel):
 
    
 #Step 1: Merge using correct keys
    compare = df_db.merge(
        df_excel,
        on=["OrderID", "ProductID"],
        suffixes=('_db', '_excel'),
        how="outer",
        indicator=True
    )
    # Missing / Extra
    mismatch = compare[compare["_merge"] != "both"].copy()

    # Value Differences
    value_diff = compare[
        (compare["_merge"] == "both") &
        (compare["priceQuantity_db"] != compare["priceQuantity_excel"])
    ].copy()

    value_diff["diff_priceQuantity"] = (
        value_diff["priceQuantity_db"] - value_diff["priceQuantity_excel"]
    )

    return mismatch, value_diff