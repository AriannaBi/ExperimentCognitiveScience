import csv

# likert = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
likert_scale = {"Strongly disagree":1, "Disagree":2, "Neutral":3, "Agree":4, "Strongly agree":5}

arr = []
with open("datafile.csv", 'r') as f:
    next(f)
    csvreader = csv.reader(f)
    for i, row in enumerate(csvreader):
        row2 = row[1:13]
        # print(row)
        print("student: ", i)      
        arr = []
        for j in range(0, len(row2)):
            if row2[j] in likert_scale:
                arr.append(likert_scale[row2[j]])
            else:
                print("ERROR")
        b = row[13:16]
        for elem in b:
            arr.append(elem)
        print(arr)


                


