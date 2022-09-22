from groupick import groupick

title = "Assign languages to groups 'a', 'b' or '1'."
options = ["foo.bar%s.baz" % x for x in range(1, 71)]
groups:set = {"a", "b", 1}
selected = groupick(options, groups, title)
print(selected)
