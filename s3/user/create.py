from s3.user.read import read
from s3.user.utils import get_df, save_to_s3

def create(
    data_dict
):
    # Get Dataframe
    df = get_df()

    # Get Ids from query
    max_id = read('', select='MAX(cast(id as int))')
    max_id = int(max_id[0][0])

    # Update DF
    data_dict['id'] = max_id + 1

    df = df.append(data_dict, ignore_index=True)

    # Save Dataframe to S3 as CSV
    save_to_s3(df)
