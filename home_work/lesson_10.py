name = "Віталій"

print(name)
print(name.encode('utf-8'),  len(name.encode('utf-8')),  "байтів")    # кодування у utf-8 по замовчунням
print(name.encode('utf-16'), len(name.encode('utf-16')), "байтів")
print(name.encode('utf-32'), len(name.encode('utf-32')), "байтів")
