import os
import json
import csv
import pickle


def get_dir_info(directory):
    dir_info = []

    for root, dirs, files in os.walk(directory):
        total_size = sum(os.path.getsize(os.path.join(root, f)) for f in files)

        dir_info.append({
            "name": os.path.basename(root),
            "path": root,
            "parent": os.path.dirname(root),
            "type": "directory",
            "size": total_size
        })

        for file in files:
            file_path = os.path.join(root, file)
            dir_info.append({
                "name": file,
                "path": file_path,
                "parent": root,
                "type": "file",
                "size": os.path.getsize(file_path)
            })

    return dir_info


def save_results(data, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "results.json"), "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    csv_path = os.path.join(output_dir, "results.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "path", "parent", "type", "size"])
        writer.writeheader()
        writer.writerows(data)

    with open(os.path.join(output_dir, "results.pkl"), "wb") as pickle_file:
        pickle.dump(data, pickle_file)


if __name__ == "__main__":
    directory = input("Введите путь к директории: ")
    output_directory = "output"
    results = get_dir_info(directory)
    save_results(results, output_directory)
    print(f"Результаты сохранены в папке: {output_directory}")
