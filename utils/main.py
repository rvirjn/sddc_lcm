import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
import math
import re
import time
from time import strftime
from utils import util


### Define variables contants
LOG_DIR = "logs"
HOST_PATTERN = r'(^\S+\.[\S+\.]+\S+)\s'
LOGGER_FILE_PATTERN = r'(^\S+\.[\S+\.]+\S+)\s'
ERROR_PATTERN = 'ERROR:'
INFO_PATTERN = 'INFO:'
DEBUG_PATTERN = 'DEBUG:'
host_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
logger_file_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
has_error_pattern = r''
excel_file_path = "data/excel_data_1.xlsx"


### Get log files
log_files = util.get_log_files(log_dir=LOG_DIR)
print(log_files)


### Get Data from logs and export to Excel
excel_export_data = util.extract_data_from_logs(log_files=log_files, column_names=['time', 'info', 'error', 'debug', 'warn', 'exception', 'filename', 'line'])
util.export_to_file(dict_with_list_values=excel_export_data, export_file_path=excel_file_path)

import time
print(excel_file_path)
df = pd.read_excel(excel_file_path)