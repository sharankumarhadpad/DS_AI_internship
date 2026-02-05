#personal contact book
contacts = {"srm":1221,"xyz":4432,"nrr":4563}
print(contacts)
for name,number in contacts.items():
 print(name,number)
print(contacts.get("srm"))

 # duplicate cleaner
raw_logs=["ID01","ID02","ID03","ID04","ID05","ID07"]
unique_users=["ID01","ID02","ID03","ID04","ID05","ID07"]
print(type(unique_users))
print(unique_users)
print("ID01" in unique_users)
print("ID07" in unique_users)
print("ID03" in unique_users)

# the interest matcher
friend_x = {"roman","maverick","jonathan","acrotic"}
friend_y = {"noivern","unfezant","rumble","survine"}
print(friend_x | friend_y)
print(friend_x & friend_y)
print(friend_x - friend_y)


