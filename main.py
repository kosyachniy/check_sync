"""
Find files from one directory that are not in another

Example run:
env/bin/python main.py \
    --source tests/data/nested_file/more \
    --target tests/data/nested_file/less
"""

from pathlib import Path
from copy import deepcopy
import argparse


EXCEPTIONS = {
    '.DS_Store',
}


def _args():
    """ Request command line args """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--source',
        type=str,
        required=True,
        help='Full path to source',
    )
    parser.add_argument(
        '--target',
        type=str,
        required=True,
        help='Full path to target',
    )

    return parser.parse_args()


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
            if isinstance(tree_to[file], dict):
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

def main(args: argparse.Namespace):
    """ Pretty print missing files """
    tree_source = create_tree(args.source, exceptions=EXCEPTIONS)
    tree_target = create_tree(args.target, exceptions=EXCEPTIONS)
    print_tree(compare_tree(tree_source, tree_target))


if __name__ == '__main__':
    main(_args())
