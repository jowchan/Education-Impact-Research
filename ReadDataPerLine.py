""""
The following script collects data on college seniors.
The data is organized by:
name, hometown, major and minor on one line each (major and minor can be on the same line sometimes).
This script also assumes that the middle name is just an initial.
It does not consider names with both upper and lower case: i.e. McMiller
"""
import pandas as pd
import FunctionsforPerLineData as func

def main():
    #get user to inpur txt file location
    #file_loc = input('Enter file location. Use double \\ for backslash: ')
    #file1 = open(file_loc, encoding="utf8")

    file1 = open("C:\\Users\\alto0\\Documents\\Research Download\\Python\\Fort Hays State University\\FortHaysStateUniversity_1921.txt", encoding="utf8")
        
    file_in_list =[]
    for line in file1:
        #print(type(line))

        #Then we only lock at the first two words in the line because this generally contains the name
        first_words=str(line.split()[:2])
        if(func.extract_wanted_data(first_words, line)): 
            #only append the lines with desired data (names, major, etc.)
            file_in_list.append(line) 

    #should change the following column names as needed
    csv_columns= ['First Name', 'Last Name', 'Home Town', 'Class Standing']

    #create a our dataframe
    senior_data=pd.DataFrame(columns =csv_columns) 

    class_standing = "Senior"

    for i,line in enumerate(file_in_list):
        data_dict={}
        if('Major' in line or 'Minor' in line): 
            # if we are on line with major info, then we skip this iteration
            # because we already gathered this data previously (see how get_major_minor function works to understand)
            continue
        
        # to determine the class standing if non-seniors are in the data
        if (line == "Junior\n"):
            class_standing = "Junior"
        elif (line == "Sophomore\n"):
            class_standing = "Sophomore"
        elif (line == "Freshmen\n"):
            class_standing = "Freshmen"
        
        data_dict["Class Standing"] = class_standing
        
        #we split the line into a list of strings
        data=line.split()

        if len(data)==1: #if line only has one word, then it is probably not our desired data so we skip
            continue

        #see the FunctionsforPerLineData file for function descriptions
        data_dict=func.get_name_hometown(data, data_dict)

        data_dict=func.get_major_minor(file_in_list, data_dict, senior_data, i)

        senior_data=func.add_data_to_df(senior_data,data_dict)

    #convert the dataframe to a csv file
    #the file name should be changed accordingly
    senior_data.to_csv("FortHaysStateUniversity_1921.csv") 

if __name__=="__main__":
    main()