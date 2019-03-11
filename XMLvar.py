from collections import Counter

import xml.etree.ElementTree as ElT

tree = ElT.parse('newsafr.xml')

root = tree.getroot()

descriptions = []

xml_descriptions = root.findall('channel/item')

for item in xml_descriptions:

    description = item.find("description")

    descriptions.extend(description.text.split())

for word in descriptions:
    if len(word) <= 6:
        descriptions.remove(word)

counted_words = Counter(tuple(descriptions))
print("Чаще всего встречаются слова:")

for word, number in counted_words:
    for i in range(0,10):
        print(word)