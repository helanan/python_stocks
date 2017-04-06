#dictionaries are index by keys (associative arrays), immutable
#strings and numbers can always be keys
#cant use lists as keys

stockDict = { 'GE':'General Electric', 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':'Eastman Kodak', 'AZ': 'Amazon', 'HN':'Helana Nosrat', 'NS':'Nashville Software School'}

purchases = [ ( 'GE', 100, '10-sep-2001', 48),
( 'CAT', 100, '1-apr-1999', 25),
( 'GM', 200, '1-jul-1998', 56),
( 'EK', 300, '2-feb-2017', 60),
( 'AZ', 400, '3-march-2017', 70),
( 'HN', 500, '4-april-2017', 92),
( 'NS', 600, '5-may-2017', 33)]

# basic relational database join algorithm
portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]

    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

    print("I purchased {} stocks for ${}".format(full_company_name, full_purchase_price))
    print("-------------------------")

    try:
        portfolio[ticker].append(purchase) #append the purchase to the ticker list
    except KeyError:
        portfolio[ticker] = list() #if they dont exist yet create it
        portfolio[ticker].append(purchase)
    print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))

for ticker,purchases in portfolio.items():
    print("------------{}-------------".format(ticker))
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
    print("   {}".format(purchase))
    print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))

#print(portfolio)
#program makes one pass through the data to create the dict
