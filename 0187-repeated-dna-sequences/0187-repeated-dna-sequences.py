class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        pows=[7**(i+1) for i in range(10)]
        d={'A':1,'C':2,'G':3,'T':4}
        def hash(val,toadd,toremove): return (val-(d[toremove]*pows[9]))*7+d[toadd]*7
        ans=set()
        curr=sum([d[x]*(7**(10-i)) for i,x in enumerate(s[:10])])
        z=set([curr])
        for i in range(10,len(s)):
            curr=hash(curr,s[i],s[i-10])
            if curr in z: ans.add(s[i-9:i+1])
            z.add(curr)
        return ans