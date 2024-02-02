import json
#serialization: convert dictionary to json string
data=dict(name="Dream",age=30,city="Angola")

json_data=json.dumps(data)
print(json_data)

#deserialization:convert json string to dictionary
json_data2={"name": "Dream", "age": 30, "city": "Angola"}
data2=json.loads(json_data2)
print(type(data2))

