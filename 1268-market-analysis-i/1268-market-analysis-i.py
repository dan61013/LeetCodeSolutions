import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # Merge: users <- orders (left join)
    merge_df = users.merge(
        # filtering orders by order date equal 2019
        orders[orders['order_date'].dt.year == 2019],
        left_on='user_id',
        right_on='buyer_id',
        how='left'
    )
    # create result df (distinct: user_id)
    res_df = merge_df.loc[:, ['user_id', 'join_date']].drop_duplicates(subset='user_id')
    # groupby and then count the orders each user
    cnt_df = merge_df.groupby(
        by='user_id'
    ).agg({'order_date': 'count'}).reset_index()
    # Merge: cnt & res df
    res_df = res_df.merge(
        cnt_df,
        on='user_id',
        how='inner'
    )
    # rename columns
    res_df = res_df.rename({'user_id': 'buyer_id', 'order_date': 'orders_in_2019'}, axis=1)

    return res_df