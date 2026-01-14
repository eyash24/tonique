from tonique.expense import Person, Group

# Creating members who
pid = 100
p_a = Person('A', pid=pid)
p_b = Person('B', pid=pid+1)
p_c = Person('C', pid=pid+2)
p_d = Person('D', pid=pid+3)

# members list
member_list = [p_a, p_b, p_c, p_d] 

# initialing group with existing members
grp = Group('Trip 1', members=member_list)

## checking members
grp_members = grp.get_members()

for mem in grp_members:
    print(f'Name: {mem.get_name()}, pending: {mem.check_pending()}')

# Make a list of transactions undertaken by the group
list_transactions = [
    [2562, p_a, [p_a, p_b, p_c], True],
    [6490, p_b, [p_a, p_b, p_c, p_d], True],
    [1812, p_d, [p_a, p_b, p_c, p_d], True],
    [5000, p_c, [p_a, p_b, p_c, p_d], True],
    [1680, p_a, [p_b, p_d], True],
]

# Adding transactions into the group
error_res = False
for transaction in list_transactions:
    print(f'Transaction detail: ', transaction)
    res = grp.add_transaction(*transaction)
    print(res)

else:
    print('All transactions have been run!')


# checking new pendings
grp_members = grp.get_members()
for mem in grp_members:
    print(f'Name: {mem.get_name()}, pending: {mem.check_pending()}, amount paid: {mem.get_payment_done()}, expense: {mem.get_expense()}')

# getting split from group
split_record = grp.balance()

print('\nSplit record')
for rec in split_record:
    from_person = rec[2]
    amount = rec[1]
    to_person = rec[0]

    print(f'From: {from_person.get_name()}, amount: {amount}, To: {to_person.get_name()}')