from groupick import groupick

title = "Assign languages to groups 'a', 'b' or '1'."
options = ["Java", "JavaScript", "Python", "PHP", "C++", "Erlang", "Haskell"]
groups:set = {"a", "b", 1}
selected = groupick(options, groups, title, indicator="=>", default_index=2)
print(f"Here is your assignment: {selected}")
