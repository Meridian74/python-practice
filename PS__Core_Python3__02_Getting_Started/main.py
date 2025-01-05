import math
from urllib.request import urlopen


# ez egy szimpla próbálgatás, nincs main metódus, a program futása innen indul el.
result = math.factorial(100)
print(result)
result_digit_length = len(str(result))
print(result_digit_length)
converted_number = int("10000", 3)
print(converted_number)

print(12 ** 2)  # 12^2 --> 144
print(12 ** 3)  # 12^2 --> 144
print(int(144 ** (1 / 2)))  # --> 12

# string-ek
path = r'C:\Users\Public'
print(path)
x = str(496)
print(x)
print(type(x))
s = 'parrot'
print(s[3])
print("'" + s[3] + "'")
city = 'oslo'
print(city.capitalize())

# byte-ok
data = b'Data'
print(data[0])
print(data[1])

# List
colors = {'crimson': 0xdc143c,
          'coral': 0xff7f50,
          'teal': 0x008080}

for color in colors:
    print(color, ":", hex(colors[color]))

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)
story.close()

for word in story_words:
    print(word)
