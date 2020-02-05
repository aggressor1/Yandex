def print_operation_table(operation, num_rows=9, num_columns=9):
    for j in range(1, num_rows + 1):
        for i in range(1, num_columns + 1):
            print(operation(j, i), end='\t')
        print()