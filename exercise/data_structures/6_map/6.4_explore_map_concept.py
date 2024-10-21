"""Time to play with Python dictionaries! You're going to work on a dictionary that stores cities by country and continent. The following one is done for you - the city of Mountain View is in the USA, which is in North America.

locations = {'North America': {'USA': ['Mountain View']}}

Notice that:

locations is a dictionary of dictionaries
North America (Continent) is a dictionary
USA (Country) is a key
['Mountain View'] (City) is a list acting as a value. A new city within USA country can be "appended" to the given list.
Task 1
You need to add the cities listed below by modifying the given structure. Cities to add:

Bangalore (India, Asia)
New Delhi (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)
Be careful, while adding a city in an existing country. Consider adding it to the existing list of cities as:

locations['Asia']['India'].append('New Delhi')
Task 2
Print the following (using "print") by looking them up in the structure.

A list of all cities in the USA in alphabetic order.
All cities in Asia, in alphabetic order, next to the name of the country. In your output, label each answer with a number so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
# Code

locations = {'North America': {'USA': ['Mountain View']}}

# TODO: Print a list of all cities in the USA in alphabetic order.
"""
Bangalore (India, Asia)
New Delhi (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['India'].append('New Delhi')
locations['North America']['USA'].append('Atlanta')
locations['Africa'] = {'Egypt': ['Cairo']}
locations['Asia']['China'] = ['Shanghai']
print(locations)

usa_city = []
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    usa_city.append(city)
print(usa_city)
# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
asia_citys = []
asia_country_sorted = locations['Asia']
for country, citys in asia_country_sorted.items():
    for city in citys:
        asia_citys.append("{} - {}".format(city , country))
asia_citys = sorted(asia_citys)
print(asia_citys)
