from pathlib import Path


FOLDER_FROM = '/Users/kosyachniy/Desktop/TikTok'
FOLDER_TO = ''


def create_tree(folder):
    return {
        file.name: create_tree(file) if file.is_dir() else None
        for file in Path(folder).iterdir()
    }

def print_tree(tree, level=0, indent=4):
    for name in tree:
        print((
            f"{' ' * indent * level}"
            f"{name}"
            f"{'' if tree[name] is None else '/'}"
        ))

        if tree[name] is not None:
            print_tree(tree[name], level+1, indent)


print_tree(create_tree(FOLDER_FROM))
