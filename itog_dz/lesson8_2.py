import json
import pickle
import os

def json_to_pickle(directory = '.'):
    for file in os.listdir(directory):
        file_name, file_exten = os.path.splitext(file)
        if file_exten == '.json':
            with open(os.path.join(directory, file), 'r', encoding='utf-8'):
                data = json.load(f)
            with open(os.path.join(directory, file_name + '.pickle'), 'w', encoding='utf-8') as f:
                pickle.dump(data, f)
if __name__ == '__main__':
    json_to_pickle()
