'''This program projects population growth for the next five years.'''

# Declaring variables.
currentPopulation = 312032486

# Computing seconds in a year.
secondsInMinute = 60
secondsInHour = secondsInMinute*60
secondsInDay = secondsInHour*24
secondsInYear = secondsInDay * 365

births = secondsInYear // 7
deaths = secondsInYear // 13
immigrants = secondsInYear // 45
currentPopulation1 = currentPopulation + births - deaths - immigrants

births2 = secondsInYear // 7
deaths2 = secondsInYear // 13
immigrants2 = secondsInYear // 45
currentPopulation2 = currentPopulation1 + births - deaths - immigrants

births3 = secondsInYear // 7
deaths3 = secondsInYear // 13
immigrants3 = secondsInYear // 45
currentPopulation3 = currentPopulation2 + births - deaths - immigrants

births4 = secondsInYear // 7
deaths4 = secondsInYear // 13
immigrants4 = secondsInYear // 45
currentPopulation4 = currentPopulation3 + births - deaths - immigrants

births5 = secondsInYear // 7
deaths5 = secondsInYear // 13
immigrants5 = secondsInYear // 45
currentPopulation5 = currentPopulation4 + births - deaths - immigrants

print("Year 0:", currentPopulation)
print("Year 1:", currentPopulation1)
print("Year 2:", currentPopulation2)
print("Year 3:", currentPopulation3)
print("Year 4:", currentPopulation4)
print("Year 5:", currentPopulation5)

