

import csv
import model.school as School
from utils.utils_function import *
from webscraping import *
import os        
def main():
    schools = []
    arrayofdict = []
    quantity_data = 1
    
    array_column = ['Escola','Municipio','UF']
    readed_data = read_csv('files/base_escolas_inep.csv',
                             array_column,quantity_data)        
    data_state_brazil = read_csv('files/estados_brasil.csv',
                             ['UF','ESTADO'],26)
    acronym_name_school = read_csv('files/tratamento_nomes_siglas.csv',
                             ['nome','sigla', 'restricao'],18) 
    for item in get_basic_data(readed_data, data_state_brazil,acronym_name_school, arrayofdict):
        
        school = School.School(item['Escola'], item['Endereço'], item['Telefone'], item['Condição'])
        schools.append({"Escola": school.school_name, "Endereço": school.school_address, "Telefone": school.school_phone, "Condição": school.school_status})

   
    if os.path.getsize('./files/completed_data.csv') == 0:
        write_csv('./files/completed_data.csv','w', ['Escola', 'Endereço', 'Telefone', 'Condição'], schools)
    optimized_data_resulted(readed_data)
    
   

    
    
   
main()    
      
   