# ==========================================
# Utility Functions
# ==========================================

import pandas as pd
from config import CSV_FILE_NAME


def save_csv(data):
    """
    Save reviews to CSV file
    """

    try:

        df = pd.DataFrame(data)

        df.to_csv(CSV_FILE_NAME, index=False)

        print("✅ CSV Export Successful")

    except Exception as e:

        print("❌ CSV Export Failed")
        print(e)