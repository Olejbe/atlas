import csv
from main.settings import BASE_DIR
from countries.models import Country, Continent


def populate_database() -> None:
    """
    populates the Continent and Country Table with basic facts from csv.
    :return: None
    """
    continents = ['asia', 'africa', 'europe', 'north-america', 'south-america', 'oceania']
    for continent in continents:
        Continent.objects.update_or_create(name=continent)

    with open(f'{BASE_DIR}\\countries\\utils\\country.csv', 'r') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in file_reader:
            if row[0] != 'Country':
                continent = Continent.objects.get(name=row[4])
                name = row[0]
                pop = int(row[1])
                land_a = int(row[2])
                pop_d = int(row[3])
                alpha2 =row[5]
                alpha3 =row[6]
                capital = row[7]
                Country.objects.create(name=name, capital=capital, population=pop, land_area=land_a, population_density=pop_d,
                                       continent=continent, alpha_2=alpha2, alpha_3=alpha3)
                print(f"imported {name}")
            else:
                print("Skipped header")

