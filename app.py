import json

i = 1
my_json={}

while i <= 10:
    my_json[f'field_{i}'] = f'value_{i}'
    i+=1

print(f'{json.dumps(my_json)}')
