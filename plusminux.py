standard_input = """2
5 5
2 2 1 3 2
2 4 9
2 3 4
1 5 5
1 4 9
2 4 3
10 5
1 1 1 1 1 1 1 1 1 1
3 8 13
2 5 10
3 8 10
1 10 2
1 9 100"""
# print("Hellow")
# ques 1
# n=int(input())
# ans=[]
# for i in range(n):
#     a,b,c=[int(x) for x in input().split()]
#     if (a+b) == c:
#         # print(a,b,a+b,c)
#         ans.append("+")
#     else:
#         ans.append("-")
# for a in ans:
#     print(a)

# ques 2
# n=int(input())
# ans=[]
# for i in range(n):
#     c=[]
#     b=int(input())
#     c=[int(x) for x in input().split()]
#     fe=sum(list(filter(lambda x: x%2==0, c)))
#     fo=sum(list(filter(lambda x: x%2, c)))
#     if fe>fo:
#         ans.append("YES")
#     else:
#         ans.append("NO")

# for a in ans:
#     print(a)

# ques 3
# ans = []
# n = int(input())
# for i in range(n):
#     sl = int(input())
#     ost = input()
#     st=ost
#     f = True
#     for i in range(len(st)):
#         # print(st[i], i % 2)
#         # if i>1:
#         if i>1 and st[i] == st[i-1]:
#             # i+=1
#             # ans.append("NO")
#             # print("in the false")
#             f = False
#             break
#         else:
#             st = st.replace(st[i], str(i % 2))
#         # print(st, f)
#     if sl==2 and ost[0]==ost[1]:
#         ans.append("NO")
#     elif f == True:
#         ans.append("YES")
#     else:
#         ans.append("NO")
# for a in ans:
#     print(a)
    # print("//////////////////////////////////////////////")


# ques 4
n=int(input())
ans=[]
for i in range(n):
    ans.append([0])
for i in range(n):
    p,q=[int(x) for x in input().split()]
    oa=[int(x) for x in input().split()]
    for j in range(q):
        l,r,k=[int(x) for x in input().split()]
        if sum(oa[:l-1]+[k]*(r-l+1)+oa[r:])%2==0:
            ans[i].append("NO")
        else:
            ans[i].append("YES")

for a in ans:
    for i in a[1:]:
        print(i)