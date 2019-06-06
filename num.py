s,v=map(str,input().split())
aa1=0
if len(s)>len(v):
  s,v=v,s
i=0
while i<len(s):
  aa1+=(ord(v[i])-ord(s[i]))
  i+=1
for i in range(i,len(v)):
  aa1+=ord(v[i])-ord('a')+1
print(aa1)
