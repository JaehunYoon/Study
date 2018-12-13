path = input()
location = input()

f = open('./temp.txt', 'a')

f.write(f"\n{path}\n")
f.write(f"{location}")

f.close()
