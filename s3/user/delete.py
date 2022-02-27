from s3.user.utils import get_df, save_to_s3
from s3.user.read import read

def delete(query):
    # Get Dataframe
    df = get_df()

    # Get Ids from query
    ids = read(query, select='id')
    ids = list(map(lambda x: int("".join(x)), ids))

    # Filter out Selected ID
    newdf = df[~df.id.isin(ids)]

    # Save Dataframe to S3 as CSV
    save_to_s3(newdf)
