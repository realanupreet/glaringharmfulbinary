n = input()
nmap = {}
for c in n:
    if c not in nmap:
        nmap[c] = 0
print("CHAT WITH HER!" if len(nmap) % 2 == 0 else "IGNORE HIM!")
