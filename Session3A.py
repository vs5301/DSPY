# MVC with () or no bracket is tuple
# followers = ("john", "jennie", "fionna", "dave", "kia")
# print(followers, type(followers), len(followers))

# MVC with [] as list
followers = ["john", "jennie", "fionna", "dave", "kia"]
print(followers, type(followers), len(followers))

followers[0] = "john.watson"
print(followers, type(followers), len(followers))

# List is MUTABLE
# We can add update and delete i.e. changes are supported
# The way you add data it gets stored in indexing

# Update id of a follower
del followers[3]
print(followers, type(followers), len(followers))

# Delete a follower from the list
followers.append("harry")
followers.append("george")
followers.append("Kim")

print(followers, type(followers), len(followers))

# Tuple and list are data structures

# List supports duplicates

followers.append("fionna")
followers.append("john.watson")

print(followers, type(followers), len(followers))