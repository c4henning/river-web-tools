import csv

source_csv = "test.csv"

with open(source_csv, 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

trimmed_data = []
for i in range(1, len(data)):
    if data[i][2][:2] == "M-":
        trimmed_data.append(data[i])
data = trimmed_data

data = sorted(data, key=lambda x: (x[1], x[7], x[8]))

ft_cycles = dict()

for i in range(len(data)):
    element = data[i]
    # instrument blank
    data[i].append(True) if data[i][3] == '' else data[i].append(False)
    # same sample as above
    data[i].append(True) if data[i][1] == data[i - 1][1] else data[i].append(False)
    # double xfer
    data[i].append(False) if data[i][9] and data[i - 1][9] else data[i].append(True)
    # all true
    data[i].append(True) if data[i][9] and data[i][10] and data[i][11] else data[i].append(False)

    # print(data[i])
    if data[i][-1]:
        if data[i][1] not in ft_cycles.keys():
            ft_cycles[data[i][1]] = 1
        else:
            ft_cycles[data[i][1]] += 1

ft_max_obs = max(ft_cycles.values())
print("Highest # of F/T cycles:", ft_max_obs)
ft_max_allow = int(input("Enter max allowable F/T cycles: "))
for key in ft_cycles:
    if ft_cycles[key] > ft_max_allow:
        print(key, "F/T cycles:", ft_cycles[key])
