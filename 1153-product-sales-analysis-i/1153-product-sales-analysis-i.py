import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merge_df = sales.merge(
        product,
        how='inner',
        on='product_id'
    )
    return merge_df[[
        'product_name',
        'year',
        'price'
    ]]