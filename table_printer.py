table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
results = []
result = ''
max_lengths = []
for i in range(len(table_data)):
    max_lengths.append(len(max(table_data[i], key=len)))
print(max_lengths)
for i in range(0, len(table_data[0])):
    for j in range(0, len(table_data)):
        result += table_data[j][i].rjust(max_lengths[j])+' '

    results.append(result)
    result = ''
result_in_str = '\n'.join(results)
print(result_in_str)
