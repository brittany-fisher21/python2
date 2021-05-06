meal = {
    "entree": "salmon",
    "drink": "wine",
    "dessert": "cheesecake"
}

#print(meal["dessert"]):
#print("tonight I will have %s for dinner, with %s for dessert." % (meal["entree"], meal["dessert"])
#print("tonight I will have " + meal["entree" +" for dinner, with dessert"]))


#if "dessert" in meal:
 #   print("Of COURSE Sean had dessert!!!")
#else:
 #   print("Sean did NOT have dessert, and now he is sad.")



print(meal)

meal["entree"] = "salmon"

meal["drink"] ="wine"
del meal["dessert"]
print(meal)
