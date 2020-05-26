import json



def writeData(account_Name, phone_Number, password):
    def write_json(data, filename='data.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4) 
      
      
    with open('data.json') as json_file: 
        data = json.load(json_file) 
      
        temp = data['Persons'] 
  
        # python object to be appended 
        y = {"account_Name":account_Name, 
            "phone_Number": phone_Number, 
            "password": password
            } 
        # appending data to emp_details  
        temp.append(y) 
      
    write_json(data)  

def printData():
    with open('data.json') as json_file:
        data = json.load(json_file)
    for p in data['Persons']:
        print('Account Name: ' + p['account_Name'])
        print('Phone Number: ' + p['phone_Number'])
        print('Password: ' + p['password'])
        print('')

def getData():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return(data['Persons'])

