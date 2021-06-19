# Implementation of Knowledge Based SDDC LCM.

### Import Library
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import math
import re
import time
from time import strftime
from utils import util


__author__ = 'raviranjan'

### configure spark variables
# from pyspark import SparkConf, SparkContext
# from pyspark.context import SparkContext
# from pyspark.sql.context import SQLContext
# from pyspark.sql.session import SparkSession

# sc = SparkContext()
# sqlContext = SQLContext(sc)
# spark = SparkSession(sc)

### Define variables contants
LOG_DIR = "logs"
HOST_PATTERN = r'(^\S+\.[\S+\.]+\S+)\s'
LOGGER_FILE_PATTERN = r'(^\S+\.[\S+\.]+\S+)\s'
ERROR_PATTERN = 'ERROR:'
INFO_PATTERN = 'INFO:'
DEBUG_PATTERN = 'DEBUG:'
time_stamp_pattern = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]'
host_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
logger_file_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
has_error_pattern = r''
excel_file_path = "data/excel_data.xlsx"


### Get log files
log_files = util.get_log_files(log_dir=LOG_DIR)
print(log_files)


### Get Data from logs and export to Excel
# excel_export_data = util.get_data_to_export(log_files=log_files, column_names=['line', 'info', 'error', 'debug', 'warn', 'exception'])
# util.export_to_file(dict_with_list_values=excel_export_data, export_file_path=excel_file_path)

# Get timeStamp
RE_COMPILE_TIME_STAMP_PATTERN = "(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])"
RE_COMPILE_TIME_STAMP_PATTERN = "(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]:[0-5][0-9])"

for log_file in log_files:
    print(log_file)
    # util.search_re(log_file, pattern=RE_COMPILE_TIME_STAMP_PATTERN)
    util.finditer_(log_file, regex=RE_COMPILE_TIME_STAMP_PATTERN)