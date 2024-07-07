import sqlite3
import pandas as pd 
import numpy as np

while True:
    #Get the user input
    search_string = input("Enter name to search in the database: ")   

    #Check if the input string is empty. If yes, then asking for the input again
    if not search_string.strip():
        print("Please enter a search string")
        continue 
    else:
        #Establishing connection with the database created
        connection = sqlite3.connect("Assignment\\assignment.db")

        #Creating a cursor in order to interact with the database
        cursor = connection.cursor()

        #Writing query to extract records that contain the user input (case in-sensitive)
        cursor.execute("SELECT * FROM student_details where name LIKE '%' || ? || '%' COLLATE NOCASE",(search_string,))

        #Fetching the results of the query
        results = cursor.fetchall()

        #Commting if any changes, to the table
        connection.commit()

        #Close the connection with the database
        connection.close()

        #Check if the above query contains any records
        if results:
            print("Displaying all the records that match the user input: ")

            #Converting the resulting records to a Pandas DataFrame
            results_table = pd.DataFrame(results)

            #Modifying the column and row index of the DataFrame
            results_table.columns=['Name','Marks']
            results_table.index=np.arange(1,len(results_table)+1)
            print(results_table)

            #Calculating the total and average values of the resulting records 
            total_marks=0
            total_records=results_table.shape[0]
            for ind in results_table.index:
                total_marks += results_table['Marks'][ind]
            average_mark = total_marks/total_records

            print()
            print("Total Marks: ",total_marks)
            print("Average Marks: ",average_mark)
        else:
            print("No matching records found in the table for the given input")
        break 
        





