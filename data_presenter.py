invoices = open('CupcakeInvoices.csv')

# for line in invoices:
#     line = line.split(',')
#     print(line[2])


total = []
for line in invoices:
    cupNumber = []
    line = line.rstrip('\n').split(',')
    cupcakes = float(line[3])
    # cupNumber.append(cupcakes)
    # price = float(line[4])
    sumi = float(line[3])*float(line[4])
    # print(sum)
    total.append(sumi)

# def make_total() 
total_total = sum(total)
print(round(total_total,2))

# print(sum)