import plotly.express as px
import csv
import numpy as np

#plotting the figure
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()


#getting the data source
def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks_in_percentage, "y": days_present}

#finding the correlation between the given data
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "data_two.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()