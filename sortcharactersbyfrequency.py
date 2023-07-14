# Input:
s = "treett"
# Output: "eert"

# import heapq as h
smap = {}
for c in s:
    if c in smap:
        smap[c] = smap[c]+1
    else:
        smap[c] = 1

new = sorted(smap, key=lambda x: smap[x], reverse=True)
ans = "".join([a*smap[a] for a in new])
