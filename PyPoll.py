file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')

election_data = open(file_to_load, 'r')
election_data.close()
with open(file_to_load) as election_data:
    #print(election_data)

    file_to_load = os.path.join("Resources", "election_results.csv")

file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')
election_data.close()
with open(file_to_load) as election_data:
    #print(election_data)

    import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")

# Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    # write three counties to the file
    txt_file.write("Arapahoe\n Denver\n Jefferson")
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

 # Print the header row.
    headers = next(file_reader)
    print(headers)