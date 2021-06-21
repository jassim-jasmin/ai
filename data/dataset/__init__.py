import pandas as pd


def create_dataset(dtaset_path, file_name):
    with open(dtaset_path, mode='r') as fp:
        data = fp.read()


    list_data = data.split('\n')

    dataframe = pd.DataFrame(columns=['label', 'text'])

    for index, each_data in enumerate(list_data):
        each_data = each_data.replace('\t', ' ')
        split_data = each_data.split(' ', 1)

        if split_data[0]:
            dataframe.loc[index] = split_data

    dataframe.to_csv(f'{file_name}.csv')