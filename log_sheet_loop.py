size2 = 2
size3 = 3
size4 = 4
size5 = 5
ticket = 158
qty2 = 6512
qty3 = 3212
qty4 = 4200
qty5 = 5200
order = "401586"
i = 1

while ticket <= qty2:
    print(order,i,size2, ticket)
    i = i+1
    qty2 -= ticket
    if qty2 <158:
        print(order,i,size2, qty2)

while ticket <= qty3:
    print(order,i,size3,ticket)
    i = i+1
    qty3 -= ticket
    if qty3 <158:
        print(order,i,size3,qty3)

while ticket <= qty4:
    print(order,i,size4,ticket)
    i = i+1
    qty4 -= ticket
    if qty4 <158:
        print(order,i,size4,qty3)

while ticket <= qty5:
    print(order,i,size5,ticket)
    i = i+1
    qty5 -= ticket
    if qty5 <158:
        print(order,i,size5,qty3)
