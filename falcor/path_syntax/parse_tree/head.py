from falcor.path_syntax.token_types import TOKEN_TYPES
from falcor.path_syntax.parse_tree.indexer import indexer
from falcor.path_syntax import exceptions


def head(tokenizer):
    # The top level of the parse tree.  This returns the generated path
    # from the tokenizer.

    token = tokenizer.next()
    state = {}
    out = []

    while not token['done']:

        if token['type'] == TOKEN_TYPES['token']:
            try:
                int(token['token'][0])
            except ValueError:
                pass
            else:
                raise exceptions.InvalidIdentifier(tokenizer)
            # first = +token.token[0]
            # if (!isNaN(first)) {
            #     E.throwError(E.invalidIdentifier, tokenizer);
            # }
            out.append(token['token'])

        # dotSeparators at the top level have no meaning
        elif token['type'] == TOKEN_TYPES['dotSeparator']:

            if len(out) == 0:
                raise exceptions.UnexpectedToken(tokenizer)

        # Spaces do nothing.
        elif token['type'] == TOKEN_TYPES['space']:
            # NOTE: Spaces at the top level are allowed.
            # titlesById  .summary is a valid path.
            pass
        # Its time to decend the parse tree.
        elif token['type'] == TOKEN_TYPES['openingBracket']:

            indexer(tokenizer, token, state, out)

        else:
            raise exceptions.UnexpectedToken(tokenizer)

        # Keep cycling through the tokenizer.
        token = tokenizer.next()

    if len(out) == 0:
        raise exceptions.InvalidPath(tokenizer)

    return out
