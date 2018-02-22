import os
import json

clear = lambda: os.system('cls')

with open('offer_data.json', 'r') as data_file:
    json_data = data_file.read()

arr = json.loads(json_data)

print(len(arr))

e_commerce = []
fashion = []
food_and_beverage = []
travel = []
entertainment = []
health = []

general = []


def label():
    myName = input("Whats your name: ")

    for offer in arr:
        print("Make a choice for: ")
        print(offer)
        print("1. e_commerce")
        print("2. fashion")
        print("3. food_and_beverage")
        print("4. travel")
        print("5. entertainment")
        print("6. health")
        choice = input("Make a choice: ")
        if choice == '1':
            e_commerce.append(offer)
        elif choice == '2':
            fashion.append(offer)
        elif choice == '3':
            food_and_beverage.append(offer)
        elif choice == '4':
            travel.append(offer)
        elif choice == '5':
            entertainment.append(offer)
        elif choice == '6':
            health.append(offer)
        elif choice == '-1':
            break
        else:
            print("UnKnown Option !!")
            general.append(offer)
        print("#################################")

    with open('e_commerce-' + myName + '.json', 'w') as outfile:
        json.dump(e_commerce, outfile)

    with open('fashion-' + myName + '.json', 'w') as outfile:
        json.dump(fashion, outfile)

    with open('food_and_beverage-' + myName + '.json', 'w') as outfile:
        json.dump(food_and_beverage, outfile)

    with open('travel-' + myName + '.json', 'w') as outfile:
        json.dump(travel, outfile)

    with open('entertainment-' + myName + '.json', 'w') as outfile:
        json.dump(entertainment, outfile)

    with open('health-' + myName + '.json', 'w') as outfile:
        json.dump(health, outfile)

    with open('general-' + myName + '.json', 'w') as outfile:
        json.dump(general, outfile)


def redist():
    m = []
    c = []
    with open('offer_data.json', 'r') as data_file:
        json_data = data_file.read()

    arr = json.loads(json_data)
    count = 0
    for data in arr:
        count += 1
        if count <= len(arr) * 0.6:
            m.append(data)
        else:
            c.append(data)

    with open('train.json', 'w') as outfile:
        json.dump(m, outfile)

    with open('test.json', 'w') as outfile:
        json.dump(c, outfile)

        #fa5791ac-829e-4c81-85db-a9a5f6ff2874
