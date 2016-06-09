# We start out with a very simple class, containg
# two methods with very little actual content.
class MyClass:

    # This field will not be exposed to the global
    # namespace because it is not callable.
    field = 0    

    # Note that Python requires the "self"-reference
    # ("this" in Java) to be the first parameter of 
    # any method. When calling a method, you do not
    # pass it as an argument, though. This happens
    # automatically behind the scenes.
    def bar(self):
        self.foo()
        
    def egg(self):
        print "The chicken comes first ;)"
    
    def foo(self):
        print "Hi there"
    
# Any object in Python has an attribute "__dict__"
# containing all names defined in the object. Even
# though everything in Python is an object, a more
# apt way would be to say that everything is a 
# dictionary.
cls_dict = MyClass.__dict__

# Let's have an instance of our class to actually
# call the methods on. Calling a constructor is 
# pretty simple: just use the classname. No "new" 
# keyword required (or allowed).
myObject = MyClass()

# When calling a method you do not explicitly pass
# the "self"-parameter. Python internally rewrites
# this code to (simplified, of course):
#    MyClass.egg(myObject)
myObject.egg()

# Now, we go through all keys in the dictionary of
# our class, getting the names.
for key in cls_dict:
    # Testing for types can be a bit tricky in
    # Python and does not go well with Duck-typing.
    # Here we just assume that whatever is callable
    # is a method (other callables are classes).
    if callable(cls_dict[key]):
        # Given the name of our method, we want to define
        # a function like so:
        #   def foo():
        #       return myObject.foo()
        # To that end we use Python's "exec"-statement,
        # which lets us define a function for each
        # method.
        exec "def %(key)s(): return myObject.%(key)s()" % {'key': key}
     
# After all the magic, let's call our new function.   
bar()
