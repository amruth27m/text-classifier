import os
import json

clear = lambda: os.system('cls')





def label():
    
    myName = ''
    print("What is your name?")
    print("1. Balaji")
    print("2. Amruth")
    print("3. Adil")
    choice = input("Enter choice: ")
    
    if(choice == '1'):
        os.chdir('balaji')
    elif(choice == '2'):
        os.chdir('amruth')
    elif(choice == '3'):
        os.chdir('adil')
    else:
        print("Wrong choice")
        return
    
    with open('data.json', 'r') as data_file:
        json_data = data_file.read()

    arr = json.loads(json_data)
    
    e_commerce = json.loads(open('e_commerce-.json').read())
    fashion = json.loads(open('fashion-.json').read())
    food_and_beverage = json.loads(open('food_and_beverage-.json').read())
    travel = json.loads(open('travel-.json').read())
    entertainment = json.loads(open('entertainment-.json').read())
    health = json.loads(open('health-.json').read())

    general = json.loads(open('general-.json').read())
    
    print("Number of records to be classified: " + str(len(arr)))
    
    for ctr in range(len(arr)):
        offer = arr[ctr]
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
    
    os.remove('data.json')
    
    remaining = []
    while ctr < len(arr):
        remaining.append(arr[ctr])
        ctr += 1
        
    print("Remaining SMS to be classified: " + str(len(remaining)))
        
    with open('data.json', 'w') as outfile:    
        json.dump(remaining, outfile)
        
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

label()
        
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
