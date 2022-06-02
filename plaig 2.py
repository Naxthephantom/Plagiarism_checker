
from difflib import SequenceMatcher

with open(" ") as file1, open(" ") as file2:
    file1data = file1.read()
    file2data = file2.read()

    similarity = sequencematcher(none, file1data, file2data).ratio()
    print (similarity*100)
    