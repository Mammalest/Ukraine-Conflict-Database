file_path = '/Users/ugurkizilkus/Desktop/db_dataset/ukraine_conflict_dataset.csv'

columns_to_split = ['source_article', 'source_office', 'source_date', 'source_headline', 'source_original']
df_full = pd.read_csv(file_path, encoding=used_encoding, error_bad_lines=False, warn_bad_lines=True)


def expand_multivalued_rows(df, columns):
    new_rows = []

    for _, row in df.iterrows():
        split_values = {col: str(row[col]).split(';') for col in columns}
        max_len = max(len(values) for values in split_values.values())
        for i in range(max_len):
            new_row = row.to_dict()
            for col in columns:
                new_row[col] = split_values[col][i] if i < len(split_values[col]) else split_values[col][-1]
            new_rows.append(new_row)

    new_df = pd.DataFrame(new_rows)
    return new_df


df_atomic = expand_multivalued_rows(df_full, columns_to_split)
output_file_path = '/Users/ugurkizilkus/Desktop/db_dataset/atomic_ukraine_dataset.csv'
df_atomic.to_csv(output_file_path, index=False, encoding='utf-8')
