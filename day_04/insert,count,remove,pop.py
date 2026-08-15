cart = ["boots", "shirt", "jacket", "jeans", "shirt"]
cart.append("socks")
cart.insert(2, "cap")
print(cart)

print(cart.count("shirt"))
print(cart.index("jacket"))

cart.remove("jeans")
cart.pop(0)
print(cart)

