"""
Find files from one directory that are not in another
"""

from pathlib import Path
from copy import deepcopy


FOLDER_FROM = '/Users/kosyachniy/Desktop/TikTok'
FOLDER_TO = '/Users/kosyachniy/Desktop/КурсТТ'


def create_tree(folder, exceptions=None):
    """ Create file tree by path """
    return {
        file.name: create_tree(file, exceptions) if file.is_dir() else None
        for file in Path(folder).iterdir()
        if not exceptions or file.name not in exceptions
    }

def compare_tree(tree_from, tree_to, short=True):
    """ Check for files of one file tree in another """

    tree_from = deepcopy(tree_from)
    tree_to = deepcopy(tree_to)

    for file in set(tree_from):
        # Completely not in inherited
        if file not in tree_to:
            # Don't display nested files
            if short and tree_from[file]:
                tree_from[file] = {}

            continue

        # If it is a file
        if tree_from[file] is None:
            # If both are files, so remove it from tracking
            if tree_to[file] is None:
                del tree_from[file]

            continue

        # If it is folder with no nested elements
        # NOTE: Case from={}, to=None (different file types) → keep
        if tree_from[file] == {}:
            # If the folder names match
            if tree_to[file] == {}:
                del tree_from[file]

            continue

        # Both are there, it is necessary to check nested files
        tree_new = compare_tree(tree_from[file], tree_to[file], short)

        # All nested elements matched
        if not tree_new:
            del tree_from[file]
            continue

        # Don't display nested files
        if short and {
            k: v and {}
            for k, v in tree_from[file].items()
        } == tree_new:
            tree_from[file] = {}
            continue

        # Save unique nested files
        tree_from[file] = tree_new

    return tree_from

def print_tree(tree, level=0, indent=4):
    """ Pretty visualize file tree """

    for name in sorted(tree.keys()):
        print((
            f"{' ' * indent * level}"
            f"{name}"
            f"{'' if tree[name] is None else '/'}"
        ))

        if tree[name] is not None:
            print_tree(tree[name], level+1, indent)


if __name__ == '__main__':
    print_tree(compare_tree(create_tree(FOLDER_FROM), create_tree(FOLDER_TO)))
