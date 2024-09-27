def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]

print(oxford_comma(["kiwi"])) 
print(oxford_comma(["kiwi", "durian"]))
print(oxford_comma(["kiwi", "durian", "starfruit"]))
print(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"]))