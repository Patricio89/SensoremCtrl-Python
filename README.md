# SensoremCtrl-Python
Simple script for writing sensor data to a .csv file.

## Motivation
Using the SenseHat library set for Python to retrieve temperature, relative humidity and timestamp values and store this into a
.csv file into choosen directory.
This script will generate the file If file doesn't already exist.

Current interval for data reading is set to 5 minutes. 

## Build status
1.0 Functional

## Tech/framework used
<b>None.</b>

## Installation
Deploy as a normal script from anywhere.

## API Reference
[SenseHat](https://pythonhosted.org/sense-hat/api/)

## Tests
<b>None.</b>

## How to use?
Boot up and script will start reading in values to csv file and loop iteration every 5 minute until script is cancelled.

To change interval, modify the sleep function.

## Contribute
Add in extra functionality / retrieve other source of data of your choice using the SenseHat library.

## Credits
* Junior Software Developer / Student - [Patricio Morales](https://github.com/Patricio89/)
* Junior Software Developer / Student - [Adrian Wieslander](https://github.com/AdrWie/)

## License
OpenSource

* Intern - Software Developer (Student) CC By [Patricio Morales](https://github.com/Patricio89)
* Intern - Software Developer (Student) CC By [Adrian Wieslander](https://github.com/AdrWie)
* B3IT Innovation AB CC By [Johnne Adermark]()
* B3IT Innovation AB CC By [Kenneth Andersson]()
