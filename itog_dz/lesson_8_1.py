import json

def json_to_csv(name = "db.json", res_file="db.csv"):
    with open(name, 'r', encoding='utf-8') as f_json:
        db = json.load(f_json)
    with open(res_file, 'w', encoding='utf-8') as f:
        for k, v in db.items():
            for k2, v2 in v.items():
                print(f"{k}, {k2}, {v2}", file = f)

if __name__ == '__main__':
    json_to_csv()