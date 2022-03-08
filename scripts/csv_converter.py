import pandas as pd
from datetime import datetime

# - - -

actual_dateandtime = datetime.today().strftime('%Y-%m-%d-%H%M')
new_file_name = 'output_converted_' + actual_dateandtime + '.csv'

def read_and_save_file(new_file_name):
    df = pd.read_csv('output.csv', sep='\t', encoding='utf-8')
    df.to_csv(new_file_name, sep=';', encoding='windows-1250', index=False)

# run
read_and_save_file(new_file_name)