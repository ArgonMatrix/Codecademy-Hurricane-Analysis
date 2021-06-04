# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1. Update Recorded Damages
# Function for converting values in 'damages' list to be represented as floats instead of as strings.
def convert_damages(damages_list):
    updated_damages = []
    for damages_string in damages_list:
        final_char = damages_string[-1]
        dollar_value = damages_string

        if final_char == 'M':
            dollar_value = float(damages_string[:-1]) * (10**6)
        elif final_char == 'B':
            dollar_value = float(damages_string[:-1]) * (10**9)
        
        updated_damages.append(dollar_value)
    
    return updated_damages

# Helper function to convert float values into more readable dollar value representations.
# Returns non-float values unchanged.
def dollarize(dollar_value):
    if not isinstance(dollar_value, float):
        return dollar_value

    dollars_and_cents = str(dollar_value).split('.')
    dollars = dollars_and_cents[0]
    cents = dollars_and_cents[1]

    if len(cents) < 2:
        cents += '0' # Add trailing 0 to make the value more readable as money.
    if len(dollars) > 3:
        fragments = [] # List for holding 'parts' of the dollar value to be joined by commas later.
        remaining_digits = dollars
        while len(remaining_digits) > 3:
            fragments.insert(0, remaining_digits[-3:])
            remaining_digits = remaining_digits[:-3]
        fragments.insert(0, remaining_digits)

        dollars = ','.join(fragments)
    
    return '$' + dollars + '.' + cents

# Convert damages
damages = convert_damages(damages)


# 2. Create Dictionary of Hurricanes
# Function that combines lists of relevant hurricane data into a dictionary. Keys are hurricane names as strings, values are dictionaries containing the remaining data.
def create_dictionary(names, months, years, winds, areas, damages, deaths):
    hurricane_dict = {}
    for index in range(len(names)):
        hurricane_dict[names[index]] = {
            "Name": names[index],
            "Month": months[index],
            "Year": years[index],
            "Max Sustained Wind": winds[index],
            "Areas Affected": areas[index],
            "Damages": damages[index],
            "Deaths": deaths[index]
        }
    
    return hurricane_dict

# Call function on given data
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
# Print data in a readable manner
for (name, info) in hurricanes.items():
    blurb = \
"""Hurricane {name}
-----------------------
Date: {month}, {year}
Maximum Sustained Wind Speed: {wind} MPH
Areas Affected: {areas}
Damages (USD): {damages}
Total Deaths: {deaths}
        """.format(
            name=name,
            month=info["Month"],
            year=info["Year"],
            wind=info["Max Sustained Wind"],
            areas=', '.join(info["Areas Affected"]),
            damages=dollarize(info["Damages"]),
            deaths=info["Deaths"]
        )
    print(blurb)

# Helper function for printing a visual buffer between sections of information
def print_buffer(buffer_string, line_count):
    for i in range(line_count):
        print(buffer_string)
    print('')
# Function call
buffer_line = "**********************************"
print_buffer(buffer_line, 2)


# 3. Hurricanes by Year
# Function to convert existing hurricanes dictionary to be sorted by year.
def sort_by_year(hurricane_dict):
    sorted_hurricanes = {}
    for info in hurricane_dict.values():
        year = info["Year"]
        # Check if the year exists in the dictionary already.
        if year in sorted_hurricanes:
            sorted_hurricanes[year].append(info)
        else:
            sorted_hurricanes[year] = [info]
    
    return sorted_hurricanes

# Apply Function & Print Data
hurricanes_by_year = sort_by_year(hurricanes)
for (year, hurricane_list) in hurricanes_by_year.items():
    names = [info["Name"] for info in hurricane_list]
    blurb = \
"""{year} Hurricanes
-----------------------
{names}
""".format(
    year=year,
    names=', '.join(names)
)
    print(blurb)

# Print buffer
print_buffer(buffer_line, 2)


# 4. Counting Affected Areas
# Function to take hurricanes dictionary and count how many times each listed area has been affected.
# Returns a dictionary where the keys are strings representing affected areas and the values are integers representing how many times they appear in the hurricanes dictionary.
def count_areas(hurricane_dict):
    area_dict = {}
    for info in hurricane_dict.values():
        for area in info["Areas Affected"]:
            if area in area_dict:
                area_dict[area] += 1
            else:
                area_dict[area] = 1
    
    return area_dict

# Apply Function & Print Data
areas_by_count = count_areas(hurricanes)
for (area, count) in areas_by_count.items():
    print("The area of {area} has been struck by a total of {count} category five hurricanes.".format(area=area, count=count))

