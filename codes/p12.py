#Dictionary
data = {
    "name":"yash gupta",
    "jobRole":"data scientist"
}
print(data["jobRole"])
print(data.get("jobRole"))
print(data.values())
print(data.keys())
print(data.items())
data.update({"name":"mahadev","age":True})
# data.clear()
# data.pop("jobRole")
# data.popitem()
#del data['name']#if no key is provided then it completely deletes the dict and we got undefined error
print(data)


for key in data.keys():
    print(f"KEY IS {key} AND THE VALUE IS {data[key]}")