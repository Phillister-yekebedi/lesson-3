#Write a Python program that takes a list of strings as input and outputs 
#the number of times each string appears in the list, using a dictionary and conditional statements.
def strings_count(strings):
    count = {}
    for string in strings:
        if string in count:
            count [string]+=1

    else:
        count [string] =1
        return count

strings = ['lemon', 'pawpaw', 'mango', 'pawpaw', 'melon']
print(strings_count(strings))

#Write a Python program that takes a list of numbers as input and outputs 
#the median of the numbers 
def number_of_times(numb):
    n = len(numb)
    if n % 2 == 0:
        middle = n//2
        median = (numb[middle]+numb[middle-1])/2
    else:
        median = numb[n//2]
        return median
    
numb = [1,2,3,4,5,6,7,8]   
print(number_of_times(numb))   

#Write a Python program that takes a list of numbers as input and outputs 
#the second largest number in the list using conditional statements and a for loop.
def second_largest_number(arr):
    largest= [0]
    second_large = [0]
    r = range(len(arr))
    for ra in r:
     if arr[ra] > largest:
        largest = arr[ra]

    for ra in r:
        if arr[ra] > second_large and arr[ra]!= largest:
            second_large = arr [ra]

            
    return second_large 

arr= [30,90,45,80]
print(second_largest_number(arr))





#Write a Python program that takes a year as input and determines if it is a leap year.
def leap_year(years): 
    if years % 4 == 0 and years % 100!= 0 or years % 400 ==0:
        print("The year is a leap year")
    else:
        print("Its not a leap year")      

print(leap_year(2024))
        
#Write a Python program that takes a string as input and checks if it is a 
#palindrome (reads the same forwards and backwards), ignoring spaces and punctuation.

def check_palindrome(texts):
    text = 0
    if text == texts[::-1]:
        return "is palindrome"
    else:
        return "is not palindrome"
    
print (check_palindrome("noon")) 



