#Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.
#The seed of the function is already sown in the skeleton code in the editor.

def is_year_leap(year):
#
# put your code here
#
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
