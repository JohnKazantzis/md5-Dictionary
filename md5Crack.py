import hashlib
import sys

#Usage -> -h --help
if sys.argv[1] == '-h' or sys.argv[1] == "--help":
    print("Usage: python3 md5Crack.py [wordlist] [hashes file]")
    exit(0)

#Opening the wordlist and the file
#where the hashes are saved
fp = open(sys.argv[1],"r",encoding='latin-1')
hp = open(sys.argv[2],"r")

#Saving the hashes from the hashes.txt
#in the hashes list
hashes = []
for line in hp:
    line = line.rstrip()
    hashes.append(line)

#Iterating over the wordlist
for line in fp:
    line = line.rstrip()
    m = hashlib.md5(line.encode())
    if m.hexdigest() in hashes:
        print(str(m.hexdigest()) + ": " + line)

fp.close()
hp.close()
