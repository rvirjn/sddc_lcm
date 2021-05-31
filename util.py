import re
import os
import time
from time import strftime
import pandas as pd


def export_to_file(export_folder, dict_with_list_values=None):
    """
    dict_with_list_values = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [32000,35000,37000,45000]
        }
    :param export_folder:
    :param dict_with_list_values:
    :param create_dict_from_list:
    :param column_name
    :return:
    """
    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
    export_file_path = export_folder + "/" + time_now + ".xlsx"
    columns = dict_with_list_values.keys()
    print('Exporting columns %s to %s' % (columns, export_file_path))
    df = pd.DataFrame(dict_with_list_values, columns=columns)
    df.to_excel(export_file_path, index=False, header=True)
    print(export_file_path)
    return export_file_path


def create_dict_from_list():
    dict_from_list = {}
    return dict_from_list


def get_log_files(log_dir):
    log_files = []
    for root, dir_, files in os.walk(log_dir):
        for sub_dir in dir_:
            sub_dir_path = os.path.join(root, sub_dir)
            print("sub_dir: %s" % sub_dir_path)
            # os.system('ls %s' % sub_dir_path)
        for f in files:
            f_path = os.path.join(root, f)
            if ".log" in f_path:
                log_files.append(f_path)
    print("Log file under %s are %s" % (log_dir, log_files))
    return log_files


def findall_(log_file, regex):
    matched_lines = []
    with open(log_file) as f:
        # lines = f.readlines()
        for line in f:
            found = re.findall(regex, line)
            if found:
                matched_lines.append(line)
        print(matched_lines)
    return matched_lines


def finditer_(log_file_path, regex, read_line=True, re_parse=False):
    with open(log_file_path, "r") as f:
        match_list = []
        if read_line:
            for line in f:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    print(match_text)
                    print(line)
                    match_list.append(match_text)
        else:
            data = f.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group()
                match_list.append(match_text)
    f.close()
    if re_parse:
        match_list = finditer_again(match_list, regex)
    match_list_clean = list(set(match_list))
    print(match_list_clean)
    return match_list_clean


def finditer_again(parsed_data, regex):
    data_string = ''.join(parsed_data)
    match_list = []
    for match in re.finditer(regex, data_string, re.S):
        match_text = match.group()
        match_list.append(match_text)
    print(match_list)
    return match_list
