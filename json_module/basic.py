import json

Person_string = '''
	{
		"people" : [
			{
				"name" : "John Smith",
				"phone" : "615-555-7164",
				"emails" : ["johnsmith@bogusemail.com" , "John-smith@work-place.com"] ,
				"has_license": false
	        },
	        {
	 			"name" : "Jane Doe",
				"phone" : "560-555-5153",
				"emails" : null,
				"has_license" : true
			}
		]
	}
'''

data=json.loads(Person_string)

# print(type(data))
# print(data)

# ######### To select each items ##########
# for person in data['people']:
#     print(person)

# ######### To select individual value from each items ##########
# for person in data['people']:
#     print(person['name'])

# ######### To delete individual value from each items ##########
for person in data['people']:
    del person['phone']

# new_string=json.dumps(data)
new_string=json.dumps(data, indent=2)     #it will indent the output to two spaces
# new_string=json.dumps(data, indent=2, sort_keys=True)     #it will sort the keys in ascending order

print(new_string)

















''' conversion table works as:
Json    Python
object  dict
array   list
string  str
nummber(int) int
number (real) float
true    True
false   False
null    None
'''