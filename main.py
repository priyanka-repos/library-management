from fastapi import FastAPI, HTTPException
import csv, pandas as pd
from schema import User

app = FastAPI()

@app.post("/add_csv")
def add_csv(user: User):
    # header = ['Name', 'Phone']
    with open('data.csv', mode='a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # if csvfile.tell() == 0:
        #     csvwriter.writerow(header)


        csvwriter.writerow([user.reg_no, user.name, user.phone])

    return "Successfully added data to csv file" 


@app.get("/read_csv/{phone}")
def read_csv(phone: int):
 
    csvfile = pd.read_csv('data.csv')
 
    records = []

    for index, row in csvfile.iterrows():
        if(row['Phone'] == phone):
            record = {
                "Name": row['Name'],
                "Phone": row['Phone']
             }
            records.append(record)
        else:
             raise HTTPException(status_code=404, detail="Data not found") 

    return records

@app.put("/update_data/{phone}")
def update_csv(phone:int,user:User):
    csvfile = pd.read_csv('data.csv')

    for index, row in csvfile.iterrows():
        if(row['Phone'] == phone):
            csvfile.at[index, 'Name'] = user.name
            csvfile.at[index, 'Phone'] = user.phone
 
    csvfile.to_csv('data.csv', index=False) 


    return "Success"