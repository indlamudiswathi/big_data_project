import pandas as pd
from sqlalchemy import create_engine

username = ''
password = ''
host = '34.63.107.244'
db = 'stgdb_S'

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:3306/{db}")
#folder="C:\\Swathi\\"
folder="C:\\Swathi\\STAGE1_DWH_SQL_DATAPLATFORMS\\DWH_Modern_Dataplatforms\\dataset\\"
files = {
    "stg_accounts": folder+"accounts.csv",
    "stg_transactions": folder+"transactions.csv",
    "stg_payments": folder+"payments.csv",
    "stg_creditcard": folder+"creditcard.csv",
    "stg_loans": folder+"loans.csv",
    "stg_cust_profile": folder+"cust.csv",
    "stg_branches": folder+"branches.csv",
    "stg_employees": folder+"employee.csv"}

for table, file in files.items():
    df = pd.read_csv(file)
    df.to_sql(table, con=engine, index=False, if_exists="replace")
    print(f"Rows loaded in the table {table}")
