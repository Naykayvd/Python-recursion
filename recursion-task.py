# Program to display fibonacci values of 20

nterms = 20

# first 2 values
n1, n2 = 0, 1
count = 0

# just making sure the number is a valid one
if nterms <= 0:
   print("number is less than one")
elif nterms == 1:
   print(n1)
else:
   while count < nterms:
       print(n1, end=" ")
       nth = n1 + n2
       # updating the values
       n1 = n2
       n2 = nth
       count += 1