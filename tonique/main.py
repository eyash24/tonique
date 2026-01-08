# TODO: improve the status codes and make a note of this in README.md file 
# TODO: Create a display function showcasing a matrix type display

from typing import List

'''
Docstring for tonique.main

Function response format 
( status code, status message custom to each function )
'''


def total_sum(li):
    res = 0
    for l in li:
        res += l[0]
    return res

def hello():
    print("Hello from tonique app!")

class Person:
    # Group Level
    
    def __init__(self, name, pid, payment_done=0, expense=0):
        self.pid = pid
        self.name = name
        self.payment_done = payment_done
        self.expense = expense

    def update_payment_done(self, add_amount):
        self.payment_done += add_amount
        return (202, f'Payment updated successfully for {self.name}')
    
    def update_expense(self, add_amount):
        self.expense += add_amount
        return (202, f'Expense updated successfully for {self.name}')
    
    def check_pending(self):
        amount_pending = self.payment_done - self.expense
        return amount_pending
    
    def get_payment_done(self):
        return self.payment_done
    
    def get_expense(self):
        return self.expense
    
    def get_name(self):
        return self.name

    def update_name(self, name):
        old_name = self.name
        self.name = name
        return (202, f'Member name changes successful from {old_name} to {self.name}.')

    def get_pid(self):
        return self.pid


class GroupMember(Person):
    ## App level

    def __init__(self, name, payment_done=0, expense=0, grp=None):
        super().__init__(name, payment_done, expense)
        # grp is a dictionary key: grp object, value : Person Object
        self.grp = grp
    
    def get_grp(self):
        return self.grp

    def add_grp(self, grp, pid):
        if self.grp is None:
            self.grp = dict()
            self.grp[grp] = pid
        else:
            self.grp[grp] = pid
        return (202, f'Person {self.name} aligned with Group {grp.get_name()}')
    
    def remove_grp(self, grp):
        if self.grp is None:
            return (405, f'Group {grp.get_name()} not aligned with Person {self.name}')
        
        elif grp not in self.grp:
            return (405, f'Group {grp.get_name()} not aligned with Person {self.name}')
        
        else:
            # remove from desired group only if they dont owe anyone or are owed any money from any other group member
            grp_member = self.grp[grp]
            # if grp_member.check_pending == 0:
            #     # safe to remove    
            #     self.grp.pop(grp)
            #     return (202, f'Person {self.name} successfully unaligned from Group {grp.get_name()}')

            # else:
            #     # not safe to remove said member from grp
            #     return (405, f'Member {self.name} has pending amount {grp_member.check_pending()} in Group {grp.get_name()}')
        
            # OR
            return grp.remove_member(grp_member)

     
class Group:

    def __init__(self, name: str, members: List[GroupMember]):
        self.name = name
        self.members = members
    
    def get_name(self):
        return self.name
    
    def get_members(self):
        return self.members

    def check_member(self, member):
        return member in self.members
    
    def add_member(self, member):
        self.members.append(member)
        return (202, f'Member {member.get_name()} successfully added in Group {self.name}')
    
    def remove_member(self, member):
        # check if member owe or is owed any money
        if member.check_pending() == 0:
            # moving forward with removal
            self.members.remove(member)
            return (202, f'Member {member.get_name()} removed successfully from Group {self.name}')
        
        else:
            return (405, f'Member {member.get_name()} has pending amount {member.check_pending()} in Group {self.name}')
            
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
        pendings = [ (member.check_pending(), member) for member in self.members ]

        # TODO: build a min heap and max heap for faster min and max record amount 
        # TODO: draft of the working w/o using heap -> use sort methods instead

        # split expense into to recieve and to pay
        recieve = list()
        pay = list()
        sorted = list()

        for acct in pendings:
            if acct[0] == 0:
                sorted.append(acct)
            elif acct[0] > 0: # more ammount paid then the expense 
                recieve.append(acct)
            else: # expense is more than what they have paid
                pay.append(-1*acct)
        
        # sorting each list
        recieve.sort(reverse=True)
        pay.sort()
        
        # transaction record list of (from, amount, to)
        transaction_record = list()

        if total_sum(recieve) == total_sum(pay):
            # total recieve matches total pay
            for receive_amount, person_receive in recieve:

                while True:
                    pay.sort()
                    (amount_pay, person_paying) = pay.pop(0)
                    
                    if receive_amount < amount_pay:
                        transaction_record.append((person_receive, receive_amount, person_paying))
                        # append surplus of amount_pay back to pay list 
                        pay.append((amount_pay - receive_amount, person_paying))
                        break # exit while loop
                    
                    elif receive_amount == amount_pay:
                        transaction_record.append((person_receive, amount_pay, person_paying))
                        break

                    elif receive_amount > amount_pay:
                        # need more funds
                        transaction_record.append((person_receive, amount_pay, person_paying))
                        receive_amount = receive_amount - amount_pay
        else:
            # recieve does not match with pay
            return (405, f'Receive does not match with Pay for Group {self.name}')

        return transaction_record


class App:
    def __init__(self):
        pass

                
                






        





        
