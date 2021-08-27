from utils import util


LOG_DIR = "logs"
excel_file_path = "data/excel_data_1.xlsx"


### Get log files
log_files = util.get_log_files(log_dir=LOG_DIR)
print(log_files)


### Get Data from logs and export to Excel
excel_export_data = util.extract_data_from_logs(log_files=log_files, column_names=['time', 'info', 'error', 'debug', 'warn', 'exception', 'filename', 'line'])

util.export_to_file(dict_with_list_values=excel_export_data, export_file_path=excel_file_path)