# Print Buffer
print('')
print_buffer(buffer_line, 2)


# 5. Find Most Affected Areas
# Function that takes the dictionary of affected areas by count and determines the area that has been struck most often.
# Returns a dictionary containing a list of areas tied for the most hurricanes (list has only one element if there are no ties) and the count for how many times those areas
# were struck.
def find_most_affected_areas(area_dict):
    area_list = []
    max_count = 0
    for (area, count) in area_dict.items():
        if count > max_count:
            area_list = [area]
            max_count = count
        elif count == max_count:
            area_list.append(area)
    
    return {"Areas": area_list, "Count": max_count}

# Apply the function & print the results.
most_affected_areas = find_most_affected_areas(areas_by_count)
if len(most_affected_areas["Areas"]) > 1:
    print("The areas that have been most affected by category five hurricanes, having been struck by {count} in total, are {areas} and {final_area}.".format(
        count=most_affected_areas["Count"],
        areas=', '.join(most_affected_areas["Areas"][:-1]),
        final_area=most_affected_areas["Areas"][-1]
    ))
else:
    print("The area most affected by category five hurricanes, having been struck by {count} in total, is {area}.".format(
        count=most_affected_areas["Count"],
        area=most_affected_areas["Areas"][0]
    ))

# 6. Find the Deadliest Hurricane
# Function that searches the hurricanes dictionary for the highest number of deaths. Returns a dictionary containing a list of hurricanes tied for the most deaths (list will contain
# only one element if there are no ties) and the count for how many deaths those hurricanes each caused.
def find_deadliest_hurricanes(hurricane_dict):
    hurricane_list = []
    max_deaths = 0
    for info in hurricane_dict.values():
        hurricane = info["Name"]
        death_count = info["Deaths"]
        if death_count > max_deaths:
            hurricane_list = [hurricane]
            max_deaths = death_count
        elif death_count == max_deaths:
            hurricane_list.append(hurricane)
    
    return {"Hurricanes": hurricane_list, "Deaths": max_deaths}

# Apply the function & print the results
deadliest_hurricanes = find_deadliest_hurricanes(hurricanes)
if len(deadliest_hurricanes["Hurricanes"]) > 1:
    print("The deadliest category five hurricanes, having each caused {deaths} deaths, were Hurricane {hurricanes} and Hurricane {final_hurricane}.".format(
        deaths=deadliest_hurricanes["Deaths"],
        hurricanes=', Hurricane '.join(deadliest_hurricanes["Hurricanes"][:-1]),
        final_hurricane=deadliest_hurricanes["Hurricanes"][-1]
    ))
else:
    print("The deadliest category five hurricane, having caused a total of {deaths} deaths, was Hurricane {hurricane}.".format(
        deaths=deadliest_hurricanes["Deaths"],
        hurricane=deadliest_hurricanes["Hurricanes"][0]
    ))


# 7. Find the Costliest Hurricane
# Function to search the dictionary of hurricanes for the one that caused the highest dollar value of damages. Returns a dictionary containing a list of costliest hurricanes
# (list will contain only one element if there are no ties) as well as a float representing the dollar value of the damages caused.
def find_costliest_hurricanes(hurricane_dict):
    hurricane_list = []
    max_cost = 0
    for info in hurricane_dict.values():
        hurricane = info["Name"]
        cost = info["Damages"]
        # Check to confirm the cost is a float instead of "Damages not recorded."
        if not isinstance(cost, float):
            continue

        if cost > max_cost:
            hurricane_list = [hurricane]
            max_cost = cost
        elif cost == max_cost:
            hurricane_list.append(hurricane)
    
    return {"Hurricanes": hurricane_list, "Damages": max_cost}

# Apply the function & print the results
costliest_hurricanes = find_costliest_hurricanes(hurricanes)
if len(costliest_hurricanes["Hurricanes"]) > 1:
    print("The category five hurricanes that caused the most damage, each having caused approximately {damages} in damages, were Hurricane {hurricanes} and Hurricane {final_hurricane}.".format(
        damages=dollarize(costliest_hurricanes["Damages"]),
        hurricanes=', Hurricane '.join(costliest_hurricanes["Hurricanes"][:-1]),
        final_hurricane=costliest_hurricanes["Hurricanes"][-1]
    ))
