import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merge_df = employees.merge(
        employee_uni,
        how='left',
        on='id'
    )
    return merge_df[['unique_id', 'name']]