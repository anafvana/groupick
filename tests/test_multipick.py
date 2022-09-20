from multipick import Picker

options = ["Java", "JavaScript", "Python", "PHP", "C++", "Erlang", "Haskell"]
groups:set = {"a", "b", 1}
    
def test_move_up_down():
    title = "Please assign to groups: "
    picker = Picker(options, groups, title)
    picker.move_up()
    picker.mark_index(ord("a"))
    assert picker.get_selected() == ({'1': [], 'a': [("Haskell", len(options)-1)], 'b': []})
    picker.move_down()
    picker.move_down()
    picker.mark_index(ord("1"))
    assert picker.get_selected() == ({'1': [("JavaScript", 1)], 'a': [("Haskell", len(options)-1)], 'b': []})


def test_default_index():
    title = "Please assign to groups: "
    picker = Picker(options, groups, title, default_index=1)
    picker.mark_index(ord("a"))
    assert picker.get_selected() == ({'1': [], 'a': [("JavaScript", 1)], 'b': []})

def test_change_group():
    title = "Please assign to groups: "
    picker = Picker(options, groups, title)
    picker.move_down()
    picker.mark_index(ord("a"))
    assert picker.get_selected() == ({'1': [], 'a': [("JavaScript", 1)], 'b': []})
    picker.move_down()
    picker.move_up()
    picker.mark_index(ord("b"))
    assert picker.get_selected() == ({'1': [], 'a': [], 'b': [("JavaScript", 1)]})
    picker.mark_index(ord("c"))
    assert picker.get_selected() == ({'1': [], 'a': [], 'b': [("JavaScript", 1)]})
    picker.mark_index(ord("b"))
    assert picker.get_selected() == ({'1': [], 'a': [], 'b': []})
