# tmp_str = {"name":"keerti",}
# print(tmp_str[0])

from plantuml import PlantUML
from os.path import abspath

with open("template.txt", "r") as f:
    data = f.readlines()

with open("graph.txt", "w") as r:
    for line in data:
        r.write(line)


# # create a server object to call for your computations
server = PlantUML(
    url="http://www.plantuml.com/plantuml/img/",
    basic_auth={},
    form_auth={},
    http_opts={},
    request_opts={},
)

# # Send and compile your diagram files to/with the PlantUML server
server.processes_file(abspath("./graph.txt"))
print("Graph generated successfully")
