from main import create_tree, compare_tree


def test_identically():
    assert compare_tree(
        create_tree('tests/data/1/from'),
        create_tree('tests/data/1/to')
    ) == {}

def test_more_files():
    assert compare_tree(
        create_tree('tests/data/2/from'),
        create_tree('tests/data/2/to')
    ) == {'onigiri': {'ramen': None}}
