# rainfall capture 

def get_rainfall():

    rainfall_db = {}
    
    while True:
        city = input('city: ')

        if not city:
            break

        rainfall = int(input('rainfall: '))

        if city in rainfall_db:
            rainfall_db[city] += rainfall
        else:
            rainfall_db[city] = rainfall
    print('\n\n------ Report ---------\n')
    for city in rainfall_db:
        print(f'{city} : {rainfall_db[city]}')


get_rainfall()