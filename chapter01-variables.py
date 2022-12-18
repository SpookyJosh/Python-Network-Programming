#Variables
my_hostname = "Router01"
my_domain = 'example.com'
my_motd = """
This is a string that will
contain linebreaks and could be the motd of a
router.
"""
print(my_hostname)
print(my_domain)
print(my_motd)
#Integers and floats
my_port = 22
my_throughput = 1.75
print(my_port)
print(my_throughput)
#Boolean
knows_python=True
knows_python=False
print(knows_python)
#Lists
l=[]
l.append(my_hostname)
l.append(my_domain)
l.append(my_port)
l.append(my_throughput)
#list indexes
print("The hostname stored in the list is: ")
print(l[0])
print("The domain stored in the list is: ")
print(l[1])
print("The port stored in the list is: ")
print(l[2])
#Data Types
print(type(l))
print(type(l[0]))
