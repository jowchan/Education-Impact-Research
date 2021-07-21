"""
The following script contains the functions needed for the file PerLineDataAlt
"""
import re
"""
list_to_string converts a list into a string object
@param list_container the list
@return str_object the string
"""
def list_to_string (list_container):
    str_object=""
    for item in list_container:
        str_object += item
        str_object +=' '
        #not sure why .join does not work here...
    return str_object

"""
add_data_to_df adds the row of data into the dataframe
@param dataframe the dataframe to append to
@dictionary_data the dictionary that contains the data
@return dataframe the dataframe
"""
def add_data_to_df(dataframe, dictionary_data):
    dataframe=dataframe.append(dictionary_data, ignore_index=True) #add data as a row
    return dataframe


"""
extract_wanted_data searches for the specific data desired within the file
@param first_words the first words in a string of data
@return boolean
"""
def extract_wanted_data(first_words, str):
    if( first_words.isupper() or first_words.istitle()
    or ('Major' in str) or ('Minor' in str)):
    #Genearlly, names have only the first letter capitalized or all capitalized
        return True


    
"""
get_name_hometown extracts the name and hometown of individual and stores it into a dictionary
@param list_container the list containing our desired data
@param dictionary_data the dictionary we want to add our data into
@return dictionary_data the dictionary with our data
"""
"""
def get_name_hometown(list_container, dictionary_data):
    #should change according to order of name and hometown listed
    dictionary_data['First Name']=list_container[1]
    dictionary_data['Middle Name']='N/A'
    try:
        dictionary_data['Last Name']=list_container[0] 
        dictionary_data['Home Town']=list_to_string(list_container[2:])
    except: #this is for people with only First and Last names
        dictionary_data['Last Name']=list_container[1]
        dictionary_data['Middle Name']= 'N/A'
        dictionary_data['Home Town']=list_to_string(list_container[2:]) #Note: hometown value becomes a list

    #now if middle name is more than just a letter, then its not a middle name. It is the last name.
    if (len(dictionary_data['Middle Name']) >2) and (dictionary_data['Middle Name'] != 'N/A'):
        dictionary_data['Last Name'] = dictionary_data['Middle Name']
        dictionary_data['Middle Name']= 'N/A'
        dictionary_data['Home Town']= list_to_string(list_container[2:])
    return dictionary_data
"""

def get_name_hometown(list_container, dictionary_data):
    # cut the list of data up to and including where — appears
    if ("—" in list_container):
        cut_off_index = list_container.index("—")
        list_container = list_container[: cut_off_index + 1]

    #should change according to order of name and hometown listed
    if (len(list_container) ==2): # then only first and last name available
        dictionary_data['First Name']=list_container[0]
        #dictionary_data['Middle Name']='N/A'
        dictionary_data['Last Name'] = list_container[1]
        dictionary_data['Home Town']= 'N/A'

    elif (len(list_container)- 1) == 2: # then first, last name and hometown available
        # the -1 is to count the remaining contents of the container, not including the hometown
        dictionary_data['First Name']=list_container[0]
        #dictionary_data['Middle Name']='N/A'
        dictionary_data['Last Name'] = list_container[1]
        dictionary_data['Home Town']=list_container[-1]

    elif (len(list_container)- 1) == 3: # then full first, middle, and last name + hometown available
        dictionary_data['First Name']=list_container[0]
       # dictionary_data['Middle Name']=list_container[1]
        dictionary_data['Last Name'] = list_container[1]
        dictionary_data['Home Town']=list_container[-1]
    
    elif (len(list_container)- 1) >= 4: # most likely hometown is more than one word
        if list_container[0] == 'Mrs.' or list_container[0] == 'Mr.': #if first word is a prefix
            dictionary_data['First Name']=list_container[1]
           # dictionary_data['Middle Name']=list_container[2]
            dictionary_data['Last Name'] = list_container[2]
            dictionary_data['Home Town']=list_to_string(list_container[3:]) 
        else:
            dictionary_data['First Name']=list_container[0]
           # dictionary_data['Middle Name']=list_container[1]
            dictionary_data['Last Name'] = list_container[1]
            dictionary_data['Home Town']=list_to_string(list_container[2:]) 
    return dictionary_data


"""
get_major_minor extracts the major and minor data from the line 
@param list_container the list containing our desired data
@param dictionary_data the dictionary we want to add our data into
@param dataframe the dataframe
@index the index of the list being looped through in PerLineDataAlt file
@return dictionary_data the dictionary with our data
"""
def get_major_minor(list_container, dictionary_data, dataframe, index):
    try: #the try is for when we reach close to eof, then we don't over index
            if ('Major' in list_container[index+1]): #look ahead to next line to check if major info is available
                
                if('Minor' in list_container[index+1]): 
                    #then we need to split the line by a ',' that separates our data from other undesirable data
                    major_info=list_container[index+1]
                    major_info=re.split(', |; |\. | —',major_info)
                    major_info[1] = major_info[1][7:] #remove Minor- prefix
                    major_info[0]=major_info[0][6:] #remove Major- prefix
                    dictionary_data['Minor']= major_info[1]
                    dictionary_data['Major']=major_info[0]
                
                else: #otherwise no infomration on minor on the same line
                    dictionary_data['Major']=list_container[index+1][6:]

    except: #if unable to find major information, then this information does not exist
        dictionary_data['Major']='N/A'
        #if no major, then student has no minor as well
        #dictionary_data['Minor']='N/A'

        #add the data to our dataframe
        dataframe=add_data_to_df(dataframe, dictionary_data)

        #we end the function early if guaranteed no minor so that we do not search again
        return dictionary_data 
    """
    if("Minor" not in dictionary_data): #if minor information is still missing, check next line
        try:
            #look ahead by two lines for minor info
            #This is when minor and major are on separate lines
            if ('Minor' in list_container[index + 2]): 
                dictionary_data['Minor']=list_container[index + 2][6:] #remove the 'Minor-' prefix
            else: #otherwise no information on minor is available
                dictionary_data['Minor']='N/A'

        except: #this is needed if the 'try block' does not run
            dictionary_data['Minor']='N/A'
    """
    return dictionary_data