else:
    print("The category five hurricane that caused the most damage, having resulted in {damages} in damages, was Hurricane {hurricane}.".format(
        damages=dollarize(costliest_hurricanes["Damages"]),
        hurricane=costliest_hurricanes["Hurricanes"][0]
    ))

# Print Buffer + Extra New Line
print('')
print_buffer(buffer_line, 2)


# 8. Categorize Hurricanes by Mortality
# Mortality Scale: Used to rate hurricanes based on how many deaths they caused. The values of the dictionary are the upper threshold for that specific index of the scale.
# Hurricanes that cause more deaths than the upper threshold for index 4 will be categorized as index 5.
mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000
}
# Function that takes the info for an individual hurricane and returns a mortality rating based on the number of deaths it caused.
def find_mortality_rating(hurricane_info):
    # Default rating to five, then compare deaths to thresholds to determine whether the rating should be lowered.
    mortality_index = 5
    deaths = hurricane_info["Deaths"]
    for (index, threshold) in mortality_scale.items():
        if deaths <= threshold:
            mortality_index = index
            break
    
    return mortality_index

# Use function to create a new dictionary of hurricanes sorted by mortality rating.
hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
for info in hurricanes.values():
    mortality_rating = find_mortality_rating(info)
    hurricanes_by_mortality[mortality_rating].append(info)

# Helper function to combine a list of hurricane names into a single string, returning default text if the list is empty.
def stringify(hurricane_list):
        if len(hurricane_list) > 0:
            hurricane_names = [info["Name"] for info in hurricane_list]
            return ', '.join(hurricane_names)
        else:
            return "There are no category five hurricanes that match this rating."

# Print & present the data
mini_buffer = "-------------------------------------"
for (index, hurricane_list) in hurricanes_by_mortality.items():
    if index == 0:
        print("Mortality Rating 0 Hurricanes ({} Deaths)".format(mortality_scale[0]))
    elif index < 5:
        print("Mortality Rating {rating} Hurricanes ({lower_bound}-{upper_bound} Deaths)".format(
            rating=index,
            lower_bound=mortality_scale[index-1] + 1,
            upper_bound=mortality_scale[index]
        ))
    else:
        print("Mortality Rating 5 Hurricanes ({}+ Deaths)".format(mortality_scale[4] + 1))
    print(mini_buffer)
    print(stringify(hurricane_list))
    print('')

# Print Buffer
print_buffer(buffer_line, 2)


# 9. Categorize Hurricanes by Damages
# Damage Scale: Rates hurricanes based on the dollar value of the damages they caused (in USD). The values of the dictionary are the upper thresholds for that index of the scale.
# Hurricanes that caused more damage than the upper threshold for index 4 will be categorized as index 5.
# Hurricanes for which the damages weren't recorded will have a damage rating of "Unknown"
damage_scale = {
    0: 0.0,
    1: 100000000.0,
    2: 1000000000.0,
    3: 10000000000.0,
    4: 50000000000.0
}
# Function that returns a damage rating for a particular hurricane based on the dollar value of damages it caused.
def find_damage_rating(hurricane_info):
    damage_value = hurricane_info["Damages"]
    # Check whether the damage value is a float or not.
    if not isinstance(damage_value, float):
        return "Unknown"
    
    # Default rating to 5, then lower it based on whether it meets the various thresholds.
    damage_index = 5
    for (index, value) in damage_scale.items():
        if damage_value <= value:
            damage_index = index
            break
    
    return damage_index

# Use function to sort hurricanes by damage rating
hurricanes_by_damages = {0: [], 1: [], 2: [], 3: [], 4: [], 5:[], "Unknown": []}
for info in hurricanes.values():
    damage_rating = find_damage_rating(info)
    hurricanes_by_damages[damage_rating].append(info)

# Print & present the data
for (index, hurricane_list) in hurricanes_by_damages.items():
    if index == "Unknown":
        print("Hurricanes with Unknown or Unrecorded Damages")
    elif index == 0:
        print("Damage Rating 0 Hurricanes (USD {} in Damages)".format(dollarize(damage_scale[0])))
    elif index < 5:
        print("Damage Rating {rating} Hurricanes (USD {lower_bound}-{upper_bound} in Damages)".format(
            rating=index,
            lower_bound=dollarize(damage_scale[index-1] + 0.01),
            upper_bound=dollarize(damage_scale[index])
        ))
    else:
        print("Damage Rating 5 Hurricanes (USD {}+ in Damages)".format(dollarize(damage_scale[4] + 0.01)))
    print(mini_buffer)
    print(stringify(hurricane_list))
    print('')
