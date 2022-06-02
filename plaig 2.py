
from difflib import SequenceMatcher

with open(" File1 ") as file1, open(" File2 ") as file2:
    file1data = file1.read()
    file2data = file2.read()

    similarity = sequencematcher(none, file1data, file2data).ratio()
    print (similarity*100)
    
