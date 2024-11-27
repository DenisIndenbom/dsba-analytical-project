from fastapi import FastAPI
from pandas import read_csv

from config import DATA_PATH
from units import Row, RowCreate

# Create the FastAPI instance
app = FastAPI(
    title='Earthquakes API',
    description='An API of earthquakes analysis project',
    version='1.0.0'
)

# Load dataset
data = read_csv(DATA_PATH, engine='pyarrow')


@app.get('/get_row/{index}')
def get_row(index: int):
    row = Row(index=index, **(data.iloc[index].to_dict()))

    return row


@app.post('/create_row')
def get_row(row: RowCreate):
    data.append(row.to_dict(), ignore_index=True)

    return {'index': len(data)}
