"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий."""

import os
import json
import csv
import pickle

def get_directory_info(directory):
    result = []

    def get_size(path):
        if os.path.isfile(path):
            return os.path.getsize(path)
        elif os.path.isdir(path):
            total_size = 0
            for dirpath, _, filenames in os.walk(path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(filepath)
            return total_size

    def explore_directory(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            item_type = "file" if os.path.isfile(item_path) else "directory"
            item_size = get_size(item_path) if os.path.isdir(item_path) else os.path.getsize(item_path)
            result.append({"name": item, "type": item_type, "size": item_size, "parent_directory": directory})
            if os.path.isdir(item_path):
                explore_directory(item_path)

    explore_directory(directory)

    with open('directory_info.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)

    with open('directory_info.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["name", "type", "size", "parent_directory"])
        for item in result:
            csv_writer.writerow([item["name"], item["type"], item["size"], item["parent_directory"]])

    with open('directory_info.pickle', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)
