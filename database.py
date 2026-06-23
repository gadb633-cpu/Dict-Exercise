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
# 7
agent_keys = agent.keys()
print(agent_keys)
print(agent.keys())
agent_values = agent.values()
print(agent_values)
print(agent.values())
agent_values_and_keys = agent.items()
print(agent_values_and_keys)
print(agent.items())
# 8
print("score" in agent)
# 9
scores = {"alpha":80 , "bravo":95 , "charlie":70}
print(max(scores.values()))
# 10
copy_agent = agent.copy()
print(copy_agent)
copy_agent["level"] = 10
print(copy_agent)
print(agent)
# part 2
# 1
config = {}
config_timeout = config.setdefault("timeout",30)
print(config_timeout)
print(config)
