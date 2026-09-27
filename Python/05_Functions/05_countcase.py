def count_case(s):
    lower = 0
    upper = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    dict1 = {"upper": upper, "lower": lower}
    return dict1

print(count_case("Hello WoRld PeACe"))
