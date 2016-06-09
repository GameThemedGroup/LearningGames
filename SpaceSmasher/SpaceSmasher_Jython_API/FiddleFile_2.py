# We start out with another simple class, containg two 
# methods, this time with actual parameters.
class MyClass:

    # "bar" has three parameters with "msg" being 
    # optional due to its default value.
    def bar(self, x, y, msg = None):
        if msg is not None:
            print msg
        self.foo(x + y)
        
    def foo(self, x):
        print x ** 2
        
    def foobar(self):
        print "success"

# Same as before: create an instance and access the class'
# dictionary.
myObject = MyClass()
cls_dict = MyClass.__dict__

# Also the same basic principle.
for key in cls_dict:
    if callable(cls_dict[key]):
        # Python's syntax *args is similar to Java's 
        # ...-notation and allows you to collect all
        # remaining arguments, which are then passed
        # to the function as a tuple "args".
        # Python, however, has a second mechanism for
        # named arguments with two stars. This will
        # contain only arguments with a key and is in
        # fact a dictionary-object.
        #
        # Here, we just unpack und pass both on to the
        # underlying method.
        #
        #   def foo(*args, **nagrs):
        #       return myObject.foo(*args, **nargs)
        #
        exec ("def %(key)s(*args, **nargs): " +
              "return myObject.%(key)s(*args, **nargs)") % {'key': key}
     
# After all the magic, let's call our new function.   
bar(6, 8, msg="This rocks!")
foobar()
