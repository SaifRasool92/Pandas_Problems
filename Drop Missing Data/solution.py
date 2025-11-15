import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    students.dropna(subset=['name'], inplace=True)
    return students
