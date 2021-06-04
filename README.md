# Hurricane Analysis Script
A script to examine, organize, and present various pieces of data provided on category five hurricanes. Created as part of Codecademy's Data Science Career Path.

## Description
The `script.py` file contains various lists of information, all of which pertain to category five hurricanes that have happened within the past century. There's a list for each of the following pieces of data:

* Name
* Month
* Year
* Maximum Wind Speed (in MPH)
* Areas Affected
* Damages Caused (in USD)
* Deaths Caused

The purpose of the script is to condense the lists into a dictionary where the keys are the names of each hurricane and the values are dictionaries themselves of all the relevant information for the corresponding hurricane. 

After constructing this dictionary, several functions are used to manipulate the data of the dictionary in a variety of ways. These are then presented usin the built-in `print()` function. The different methods of presenting the data are as follows:

* Each hurricane's name printed alongside all of its relevant information.
* All hurricanes sorted by which year they took place.
* How many times each area was affected by a hurricane.
* The area or areas affected by the most hurricanes.
* The hurricane or hurricanes which caused the greatest number of deaths.
* The hurricane or hurricanes which incurred the greatest dollar value in damages.
* All hurricanes sorted by their mortality index (a scale of 0-5 based on how many deaths they caused).
* All hurricanes sorted by their damage index (a scale of 0-5 based on the dollar value of how much damages they incurred).

## Technologies
* Python 3.9.5 64-bit

## Usage
* Open a terminal window such as Git Bash.
* Navigate (using `cd`) to the directory where the `script.py` script is stored.
* Run the script with the command: `python script.py`

## Example

```
$ python script.py
Hurricane Cuba I
-----------------------
Date: October, 1924
Maximum Sustained Wind Speed: 165 MPH
Areas Affected: Central America, Mexico, Cuba, Florida, The Bahamas
Damages (USD): Damages not recorded
Total Deaths: 90

Hurricane San Felipe II Okeechobee
-----------------------
Date: September, 1928
Maximum Sustained Wind Speed: 160 MPH
Areas Affected: Lesser Antilles, The Bahamas, United States East Coast, Atlantic Canada
Damages (USD): $100,000,000.00
Total Deaths: 4000

. . .

**********************************
**********************************

Damage Rating 0 Hurricanes (USD $0.00 in Damages)
-------------------------------------
There are no category five hurricanes that match this rating.

Damage Rating 1 Hurricanes (USD $0.01-$100,000,000.00 in Damages)
-------------------------------------
San Felipe II Okeechobee, Cuba II, CubaBrownsville, Tampico, Carol, Janet, Hattie, Edith

Damage Rating 2 Hurricanes (USD $100,000,000.01-$1,000,000,000.00 in Damages)
-------------------------------------
New England, Carla, Beulah, Felix

Damage Rating 3 Hurricanes (USD $1,000,000,000.01-$10,000,000,000.00 in Damages)
-------------------------------------
Camille, David, Allen, Gilbert, Hugo, Mitch, Isabel, Emily, Dean

Damage Rating 4 Hurricanes (USD $10,000,000,000.01-$50,000,000,000.00 in Damages)
-------------------------------------
Andrew, Ivan, Rita, Wilma, Matthew, Michael

Damage Rating 5 Hurricanes (USD $50,000,000,000.01+ in Damages)
-------------------------------------
Katrina, Irma, Maria

Hurricanes with Unknown or Unrecorded Damages
-------------------------------------
Cuba I, Bahamas, Labor Day, Anita

```