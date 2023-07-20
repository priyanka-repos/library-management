from fastapi import FastAPI, HTTPException
import csv, pandas as pd
from schema import User
from typing import Dict

app = FastAPI()

@app.post("/add_csv")
def add_csv(user: User):
    
    with open('data.csv', mode='a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerow([user.reg_no, user.phone, user.name,"False"])

    return "Successfully added data to csv file" 


@app.get("/read_csv")
def read_csv():
 
    csvfile = pd.read_csv('data.csv')
 
    records = []
    try:
        for index, row in csvfile.iterrows():
            if(row['Waiting'] == True):
                record = {
                    "Reg_No": row['Reg_No'],
                    "Name": row['Name'],
                    "Phone": row['Phone']
                }
                records.append(record)
        return records        
    except Exception:
        raise HTTPException(status_code=404, detail="Data not found") 

    

@app.put("/update_data/{phone}")
def update_csv(phone:int,user:User):
    csvfile = pd.read_csv('data.csv')

    for index, row in csvfile.iterrows():
        if(row['Phone'] == phone):
            csvfile.at[index, 'Name'] = user.name
            csvfile.at[index, 'Phone'] = user.phone
 
    csvfile.to_csv('data.csv', index=False) 


    return "Success"