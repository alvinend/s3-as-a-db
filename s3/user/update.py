from s3.user.utils import get_df, save_to_s3
from s3.user.read import read

def update(
    query,
    data_dict
):
    update_column_key = list(data_dict.keys())
    update_column_value = list(data_dict.values())

    # Get Dataframe
    df = get_df()

    # Get Ids from query
    ids = read(query, select='id')
    ids = list(map(lambda x: int("".join(x)), ids))

    # Update DF
    df.loc[df.id.isin(ids), update_column_key] = update_column_value

    # Save Dataframe to S3 as CSV
    save_to_s3(df)
