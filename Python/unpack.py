def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

coins_dict = {
    "galleons": 100,
    "knuts": 25,
    "sickles": 50
}

# unpacking the items of list using * 
print(total(*coins), "Knuts")

# unpacking the items of dict using * 
print(total(**coins_dict), "Knuts")