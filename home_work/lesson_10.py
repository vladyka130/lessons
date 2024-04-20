# Даний рядок у байтовому вигляді: b'r\xc3\xa9sum\xc3\xa9' закодована в кодуванні за умовчанням utf-8.
# Декодувати її у рядковий вигляд у кодуванні за замовчуванням.
# Потім результат знову перетворити на байтовий, тільки вже в кодуванні 'Latin1'
# І на кінець результат знову декодувати у рядок
# (Результати всіх перетворень виводити на екран).

s = b'r\xc3\xa9sum\xc3\xa9'
s_decode_utf8 = s.decode()
print(s_decode_utf8)
s_encode_Latin_1 = s_decode_utf8.encode('Latin1')
print(s_encode_Latin_1)
print(s_encode_Latin_1.decode('Latin1'))