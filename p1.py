import csv
import pandas
from typing import List
from fastapi import FastAPI, Request
from schema import Employee


app = FastAPI()

@app.post("/upload_csv")
async def upload_csv(employees: List[Employee]):
    # Open the CSV file in append mode
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        # Write the header row if the file is empty
        # if file.tell() == 0:
        #     writer.writerow(["Reg_No", "Phone"])
        
        # Write each employee data to the CSV file
        for employee in employees:
            writer.writerow([employee.Reg_No, employee.Phone,employee.Name,"True"])
    
    return {"message": "CSV data saved successfully."}



@app.get("/read_csv")
def read_csv():
    
    csvFile = pandas.read_csv('data.csv')
   
    df = pandas.DataFrame(csvFile)
    df = df.to_string
    records = []
    for i in df.iterrows():
        myDict = {
            "Name" : df.loc[i,"Name"],
            "Reg_No" : int(df.loc[i,"Reg_No"]),
            "Phone" : int(df.loc[i,"Phone"])
            
            
        }
        
        print(myDict)
        # records.append(myDict)
            
    return records 
   

@app.put("/update")
def update_data(employees: List[Employee]):  
    pass  