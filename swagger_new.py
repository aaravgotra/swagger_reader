from swagger_parser import SwaggerParser
parser = SwaggerParser(swagger_path='C:\\Users\\aaravgotra\\Desktop\\download.json')  # Init with file
ps=parser.definitions_example.keys()
# parser.get_path_spec()
# r1= parser.get_send_request_correct_body("/v2/pet","post")
# print(r1)
#print(parser.paths)
# r= parser.get_send_request_correct_body("/pet/{petId}", "get")
# print(r)
print(parser.paths)
for i in parser.paths:
    print(i)
    if "put" in (parser.paths[i]).keys():
        print("--------------PUT CALL--------------")
        print(parser.get_send_request_correct_body(i, "put"))
    if "post" in (parser.paths[i]).keys():
        print("--------------POST CALL-------------")
        print(parser.get_send_request_correct_body(i, "post"))
# print(ps)
# for p in ps:
#     print(parser.definitions_example.get(p))

#print(parser.get_paths_data())
