class Hash_Table:
    def __init__(self):
        self.max=100
        self.table=[[] for i in range(self.max)]
    
    def hash_value(self,key):
        h=0
        for i in key:
            h=h+ord(i)
        return h%self.max
    
    def store(self,key,value):
        h=self.hash_value(key)
        for  ind,ele in enumerate(self.table[h]):
            if len(ele)==2 and ele[0]==key:
                self.table[h][ind]=(key,value)
                break
        else:
            self.table[h].append((key,value))
    
    def lookup(self,key):
        h=self.hash_value(key)
        for element in self.table[h]:
            if element[0]==key:
                return element[1]
        else:
            return -1
    
    def delete(self,key):
        h=self.hash_value(key)
        for ind,element in enumerate(self.table[h]):
            if element[0]==key:
                del self.table[h][ind]



hash=Hash_Table()
hash.store("march 1",100)
hash.store("march 2",200)
hash.store("march 3",300)
hash.store("march 4",400)
hash.store("march 5",500)
hash.store("march 6",600)
hash.store("march 17",1700)
hash.store("december 6",2000)
print(hash.table)



hash.delete("march 6")
print(hash.table)