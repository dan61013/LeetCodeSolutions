import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[
        views['author_id'] == views['viewer_id']
    ].drop_duplicates(subset='viewer_id')
    return views.loc[:, 'viewer_id'].sort_values().rename('id').to_frame()