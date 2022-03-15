from main import create_tree, compare_tree


def test_identically():
    assert compare_tree(
        create_tree('tests/data/nested_file/less'),
        create_tree('tests/data/nested_file/more')
    ) == {}

def test_more_files():
    assert compare_tree(
        create_tree('tests/data/nested_file/more'),
        create_tree('tests/data/nested_file/less')
    ) == {'onigiri': {'ramen': None, 'hacapuri': {}}, 'sake': None, 'sodzu': {}}

def test_similar_names():
    assert compare_tree(
        create_tree('tests/data/similar_name/file'),
        create_tree('tests/data/similar_name/folder')
    ) == {'hinkali': None}

    assert compare_tree(
        create_tree('tests/data/similar_name/folder'),
        create_tree('tests/data/similar_name/file')
    ) == {'hinkali': {}}

def test_tree_pruning():
    assert compare_tree(
        create_tree('tests/data/dont_display/more'),
        create_tree('tests/data/dont_display/less')
    ) == {'hinkali': {}, 'sake': {}, 'ramen': {'onigiri': {'taiga': None}}}
