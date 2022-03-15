"""
Find files from one directory that are not in another
"""


from pathlib import Path


FOLDER_FROM = '/Users/kosyachniy/Desktop/TikTok'
FOLDER_TO = '/Users/kosyachniy/Desktop/КурсТТ'


def create_tree(folder):
    """ Create file tree by path """
    return {
        file.name: create_tree(file) if file.is_dir() else None
        for file in Path(folder).iterdir()
    }

def compare_tree(tree_from, tree_to):
    """ Check for files of one file tree in another """

    for file in set(tree_from):
        if file not in tree_to:
            continue

        if tree_from[file] and tree_to[file]:
            tree_from[file] = compare_tree(tree_from[file], tree_to[file])

        if not tree_from[file]:
            del tree_from[file]

    return tree_from

def print_tree(tree, level=0, indent=4):
    """ Pretty visualize file tree """

    for name in tree:
        print((
            f"{' ' * indent * level}"
            f"{name}"
            f"{'' if tree[name] is None else '/'}"
        ))

        if tree[name] is not None:
            print_tree(tree[name], level+1, indent)


if __name__ == '__main__':
    print_tree(compare_tree(create_tree(FOLDER_FROM), create_tree(FOLDER_TO)))
