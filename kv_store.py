#import shelve

class KVstore:
      d={}
#      def _init_(self):
#          d=shelve.open("/Users/vishpreet/Documents/python/python-code/kvfile.txt")

      def get(self,key):
          return self.d[key]

      def set(self,key,value):
          self.d[key]= value

      #def set(self,key):
        #  self.d[key]= "vishal"

     # def destroy(self):
     #      print("closing")
     #  shelve.close()

obj = KVstore()
obj.set(1, "Apple")
obj.set(2, "Orange")
obj.set(3, "kela")
#obj.set(4)
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
#print(obj.get(4))
#obj.destroy()
