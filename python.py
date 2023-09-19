#Import the file, replace with the correct filepath
import csv
file_path = '/Users/agramont/Documents/jagramont_python/brca_cnvs_tcga-1.csv'
#the data of the excercise as a list
excercise = []
#open the data
with open(file_path, mode='r') as file:
    #read the file
    csv_reader = csv.reader(file)
    
    #ignore the head names in the first row
    next(csv_reader)
    
    for row in csv_reader:
        #extract the values of column 3 and column 4
        start = float(row[2])  
        end = float(row[3])  
        
        #determine the size
        Size = end - start
        #add the results to the file
        row.append(Size)
        excercise.append(row)
#save the results in a new csv file
output_file = '/Users/agramont/Documents/jagramont_python/excercise_results_file.csv'

with open(output_file, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # include the results of the excercise as a new row in the csv file
    for row in excercise:
        csv_writer.writerow(row)

# Print the modified data.
for row in excercise:
    print(row)