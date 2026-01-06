# TODO: improve the status codes and make a note of this in README.md file 

def hello():
    print("Hello from tonique app.")

class Person:
    
    def __init__(self, name, pid, payment_done=0, expense=0):
        self.name = name
        self.pid = pid
        self.payment_done = payment_done
        self.expense = expense
    
    def update_payment_done(self, add_amount):
        self.payment_done += add_amount
        return 202
    
    def update_expense(self, add_amount):
        self.expense += add_amount
        return 202
    
    def check_pending(self):
        amount_pending = self.payment_done - self.payment_receive
        return amount_pending
    
    def get_payment_done(self):
        return self.payment_done
    
    def get_expense(self):
        return self.expense
    

class Group:

    def __init__(self, name, members):
        self.name = name
        self.members = members
    
    def add_member(self, member):
        self.members.append(member)
    
    def remove_member(self, member):
        # check if member owes or is owed any money
        if member.check_pending == 0:
            # moving forward with removal
            self.members.remove(member)
            return 202
        else:
            return 405
            
    def add_transaction(self, amount, paid_by, split_grp, equal_split=True, split_unequally=None):
        # TODO: if equal split false, the unequal_split has to match with the amount paid, \
        # create a function that does this check before initiating this process 

        # adding the payment done by paid_by
        paid_by.update_payment_done(amount)

        # based of split grp, divide splits 
        if equal_split:
            share = amount / len(split_grp)
            for person in split_grp:
                person.update_expense(share)
        
        else:
            for person, share in split_unequally:
                person.update_expense(share)

    def balance(self):
        payment_done = [ (member.get_payment_done, member) for member in self.members ]
        expense = [ (member.get_expense, member) for member in self.members ]

        # TODO: build a min heap and max heap for faster min and max record amount 
        
