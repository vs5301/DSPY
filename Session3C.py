johnsFollowers = {"kia", "sim", "leo", "mike", "dave"}
fionnasFollowers = {"john", "kia", "lee", "Ana", "mike", "dave"}

# Mututal friends/followers
mututalFollowers = johnsFollowers.intersection(fionnasFollowers)

print("JOHN")
print(johnsFollowers, len(johnsFollowers))

print("FIONNA")
print(fionnasFollowers, len(fionnasFollowers))

print("MUTUAL")
print(mututalFollowers, len(mututalFollowers))