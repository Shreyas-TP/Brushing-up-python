#dictionary
'''
dish={
    "tumkur":"idli",
    "bangalore":"dosa",
    "mysore":"vada"
}

print(dish["tumkur"])

print(dish.get("mangalore","not found"))
print(dish)
dish["mangalore"]="nirr dosa"
print(dish)
dish.pop("mangalore")
print(dish)


print(dish.keys())
print(dish.values())
print(dish.items())     
print(len(dish))   

new_dish={
    "hubli":"bisi bele bath",
    "mangalore":"nirr dosa",
}
dish.update(new_dish)
print(dish)'''

item1={
    "name":"laptop",
    "brand":"dell",
    "price":50000       
}
item2={
    "name":"phone",
    "brand":"samsung",
    "price":20000
}

items=[item1,item2]
print(items)

print(f"total price: {item1['price'] + item2['price']}")


friends={
    "friend1":{"name":"alice","age":25, "fav_sub":"english"},
    "friend2":{"name":"bob","age":30, "fav_sub":"maths"},
}
print(friends)

print(friends["friend1"]["fav_sub"])