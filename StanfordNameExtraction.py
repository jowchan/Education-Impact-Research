#This code utilizes Stanford's name detection module, which is built off of nltk.
#The script only extracts names so far.
import stanza
import pandas as pd
stanza.download('en') # download English model, only for the first run 
nlp = stanza.Pipeline('en') # initialize English neural

def main():
    #replace the file directory as needed
    file1=open("C:\\Users\\alto0\\Documents\\Research Download\\Python\\Kansas State University-selected\\KansasStateUniversity_1906.txt", encoding="utf8")
    list_doc=[]
    """
    doc = nlp('Barack Obama was born in Hawaii.')
    doc_items = doc.entities
    print(doc.entities)
    for span_item in doc_items:
        if span_item.type == 'PERSON':
            print(span_item.text)
    """
    for sentence in file1:
        doc= nlp(sentence)
        doc_items = doc.entities
        #print(doc.entities)
        for span_item in doc_items:
            if span_item.type == 'PERSON': #extract only the names
                list_doc.append(span_item.text)

    #should change the following column names as needed
    csv_columns= ['Name']

    #create a our dataframe
    senior_data=pd.DataFrame(columns =csv_columns) 
    senior_data['Name']= list_doc
    
    #rename the csv file as needed
    senior_data.to_csv("KansasStateUniversity_1906.csv") 
if __name__ == "__main__":
    main()

        



