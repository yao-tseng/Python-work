#V3 is for Python 3

def scope_test():
	def do_local():
		variable = "local variable"

#V3	def do_nonlocal():
#V3		nonlocal variable
#V3		variable = "nonlocal variable"

	def do_global():
		global variable
		variable = "global variable"

	variable = "test variable"
	
	do_local()
	print( "After local assignment: %s" % variable )
#V3	do_nonlocal()
#V3	print( "After nonlocal assignment: %s" % variable )
	do_global()
	print( "After global assignment: %s" % variable )

scope_test()
print( "In global scope: %s" % variable )


'''
output>>
After local assignment: test variable
After global assignment: test variable
In global scope: global variable

V3 output>>
After local assignment: test variable
After nonlocal assignment: nonlocal variable
After global assignment: nonlocal variable
In global scope: global variable
'''
