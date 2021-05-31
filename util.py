import re
import os


def parse_data(log_file_path, regex, read_line=True, re_parse=False):
    with open(log_file_path, "r") as f:
        match_list = []
        if read_line:
            for line in f:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
        else:
            data = f.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group()
                match_list.append(match_text)
    f.close()
    if re_parse:
        match_list = re_parse_data(match_list, '(property name="(.{1,50})">(Enabled)<\/property>)')
    match_list_clean = list(set(match_list))
    return match_list_clean


def export_to_file(export_file, lines):
    with open(export_file, "w+") as f:
        f.write("EXPORTED DATA:\n")
    for item in xrange(0, len(lines)):
        print lines[item]
        f.write(lines[item] + "\n")
    f.close()


def re_parse_data(parsed_data, regex):
    data_string = ''.join(parsed_data)
    match_list = []
    for match in re.finditer(regex, data_string, re.S):
        match_text = match.group()
        match_list.append(match_text)
    return match_list


def get_log_files(log_dir):
    log_files = []
    for root, dir_, files in os.walk(log_dir):
        for dir__ in dir_:
            dir__path = os.path.join(root, dir__)
            # print(dir__path)
            # os.system('ls %s' % dir__path)
        for f in files:
            f_path = os.path.join(root, f)
            if ".log" in f_path:
                log_files.append(f_path)
    return log_files
