class ToyClass:
    def instancemethod(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    @staticmethod
    def staticmethod():
        return 'static method called'

obj = ToyClass()
# print(obj.instancemethod())

# print(ToyClass.instancemethod(obj))

# print(obj.classmethod())

print(obj.staticmethod())