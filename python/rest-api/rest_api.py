
import json

class RestAPI(object):

    data = {}

    def __init__(self, database=None):
        self.data = database

    def get(self, url, payload=None):
        if(url == "/users"):
            if(payload):
                users = json.loads(payload)["users"]
                response = []
                for i in self.data["users"]:
                    if(i["name"] in users):
                        response += [i]
                return json.dumps({"users" : response})
            return json.dumps(self.data)


    def borrow(self,fromuser,touser,amount):
        for i in self.data["users"]:
            if( i["name"] == fromuser):
                i['balance'] += amount
                if( i["owed_by"].get(touser , -1) != -1 ):
                    i["owed_by"][fromuser] += amount
                elif( i["owes"].get(touser , -1) != -1 ):
                    if(i["owes"].get(touser) > amount):
                        i["owes"][touser] -= amount
                    else:
                        i["owed_by"][touser] = amount - i["owes"][touser]
                        del i["owes"][touser]
                else:
                    i["owed_by"][touser] = amount
            if( i['name'] == touser  ):
                i['balance'] -= amount
                if( i["owed_by"].get(fromuser , -1)  != -1 ):
                    if(i["owed_by"].get(fromuser) > amount ):
                        i["owed_by"][fromuser] -= amount
                    else:
                        i["owes"][fromuser] = amount - i["owed_by"][fromuser]
                        del i["owed_by"][fromuser]
                elif(i["owes"].get(fromuser , -1) != -1):
                    i["owes"][fromuser] += amount
                else:
                    i["owes"][fromuser] = amount


    def post(self, url, payload=None):
        if(url == "/add"):
            data = json.loads(payload)
            newuser =[{
                'name': data['user'],
                'owes': {},
                'owed_by': {},
                'balance': 0
            }]
            self.data['users'] = self.data['users'] + newuser

            return json.dumps(newuser[0])
        elif(url == "/iou"):
            data = json.loads(payload)
            self.borrow(data["lender"] , data["borrower"] , data['amount'])
            return self.get("/users" , json.dumps({"users" : [data["lender"] , data["borrower"]]}) )
