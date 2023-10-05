import dataiku
from dataiku.customrecipe import get_input_names_for_role
from dataiku.customrecipe import get_output_names_for_role
from dataiku.customrecipe import get_recipe_config


input_A_names = get_input_names_for_role('input_A_role')
output_A_names = get_output_names_for_role('main_output')

config = get_recipe_config()

source_copy = dataiku.Dataset(input_A_names[0])
source_copy_df = source_copy.get_dataframe()

prefix = config.get("prefix", "")
suffix = config.get("suffix", "")
columns_black_list = config.get("columns_black_list", [])

panda_renamed_df = source_copy_df
columns_to_rename = {}

for column_name in panda_renamed_df.columns:
    if column_name in columns_black_list:
        continue
    columns_to_rename[column_name] = "{}{}{}".format(prefix, column_name, suffix)

panda_renamed_df.rename(columns=columns_to_rename, inplace=True)

panda_renamed = dataiku.Dataset(output_A_names[0])
panda_renamed.write_with_schema(panda_renamed_df)
