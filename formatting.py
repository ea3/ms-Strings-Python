for i in range(1, 13):
    print("No. {0:5} squared is {1:5} and cubed is {2:5} ". format(i, i**2, i**3))   # :5 is the width of the formatting. Rigth align

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4} ". format(i, i**2, i**3))  #left align " <" . Centered "^".">" Right align

print()


print("PI is approximately {0:12}".format(22 / 7))
print("PI is approximately {0:12f}".format(22 / 7))
print("PI is approximately {0:12.50f}".format(22 / 7))
print("PI is approximately {0:52.50f}".format(22 / 7))
print("PI is approximately {0:62.50f}".format(22 / 7))
print("PI is approximately {0:72.50f}".format(22 / 7))

