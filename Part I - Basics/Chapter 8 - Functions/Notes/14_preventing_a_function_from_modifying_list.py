"""
Sometimes you'll want to prevent a function from modifying a list.
For example, say that you start with a list of unprinted designs and
write a function to move them to a list of completed models, as in 
the previous example.

You may decide that even though you've printed all the designs,
you want to keep the original list of unprinted designs for your 
records. But because you moved all the design names out of 
unprinted_designs, the list is now empty, and the empty list is the
only version you have; the original is gone.

In this case, you can address this issue by passing the function a 
copy of the list, not the original. Any changes the function makes to 
the list will affect only the copy, leaving the original intact.
"""

# function_name(list_name[:])

"""
The slice notation makes a copy of the list to send to the function.
If we didn't want to empty the list of unprinted designs in print_models.py,
we could call print_models() like this:
"""

# print_models(unprinted_designs[:], completed_models)

"""
The function can do its job because it still receives the names of all 
unprinted designs. But this time it uses a copy of unprinted_designs, and not
the original. This way, the list 'completed_models' will fill up with the names
of printed models like it did before, but will leave the original list of
unprinted designs unaffected.

It should, however, be noted that even though you can preserve the contents of
a list by the method detailed above, there should be a specific reason for you
to do this instead of passing the original list to functions, as it's more 
efficient for a function to work with an existing list than it is for it to
make a separate copy, especially when larger lists are involved.
"""
