import requests
r=requests.get("https://petstore.swagger.io/v2/swagger.json").json()

print(r.keys())
for path in r.get("paths"):
    print("\n Path--------> "+path)
    if 'post' in r['paths'][path]:
        print("I have post")
        if 'schema'in r['paths'][path]['post']['parameters'][0]:
          print((r['paths'][path]['post']['parameters'][0]['schema']))
          print("Request Body ------------")
          if '$ref' in  r['paths'][path]['post']['parameters'][0]['schema']:
              definition=(r['paths'][path]['post']['parameters'][0]['schema']['$ref']).split("/")
              print(r[definition[-2]][definition[-1]]['properties'])
          else:
              definition=(r['paths'][path]['post']['parameters'][0]['schema']['items']['$ref']).split("/")
              print(r[definition[-2]][definition[-1]]['properties'])
    # if 'put' in r['paths'][path]:
    #     print("I have put")
    #     print((r['paths'][path]['put']['parameters']))


print("--------------Definitions--------------")
print(r["definitions"]["Pet"])


