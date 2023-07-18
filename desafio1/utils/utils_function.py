import os
import csv

def read_csv(csv_file_name,column_names,number):
    
   
    arrayofdict = []
    
    num_rows = None
    with open( csv_file_name, encoding='utf8') as csv_file:
        csv_data = csv.DictReader(csv_file, delimiter=';')
       
      

        
        for  i,item in enumerate(csv_data):
            
            if(i<=number):
                info = {}
                for column in column_names:

                    info[column] = item[column]

                arrayofdict.append(info)
            
    return arrayofdict
         
def write_csv(csv_file_name,mode, column_names, arrayofdict): 
    schools = [] 
                        
    with open(csv_file_name, mode = mode, newline='', encoding='utf8') as csv_file:
        #fieldnames = ['Name', 'Email']
        writer = csv.DictWriter(csv_file, fieldnames=column_names, delimiter= ';')
        if os.path.getsize('./files/completed_data.csv') == 0: 
            writer.writeheader()
        writer.writerows(arrayofdict)
  