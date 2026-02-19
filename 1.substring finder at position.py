class Subfinder:
    def __init__(self,text,sub):
        self.text=text
        self.sub=sub
    def check(self):
        for i in range (len(self.text)-len(self.sub)+1):
            if self.text[i:i+len(self.sub)]==self.sub:
                return i
        return -1
t="varun gowda c"
s="gow"
obj1=Subfinder(t,s)
pos=obj1.check()
print("found at "if pos!=-1 else "not found",pos)
