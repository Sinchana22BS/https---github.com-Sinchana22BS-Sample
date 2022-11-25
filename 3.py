import csv
with open("candidate.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)
    specific = data[1][:-1]
    general = [['?' for i in range (len(specific))] for j in range(len(specific))]
    for i in data:
        if i[-1] == "Yes":
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    specific[j] = "?"
                    general[j][j]="?"
        elif i[-1] == "No":
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    general[j][j] = specific[j]
                else :
                    general[j][j] = "?"
        print("\n step" + str(data.index(i)+1) + "of candidates Elimination Algorithm")
        print(specific)
        print(general)
    gh = []
    for i in general:
        for j in i:
            if j != '?':
                gh.append(i)
                break
        print("\n Final Specific hypothesis : \n" , specific)
        print("\n Final General hypothesis:\n",gh)