# part 1
# 1
agent = {"name":"alpha", "level":3 , "active":True}
print(agent)
# 2
print(agent["name"])
# 3
key_level = agent.get(0)
print(key_level)
# 4
agent["score"]= 95
print(agent)
# 5
agent["level"]=5
print(agent)
# 6
del agent["active"]
print(agent)
