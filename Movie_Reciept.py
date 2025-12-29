name = input("What movie are you looking for? ")
tickets = int(input("How many tickets do you need? "))
snacks = input("Would you want snacks? (yes/no) ")
price_ticket = 12.00
price_snack = 5.00
total_price = (tickets*price_ticket)
if snacks == "yes":
    total_price += (tickets*price_snack)
total_price += (total_price*0.07)
print(f"\n     {name} Receipt")
print("--------------------------------")
print(f"        Movie: {name}")
print(
    f"        Tickets: {tickets} x ${price_ticket} = ${tickets*price_ticket}")
print(
    f"        Snacks: {tickets} x ${price_snack} = ${tickets*price_snack if snacks == 'yes' else 0}")
print(f"        Tax: 7% = ${total_price}")
print("--------------------------------")
print(f"        Total: ${total_price}")
