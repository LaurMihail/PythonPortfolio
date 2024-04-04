
multiline = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius\nThere is no atmosphere!"
print(multiline.replace("Celsius", "C"))
print(multiline.find("Mars"))
print(multiline.count("daytime"))
for items in multiline.split():
    if items.isnumeric():
        print(items)

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split('. ')
print(sentences)
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")


astero = "Ganymede"
planet = "Mars"
gravity = "1.43"
template = """Gravity Facts about {astero}
----------------------------------------
Planet Name: {planet}
Gravity on {astero}: {gravity} m/s2"""
print(template.format(astero=astero, planet=planet, gravity=gravity))


first_planet = int(input('Enter the distance from the sun for the first planet in km: '))
second_planet = int(input('Enter the distance from the sun for the second planet in km: '))
distance_km = second_planet - first_planet
print(f"Distance between the two planets is {distance_km} km")
