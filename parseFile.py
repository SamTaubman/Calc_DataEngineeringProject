import csv
    
def createFileStructure(cleaned_data, num_of_blanks):
    num_of_data = num_of_blanks//2 #since there are 2 blank rows with every new section of data can use num_of_blanks to find how many data sections there are
    FileStructure = []
    i = 0 #i keeps track of position in cleaned_data
    for _ in range(num_of_data):
        Data = []
        Upper = True
        
        #While loop to handle row wise entered data
        while Upper:
            row = cleaned_data[i]
            if not row[0]:
                Upper = False
                i += 1
                break
            group = {"name":"","units":"","data":""}
            group["name"] = str(row[0])
            group["units"] = str(row[2])
            group["data"] = str(row[1])
            Data.append(group)
            i += 1
        
        #for loop to handle column wise entered data
        for x in range(len(cleaned_data[i])):
            case = []
            for dta in range(i+2, len(cleaned_data)):
                if cleaned_data[dta][x] == '':
                    break
                if cleaned_data[dta][7] == 'yes':
                    continue
                case.append(str(cleaned_data[dta][x]))
            Data.append({"name":str(cleaned_data[i][x]), "units":str(cleaned_data[i+1][x]), "data":case})
        i = dta + 1 #set i to next new section of data after blank row
        
        FileStructure.append(Data)

    return FileStructure

def openFile(data_path):
    remove_blankRows_data = []
    num_of_blanks = 0
    previous_row_empty = False
    #removes any contiguous blank rows of data
    with open(data_path, newline='\n') as inputfile:
        for row in csv.reader(inputfile):
            current_row_empty = not any(row)
            if current_row_empty:
                num_of_blanks += 1
            if current_row_empty and previous_row_empty:
                num_of_blanks -= 1
                continue
            remove_blankRows_data.append(row)
            previous_row_empty = current_row_empty
    FileStructure = createFileStructure(remove_blankRows_data, num_of_blanks)
    print(FileStructure)

data_path = ""
openFile(data_path)
