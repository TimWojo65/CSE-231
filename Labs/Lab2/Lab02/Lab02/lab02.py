from shelve import BsdDbShelf
odd_count=0
odd_sum=0
even_count=0
even_sum=0
positive_int_count=0

while True:
    n_str = int(input("\n:~Input an integer (0 terminates)~:"))
    if n_str == 0:
        break
    if n_str < 0:
        continue
    if n_str%2 != 0:
        odd_count +=1
        odd_sum +=n_str
    if n_str%2 == 0:
        even_count +=1
        even_sum +=n_str
    if n_str > 0:
        positive_int_count+=1








# Good stuff goes here


#Do not change the following lines of code
print("\n")
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
