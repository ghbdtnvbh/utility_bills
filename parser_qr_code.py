import os
import csv
import json
import datetime

receipt_list = []
date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
fieldnames = ['DateTime', 'Name', 'BankName', 'PersonalAcc','Sum','Contract','CorrespAcc', 'Category', 
    'Pr1', 'PayeeINN', 'NCounters', 'BIC', 'SP1', 'PrK1', 'PersAcc',
    'NPr','MiddleName', 'LastName', 'PayerAddress', 'FirstName', 'InstNum', 'QuittDate', 'ServiceName']

def parser(receipt):
    receipt_prepared  = receipt.replace( '"', "").replace(' ', '_').replace( "=", " ").split('|')

    for i in receipt_prepared[1:]:
        receipt_list.append(i.split())
    
    list_to_dict = dict(receipt_list)
    list_to_dict.update({'DateTime': date_time})

    with open("qr_data.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames)
        if os.stat("qr_data.csv").st_size > 0:
            file_writer.writerow(list_to_dict)
        else:
            file_writer.writeheader()
            file_writer.writerow(list_to_dict)

    with open("qr.json", "a") as json_file:
        json.dump(list_to_dict, json_file, indent=4, ensure_ascii=False)
