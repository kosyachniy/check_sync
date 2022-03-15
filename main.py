from pathlib import Path


FOLDER_FROM = '/Users/kosyachniy/Desktop/TikTok'
FOLDER_TO = '/Users/kosyachniy/Desktop/КурсТТ'


def create_tree(folder):
    return {
        file.name: create_tree(file) if file.is_dir() else None
        for file in Path(folder).iterdir()
    }

def compare_tree(tree_from, tree_to):
    for file in set(tree_from):
        if file not in tree_to:
            continue

        if tree_from[file] and tree_to[file]:
            tree_from[file] = compare_tree(tree_from[file], tree_to[file])

        if not tree_from[file]:
            del tree_from[file]

    return tree_from

def print_tree(tree, level=0, indent=4):
    for name in tree:
        print((
            f"{' ' * indent * level}"
            f"{name}"
            f"{'' if tree[name] is None else '/'}"
        ))

        if tree[name] is not None:
            print_tree(tree[name], level+1, indent)


print_tree(compare_tree(create_tree(FOLDER_FROM), create_tree(FOLDER_TO)))
