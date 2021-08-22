import re
import os
import time
from time import strftime


def export_to_file(dict_with_list_values=None, export_file_path=None, export_folder=None):
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
    if not export_file_path:
        time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
        export_file_path = export_folder + "/" + time_now + ".xlsx"
    columns = dict_with_list_values.keys()
    print('Exporting columns %s to %s' % (columns, export_file_path))
    import pandas as pd
    df = pd.DataFrame(dict_with_list_values, columns=columns)
    df.to_excel(export_file_path, index=False, header=True)
    print(export_file_path)
    return export_file_path


def extract_data_from_logs(log_files=None,
                           column_names=['time', 'info', 'error', 'debug', 'warn', 'exception',
                                         'filename', 'line'], add_time_stamp=True):
    excel_export_data = {
    }
    for column_name in column_names:
        excel_export_data[column_name] = []
    print("Define column %s" % excel_export_data)
    for log_file in log_files:
        with open(log_file) as f:
            for line in f:
                one_row_values = {}  # store one row value with key as column name and its value
                for column_name in column_names:
                    column_name = column_name.lower()
                    line = line.lower().strip()
                    if column_name in line:
                        cell_value = 1
                    else:
                        cell_value = 0
                    if column_name == "line":
                        cell_value = line
                    if column_name == "filename":
                        cell_value = log_file.split('/')[-1]
                    if add_time_stamp and column_name == "time":
                        RE_COMPILE_TIME_STAMP_PATTERN = "(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]:[0-5][0-9])"
                        cell_value = finditer_line(line, regex=RE_COMPILE_TIME_STAMP_PATTERN,
                                                   log_file=log_file)
                        if not cell_value:
                            line = replace_timestamp_with_time(line)
                            cell_value = finditer_line(line, regex=RE_COMPILE_TIME_STAMP_PATTERN,
                                                       log_file=log_file)
                        if not cell_value:
                            print(line)

                    # Final cell value for that column
                    one_row_values[column_name] = cell_value

                for column_name in one_row_values:
                    # append the list value
                    existing_one_column_values = excel_export_data[column_name]
                    existing_one_column_values.append(one_row_values[column_name])
                    excel_export_data[column_name] = existing_one_column_values
    files = []
    for log_file in log_files:
        log_file = log_file.split('/')[-1]
        files.append(log_file)
    for column_name in column_names:
        print("Total %s values for Column:%s in all log files" % (
        len(excel_export_data[column_name]), column_name))

    return excel_export_data


def get_log_files(log_dir):
    log_files = []
    for root, dir_, files in os.walk(log_dir):
        for sub_dir in dir_:
            sub_dir_path = os.path.join(root, sub_dir)
            # print("sub_dir: %s" % sub_dir_path)
            # os.system('ls %s' % sub_dir_path)
        for f in files:
            f_path = os.path.join(root, f)
            if ".log" in f_path:
                log_files.append(f_path)
    print("%s" % (log_files))
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


def search_re(line, pattern=None):
    # Python program to illustrate
    # Matching regex objects
    match = re.match(pattern, line)
    if not match:
        regex_com = re.compile(pattern)
        match = regex_com.search(line)
        if match:
            value = match.group()
            print('found using re.compile: %s' % value)
            return value
        else:
            print('%s not Found using re.compile also:' % pattern)
            return ''
    else:
        value = match.group()
        print('Found using re.match: %s' % value)
        return value


def finditer_(log_file_path, regex, read_line=True):
    """
    regex = '(<property name="(.*?)">(.*?)<\/property>)'
    :param log_file_path:
    :param regex:
    :param read_line:
    :param re_parse:
    :return:
    """
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
    print(match_list)
    return match_list


def finditer_line(line, regex, log_file=None):
    """
    regex = '(<property name="(.*?)">(.*?)<\/property>)'
    :param log_file_path:
    :param regex:
    :param read_line:
    :param re_parse:
    :return:
    """
    match_text = ''
    for match in re.finditer(regex, line, re.S):
        match_text = match.group()
    return match_text


def count_cell_entries(df, col_name='', output_col_name=''):
    """
    Returns pd.value_counts() as a DataFrame

    Parameters
    ----------
    df : Pandas Dataframe
        Dataframe on which to run value_counts(), must have column `col`.
    col : str
        Name of column in `df` for which to generate counts

    Returns
    -------
    Pandas Dataframe
        Returned dataframe will have a single column named "count" which contains the count_values()
        for each unique value of df[col]. The index name of this dataframe is `col`.

    Example
    -------
    >>> value_counts_df(pd.DataFrame({'a':[1, 1, 2, 2, 2]}), 'a')
       count
    a
    2      3
    1      2
    """
    # df = pd.DataFrame(df[col].value_counts())
    # df.index.name = col
    # df.columns = ['count']
    z = df[col_name].value_counts()
    z1 = z.to_dict()  # converts to dictionary
    df[output_col_name] = df[col_name].map(z1)
    return df


def date2int(df):
    if df.timestamp:
        t = df['time']
        try:
            t1 = t.timetuple()
            return int(time.mktime(t1))
        except ValueError:
            return None


def timestamp2date(timestamp):
    from datetime import datetime
    return datetime.fromtimestamp(int(timestamp))


def replace_timestamp_with_time(line):
    if line.startswith('-'):
        tmp = line[line.index('-') + len('-'):].strip()
    elif line.startswith(' -'):
        tmp = line[line.index('-') + len('-'):].strip()
    else:
        tmp = line
    tmp = tmp.split(" ")
    if tmp:
        tmp = tmp[0]
        if tmp.isnumeric():
            time = timestamp2date(tmp)
            line = line.replace(tmp, str(time))
    return line
