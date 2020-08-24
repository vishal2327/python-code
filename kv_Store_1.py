
import shelve

class KVstore:
    d = {}

    def _init_(self):
        self.d = shelve.open("/Users/vishpreet/Documents/python/python-code/kv_store1.txt",'w')

    def get(self,key):
        return self.d[key]

    def set(self,key,value):
        self.d[key]= value

    def close(self):
        self.d.sync()


obj = KVstore()

obj.set(1,"green")
obj.set(2,"red")
obj.set(3,"yellow")

print(obj.get(1))
print(obj.get(2))
print(obj.get(3))

#obj.close()
