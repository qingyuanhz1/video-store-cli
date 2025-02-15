import requests
import datetime

class Customer: 
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")

    def create_customer(self, name="Default name", postal_code="postal code", phone="phone"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()
    
    def list_customers(self): 
        response = requests.get(self.url+"/customers")
        return response.json()
    
    def get_customer(self, name=None, id=None): 
        for customer in self.list_customers(): 
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer
        
        if self.selected_customer == None: 
            return "Could not find customer by that id or name"
        
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()
    
    def update_customer(self,name=None,postal_code=None, phone=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone: 
            phone = self.selected_customer["phone"]

        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()