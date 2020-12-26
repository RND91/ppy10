import numpy as np
import csv 
import plotly.express as px

def get_data_source(data_path):
    days = []
    marks = []
    with open(data_path) as csvf:
        csvreader = csv.DictReader(csvf)
        for row in csvreader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x":days,"y":marks}
    

def correl(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(correlation[0,1])

def plot(data_path):
    with open(data_path) as csvf:
        reader = csv.DictReader(csvf)
        fig = px.scatter(reader,x="Days Present",y="Marks In Percentage")
        fig.show()

def main():
    data_path = "data2.csv"
    ds = get_data_source(data_path)
    correl(ds)
    plot(data_path)

main()