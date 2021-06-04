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


# write your count affected areas function here:







# write your find most affected area function here:







# write your greatest number of deaths function here:







# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:
