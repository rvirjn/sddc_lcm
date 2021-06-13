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
TIME_STAMP_PATTERN = "^(2[0-3]|[01]?[0-9]):(0[1-9]{1}|[1-5]{1}[0-9]):(0[1-9]{1}|[1-5]{1}[0-9])$"
HOST_PATTERN = r'(^\S+\.[\S+\.]+\S+)\s'
LOGGER_FILE_PATTERN = r'(^\S+\.[\S+\.]+\S+)\s'
ERROR_PATTERN = 'ERROR:'
INFO_PATTERN = 'INFO:'
DEBUG_PATTERN = 'DEBUG:'
time_stamp_pattern = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]'
host_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
logger_file_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
has_error_pattern = r''

### Get log files
log_files = util.get_log_files(log_dir=LOG_DIR)
print(log_files)


### Get Data from logs and export to Excel
excel_export_data = util.get_data_to_export(log_file=log_files[0], column_names=['line', 'info', 'error', 'debug', 'warn', 'exception'])
DATA_DIR = "data"
util.export_to_file(export_folder=DATA_DIR, dict_with_list_values=excel_export_data, export_file_path="data/excel_data.xlsx")


# Get timeStamp
util.search_re(log_files[0], pattern="04/24/2021 11:23:41 am")


excel_data = pd.read_excel("data/excel_data.xlsx")
excel_data.head(10)