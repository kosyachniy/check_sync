from main import create_tree, compare_tree


def test_identically():
    assert compare_tree(
        create_tree('tests/data/nested_file/less', exceptions=['_']),
        create_tree('tests/data/nested_file/more', exceptions=['_'])
    ) == {}

def test_more_files():
    assert compare_tree(
        create_tree('tests/data/nested_file/more', exceptions=['_']),
        create_tree('tests/data/nested_file/less', exceptions=['_'])
    ) == {'onigiri': {'ramen': None, 'hacapuri': {}}, 'sake': None, 'sodzu': {}}

def test_similar_names():
    assert compare_tree(
        create_tree('tests/data/similar_name/file', exceptions=['_']),
        create_tree('tests/data/similar_name/folder', exceptions=['_'])
    ) == {'hinkali': None}

    assert compare_tree(
        create_tree('tests/data/similar_name/folder', exceptions=['_']),
        create_tree('tests/data/similar_name/file', exceptions=['_'])
    ) == {'hinkali': {}}

def test_tree_pruning():
    assert compare_tree(
        create_tree('tests/data/dont_display/more', exceptions=['_']),
        create_tree('tests/data/dont_display/less', exceptions=['_'])
    ) == {'hinkali': {}, 'sake': {}, 'ramen': {'onigiri': {'taiga': None}}}

    assert compare_tree(
        create_tree('tests/data/dont_display/less', exceptions=['_']),
        create_tree('tests/data/dont_display/more', exceptions=['_'])
    ) == {'ramen': {'ramen': None}}
