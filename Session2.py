#1. Storage Container Creation Statement
johnsAge = 20

# johnsAge is a Reference Variable
# It hold HashCode for the Data 20

# 2. Container Read Statement
print("Johns Age is:", johnsAge)
print("Johns Age HashCode is: ", id(johnsAge))

jenniesAge = 20
print("Jennies Age is:", jenniesAge)
print("Jennies Age HashCode is: ", id(jenniesAge))

print("=====================")

# 3. Container Updation Statement
johnsAge = 22

print("Johns age now: ", johnsAge)
print("Johns age hashcode now: ", id(johnsAge))

print("Jennies age now:", jenniesAge)
print("Jennies age hashcode now: ", id(jenniesAge))

# 4. Container Copy Statement | Reference Copy
siasAge = jenniesAge
print("=====================")

print("Sias age is: ", siasAge)
print("Sias age hascode is ", id(siasAge))

# 5. Container Delete Statement
del jenniesAge

print("SiasAge is ", siasAge)

# If we delete the variable it will delete everything. But, if some other
# variable also refers to the same data location, it will not delete the data.

# Reference Variable: Which holds the HashCode
print("Sias age hascode in Binary is: ", bin(id(siasAge)))
print("Sias age hascode in Octal is: ", oct(id(siasAge)))
print("Sias age hascode in Decimal is: ", id(siasAge))
print("Sias age hascode in Hexa Decimal is: ", hex(id(siasAge)))
