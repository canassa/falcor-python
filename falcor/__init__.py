from falcor.tokenizer import Tokenizer
from falcor.parse_tree.head import head


def parser(path, extended_rules=None):
    return head(Tokenizer(path, extended_rules))


def from_path(path, ext=None):
    if not path:
        return []

    if isinstance(path, str):
        return parser(path, ext)

    return path


def from_paths_or_path_values(paths, ext=None):
    # Constructs the paths from paths / pathValues that have strings.
    # If it does not have a string, just moves the value into the return
    # results.
    if not paths:
        return []

    out = []
    for path in paths:

        # Is the path a string
        if isinstance(path, str):
            out.append(parser(path, ext))

        # is the path a path value with a string value.
        elif isinstance(path, dict) and isinstance(path['path'], str):
            out.append({
                'path': parser(path['path'], ext),
                'value': path['value'],
            })

        # just copy it over.
        else:
            out.append(path)

    return out
