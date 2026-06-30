# This is your first Buisness AI script!

# 1. Import the "calculator" for spreadsheets
import pandas as pd

# 2. Tell the computer where your download file is (on your Desktop)
file_path = r"C:\Users\kratik\VS Code\Business Process Bridge Project\bridge_project\WA_Fn-UseC_-Telco-Customer-Churn.csv"
# !!! IMPORTANT: Change "Your Name" in the line above to your actual Windows username !!!

# 3. Load the data into memory
print("Loading buisness data...")
df = pd.read_csv(file_path)

# 4. The "Buisness Diagnosis" - Let's look at the raw numbers
total_customer = len(df)
churned_customer = df[df['Churn'] == 'Yes'].shape[0]
retention_rate = (total_customer - churned_customer) / total_customer * 100

# 5. Print the results like a CEO report
print("========== BUISNESS HEALTH REPORT ==========")
print(f"Total Customers: {total_customer}")
print(f"Customers who left (churn): {churned_customer}")
print(f"Retention Rate: {retention_rate:.2f}%")
print(f"Monthly Charges average: ${df['MonthlyCharges'].mean():.2f}")
print("=======================================")