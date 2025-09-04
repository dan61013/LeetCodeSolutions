import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # merge two tables
    merge_df = visits.merge(
        transactions,
        how='left',
        on='visit_id'
    )
    # filtering: isna
    merge_df = merge_df[merge_df['transaction_id'].isna()]
    # groupby each customerID and count NULL
    cnt_ser = merge_df.groupby(
        by=['customer_id']
    ).agg(count_no_trans=('transaction_id', lambda x: x.isna().sum()))

    return cnt_ser.reset_index()