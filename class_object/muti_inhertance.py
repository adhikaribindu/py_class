class Bank:
    def get_name(self):
        return "Abc Bank"
    
    def get_interest(self):
        return 10
    
class Customer(Bank):
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

class CustomerAccountDetail(Customer,Bank):
    balance=0

    def __init__(self,name,phone_number):
        self.customer=Customer(name=name,phone_number=phone_number)

    def get_balance(self):
        return self.balance
    
    def get_customer_details(self):
        return{
            "name":self.customer.name,
            "phone_number":self.customer.phone_number
        }
    
account_detail=CustomerAccountDetail("ram",212121)
account_detail.get_balance()
account_detail.get_customer_details()