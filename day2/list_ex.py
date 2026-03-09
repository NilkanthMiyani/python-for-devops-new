a = [100,200,'nilkanth',True,4.5]
print(type(a))
a.append(500)
print(a)  

clouds = list()
print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
print(clouds)

print("World leader for cloud service provider is: ", clouds[0])
print(dir(clouds))
print(clouds.extend.__doc__)

# iterate a list
for cloud in clouds:
    if cloud == "aws":
        print("Amazon is the market leader")
    elif cloud == "azure" or cloud == "gcp":
        print("They are also exist in this market")
    else:
        print("Other cloud providers are also exist")
        