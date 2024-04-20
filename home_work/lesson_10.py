name = "Віталій"

print(name)
print(name.encode('utf-8'),  len(name.encode('utf-8')),  "байтів")    # кодування у utf-8 по замовчунням
print(name.encode('utf-16'), len(name.encode('utf-16')), "байтів")
print(name.encode('utf-32'), len(name.encode('utf-32')), "байтів")
print("----------------------------------------------------------------------")

a = b'\xd0\x92\xd1\x96\xd1\x82\xd0\xb0\xd0\xbb\xd1\x96\xd0\xb9'
print(a.decode())                                                      # декодування (utf-8)
