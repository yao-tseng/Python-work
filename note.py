
# print
print( ">>PRINT" )

print( "Hey pretty!" )
	# "(text)" or '(text)' doesn't metter

# variables and types
print( ">>VARIABLES & TYPES" )

int_1 = 7
float_1 = 7.0
float_2 = float(7)
print( int_1 )
print( float_1 )
print( float_2 )

string_1 = "hey"
print( string_1 )

one = 1
two = 2
three = one + two
print( three )

h = "hello"
w = "world"
hw = h + w
print( hw )

a, b = 3, 4
print( b, a )

# lists
print( ">>LISTS" )

list_1 = [11, 22, 33]
print( list_1 )
print( list_1[2] )

list_2 = []
list_2.append(44)
list_2.append(55)
list_2.append(66)
list_2.append( "numbers" )
print(list_2)

# basic operators
print( ">>BASIC OPERATORS" )

number_1 = 2 + 3 * 4 / 5.0
print( number_1 )

remainder = 9 % 2
print( remainder )

square = 7 ** 2
cube = 3 ** 3
print( square, cube )

hipython = "Hi" + " " + "Python"
print( hipython )

even_num = [2, 4, 6]
odd_num = [1, 3, 5]
print( odd_num + even_num )
print( odd_num * 3 )

# string formatting
print( ">>STRING FORMATTING" )

name_1 = "Yao"
age_1 = 24
data_1 = ( "Yao", 21 )
print( "%s is %d years old." % (name_1, age_1) )
print( "%s likes the number %s." % data_1 )

list_3 = [21, 31, 41]
print( "List: %s" % list_3 )
	#any object which is not a string can be formatted using the %s operator

# basic string operations
print( ">>BASIC STRING OPERATIONS" )

string_2 = "This is a string!"
print( len(string_2) )
print( string_2.index("s") )	#this method only recognizes the first
print( string_2.count("s") )
print( string_2[3:13] )
print( string_2[3:13:3] )
print( string_2[::-1] )		#reverse string
print( string_2.upper() )
print( string_2.lower() )
print( string_2.startswith("Thi") )	#true
print( string_2.endswith("Ing!") )	#false
print( string_2.split("s") )




















