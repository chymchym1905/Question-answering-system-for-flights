import csv
import os
import glob



def read_txt_files(folder_path):
    results = []
    for filename in os.listdir(folder_path):
        if filename.startswith("1") and filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                results.append((filename, content))
    return results

def read_txt_files2(folder_path):
    results = []
    for filename in os.listdir(folder_path):
        if filename.startswith("2") and filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                results.append((filename, content))
    return results

def read_txt_files3(folder_path):
    results = []
    for filename in os.listdir(folder_path):
        if filename.startswith("3") and filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                results.append((filename, content))
    return results

def read_txt_files4(folder_path):
    results = []
    for filename in os.listdir(folder_path):
        if filename.startswith("4") and filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                results.append((filename, content))
    return results

def write_to_csv(data, csv_file_path):
    with open(csv_file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Filename", "Content"])
        for row in data:
            writer.writerow([row[0], row[1]])



def run():
    output = "./test/output"
    # testpath = "./test/input"
    # expectpath = "./test/expect"

    # folder_path = "./name/q1/src/test/solutions"
    # testpath = "./name/q1/src/test/solutions"

    wordsegment = "./viewresult/wordsegment.csv"
    relations = "./viewresult/relations.csv"
    logicalform = "./viewresult/logicform.csv"
    answer = './viewresult/answers.csv'
    # testcase = "./testcase.csv"
    # expect = "./expect.csv"

    data = read_txt_files(output)
    write_to_csv(data, wordsegment)

    data = read_txt_files2(output)
    write_to_csv(data, relations)

    data = read_txt_files3(output)
    write_to_csv(data, logicalform)

    data = read_txt_files4(output)
    write_to_csv(data, answer)

    # data = read_txt_files(testpath)
    # write_to_csv(data, testcase)

    # data = read_txt_files(expectpath)
    # write_to_csv(data, expect)