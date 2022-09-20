from multipick import multipick

title = "Assign languages to groups 'a', 'b' or '1'."
options = ["foo.bar%s.baz" % x for x in range(1, 71)]
groups:set = {"a", "b", 1}
selected = multipick(options, groups, title)
print(selected)
