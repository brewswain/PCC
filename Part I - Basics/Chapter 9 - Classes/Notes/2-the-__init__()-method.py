"""
======================================================================
|    # This section references the class made in the previous file.  |
======================================================================

A function that's part of a class is a method. Everything you
learned about functions applies to methods as well; the only
practical difference for now is the way we call methods.

The __init__() method is a special method Python runs 
automatically whenever we create a new instance based on the
'Dog' class. This method has two leading underscores and two
trailing underscores, a convention that helps prevent Python's 
default method names from conflicting with your method names.

We define the __init__() method to have three parameters:
self, name, and ge. The self parameter is required in the 
method definition, and it must come first before the other
parameters. It must be included in the definition because
when Python calls this __init__() method later(To create
an instance of Dog), the method call will automatically
pass the self argument.

Every method call associated with a class automatically 
passes self, which is a reference to the instance itself;
it gives the individual instance access to the attributes
and methods in the class. When we make an instance of Dog,
Python will call the __init__() method from the Dog class.
We'll pass Dog() a name and age as arguments; self is 
passed automatically, so we don't need to pass it. 

Whenever we want to make an instance from the Dog class,
we'll provide values for only the last two parameters, 
name and age.

The two variables defined at line 26 + line 27:

========================
|   #self.name = name  |
|   #self.age = age    |
========================

Each have the prefix self. Any variable prefixed with self
is available to every method in the class, and we'll also
be able to access these variables through any instance created
from the class.

"self.name = name" Takes the value stored in the parameter name
and stores it in the variable name, which is then attached to the 
instance being created. The same process happens with self.age = age.
Variables that are accessible through instances like this are called 
attributes.

The Dog class has two other methods defined: sit() and roll_over().
Because these methods don't need additional information like a name or
age, we just define them to have one parameter, self. The instances we 
create later will have access to these methods. In other words, they'll
be able to sit and roll over. For now, sit() and roll_over() don't do 
much. They simply print a message saying the god is sitting or rolling
over. But the concept can be extended to realistic situations:

If this class were part of an actual computer game, these methods would
contain code to make an animated dog sit and roll over. If this class was
written to control a robot, these methods would direct movements that cause
a dog robot to sit and roll over.
"""
