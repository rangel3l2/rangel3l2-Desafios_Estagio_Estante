from time import sleep
import utils.driver_manager as dm
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import json
import lxml
from utils.utils_function import *
import model.school as School
def get_basic_data(readed_data, data_state_brazil,acronyms, arrayofdict):
    
    for item in readed_data:
        
        for acronym in acronyms:
            
            

            splited = item['Escola'].split()  
            if (acronym['sigla'] in item['Escola'] and len(acronym['sigla']) == len(splited[0]) ):
            
                
                item['Escola'] = item['Escola'].replace(acronym['sigla'], acronym['nome']).replace('.','')
                          
                        
        for column in data_state_brazil:               
            
            if(column['UF'] == item['UF']):
                item['UF'] = column['ESTADO']
                try:    

                    browser =  dm.set_browser_chrome('https://www.google.com/')
                    browser.find_element            
                    elem = browser.find_element(By.NAME, 'q')
                    elem.clear()
                    elem.send_keys(f"{item['Escola']} CIDADE= {item['Municipio']} ESTADO=  {item['UF']}   {Keys.RETURN} ") 
                    school_data = {} 
                    school_data['Escola'] = browser.find_element(By.CSS_SELECTOR, ".qrShPb").text.upper()
                    school_data['Endereço'] = browser.find_element(By.CSS_SELECTOR, ".LrzXr").text.upper()
                    school_data['Telefone'] = browser.find_element(By.CSS_SELECTOR, '.zdqRlf').text.upper()
                    school_data['Condição'] = True
                    arrayofdict.append( 
                        {'Escola': school_data['Escola'], 'Endereço': school_data['Endereço'], 'Telefone': school_data['Telefone'], 
                        'Condição': school_data['Condição']})       
                except:     
                    arrayofdict.append(
                        {'Escola': item['Escola'] , 'Endereço': 'NÃO ENCONTRADO' , 'Telefone': 'NÃO ENCONTRADO', 
                        'Condição': False}
                    )
       
                 
           
        sleep(2)
    return arrayofdict
def optimized_data_resulted(readed_data):
    arrayofdict = []
    schools = []
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com"
    }
    url = ''
    city = []
    for data in readed_data:
          city.append(data['Municipio'])
    unique_city = {}
    for city in city:
        unique_city[city] = True
    unique_city = list(unique_city.keys())
    for data in readed_data:
        print(unique_city)
        if data['Municipio'] in unique_city:
            
            url = f"https://www.google.com/search?tbs=lf:1,lf_ui:2&tbm=lcl&q=escola+publica+{data['Municipio']}+ {data['UF']}&rflfq=1&num=10&sa=X&ved=2ahUKEwib54Csgfz_AhVLLbkGHWDrB64QjGp6BAgaEAE&cshid=1688712851262688&biw=1292&bih=636&dpr=1#rlfi=hd:;si:;mv:[[-20.708819727811274,-51.29209920456627],[-21.017440937275275,-51.89085408737877]]"
            print(url)
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser') 
            name_school = soup.find_all("span", {"class":"OSrXXb"})    
            cards = soup.select("div.rllt__details:last-child")
            address = soup.find_all('')


            for item in cards:
                dict_school = {
                    'Escola': '',
                    'Telefone': '',
                    'Endereço': '',
                    'Condição': False
                }
                try:  
                    data = item.text
                    splited_data = data.split(" · ")                    
                    dict_school['Escola'] = splited_data[0]
                    for char in dict_school['Escola']:
                        if char.isdigit():
                            dict_school['Escola'] =  dict_school['Escola'].replace(char, '').replace(',()', '')
                    for char in splited_data[1]:
                        if '(' and char.isdigit() and ')':
                            dict_school['Telefone'] = splited_data[1] or ''                
                            dict_school['Endereço'] = splited_data[2].replace('pública', '').replace('Escola','')
                    for char in splited_data[2]:
                        if '(' and char.isdigit() and ')':
                            dict_school['Telefone'] = splited_data[2] or ''                
                            dict_school['Endereço'] = splited_data[1].replace('Escola','').replace('pública', '')



                except IndexError:
                    dict_school['Condição'] = True
                    if not dict_school['Telefone']:
                        dict_school['Telefone']
                    if not dict_school['Endereço']:
                        dict_school['Endereço'] = 'Não encontrado valor'    

                finally:
                    arrayofdict.append(dict_school) 

               

    name_school_csv = []
    for data in readed_data:
        name_school_csv.append(data['Escola'].upper()) 
    
    for item in arrayofdict:
        
        if  item['Escola'].upper() not in name_school_csv:
            print(item['Escola'])
            school = School.School(item['Escola'], item['Endereço'], item['Telefone'], item['Condição'])
            schools.append({"Escola": school.school_name, "Endereço": school.school_address, "Telefone": school.school_phone, "Condição": school.school_status})
                            
    write_csv('./files/completed_data.csv','a', ['Escola', 'Endereço', 'Telefone', 'Condição'], schools)

