import json

path_file_new = "learn/test1/files/predicted_value_new.json"
path_file_old = "learn/test1/files/predicted_value_old.json"

fp = open(path_file_new, 'r')
data_file_new = json.loads(fp.read())
fp.flush()
fp.close()

fp = open(path_file_old, 'r')
data_file_old = json.loads(fp.read())
fp.flush()
fp.close()

def calculate(type):
    missmatch_count = 0
    match_count = 0
    for file_new,seller_new in data_file_new[type].items():
        if data_file_old[type][file_new] != seller_new:
            print(file_new)
            print('old: ', data_file_old[type][file_new])
            print('new:', seller_new)
            missmatch_count += 1
        else:
            match_count += 1

    print(f'matching {type}:', match_count)
    print(f'missmatch {type}:', missmatch_count)

# calculate('seller')
calculate('buyer')