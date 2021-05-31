

from util import get_log_files
log_dir = "logs"
time_stamp_pattern = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]'
host_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
logger_file_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
has_error_pattern = 'ERROR:'
regex = '(<property name="(.*?)">(.*?)<\/property>)'
log_files = get_log_files(log_dir=log_dir)

from util import finditer_
# finditer_(log_file_path=log_files[0], regex=has_error_pattern)

from util import findall_
search_lines = findall_(log_file=log_files[0], regex=has_error_pattern)

from util import export_to_file
export_to_file(export_folder=log_dir, dict_with_list_values={"HasError": search_lines})