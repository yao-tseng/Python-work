
# print
print( "\n>>PRINT" )

print( "Hey pretty!" )
	# "(text)" or '(text)' doesn't metter

# variables and types
print( "\n>>VARIABLES & TYPES" )

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
print( "\n>>LISTS" )

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
print( "\n>>BASIC OPERATORS" )

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
print( "\n>>STRING FORMATTING" )

name_1 = "Yao"
age_1 = 24
data_1 = ( "Yao", 21 )
print( "%s is %d years old." % (name_1, age_1) )
print( "%s likes the number %s." % data_1 )

list_3 = [21, 31, 41]
print( "List: %s" % list_3 )
	#any object which is not a string can be formatted using the %s operator

# basic string operations
print( "\n>>BASIC STRING OPERATIONS" )

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

# conditions
print( "\n>>CONDITIONS" )

int_2 = 3
print( int_2 == 3 )
print( int_2 == 2 )
print( int_2 < 5 )

name_2 = "Elaina"
name_3 = ["Elaina", "Bella"]
age_2 = 24
if name_2 == "Elaina" and age_2 == 24:
	print( "This person is now in the US." )
if name_2 == "Elaina" or name_2 == "Bella":
	print( "This person's last name is Tseng." )
if name_2 in name_3:
	print( "This person's name is either Elaina or Bella." )

time_1 = 1200
if time_1 > 1200:
	print( "It's now after noon." )
elif time_1 < 1200:
	print( "It's in the morning." )
else:
	print( "It's noon now." )

name_4 = "Elaina"
name_5 = "Elaina"
name_6 = ["Elaina"]
name_7 = ["Elaina"]
print( name_4 == name_5 )
print( name_4 is name_5 )
print( name_6 is name_7 )

print( not False )		#true
print( not False == (True) )	#true
number_2 = 1
number_3 = 99
number_4 = 0
print( not number_2 )		#false
print( not number_3 )		#false
print( not number_4 )		#true

# loops
print( "\n>>LOOPS" )

for x_1 in range(5):
	print( x_1 )		#0,1,2,,3,4
for x_2 in range(3, 6):
	print( x_2 )		#3,4,5
for x_3 in range(0, 20, 4):
	print( x_3 )		#0,4,8,12,16

count_1 = 0
while count_1 < 3:
	print( count_1 )	#0,1,2
	count_1 += 1

count_2 = 0
while True:
	print( count_2 )	#0,1,2
	count_2 += 1
	if count_2 >= 3:
		break
	#break is used to exit a loop (for/while)

for x_4 in range(20):
	if x_4 % 6 != False:
		continue
	print( x_4 )		#0,6,12,18
	#continue is used to skip the current block

# functions
print( "\n>>FUNCTIONS" )

def function_1():
	print( "Hope I can still do functions here lol" )
function_1()

def function_2( name, favorite_athlete ):
	print( "%s's favorite athlete is %s" % ( name, favorite_athlete ) )
function_2( "Yao", "Allen Iverson" )

def multiply_2_numbers( x, y ):
	return x * y
x_5 = multiply_2_numbers( 3, 5 )
print( x_5 )








