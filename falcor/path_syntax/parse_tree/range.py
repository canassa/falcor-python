from falcor.path_syntax.tokenizer import Tokenizer
from falcor.path_syntax.token_types import TOKEN_TYPES
from falcor.path_syntax import exceptions


def _range(tokenizer, opening_token, state, out):
    """
    The indexer is all the logic that happens in between
    the '[', opening bracket, and ']' closing bracket.

    FIXME: ``opening_token`` and ``out`` not used.
    """

    token = tokenizer.peek()
    dot_count = 1
    done = False
    inclusive = True

    # Grab the last token off the stack.  Must be an integer.
    idx = len(state['indexer']) - 1
    _from = Tokenizer.to_number(state['indexer'][idx])
    to = None

    # if (isNaN(_from)) {
    #     E.throwError(E.range.precedingNaN, tokenizer)
    # }

    # Why is number checking so difficult in javascript.

    while not done and not token['done']:

        # dotSeparators at the top level have no meaning
        if token['type'] == TOKEN_TYPES['dotSeparator']:
            if dot_count == 3:
                raise exceptions.UnexpectedToken(tokenizer)
            dot_count += 1

            if dot_count == 3:
                inclusive = False

        elif token['type'] == TOKEN_TYPES['token']:
            # move the tokenizer forward and save to.
            to = Tokenizer.to_number(tokenizer.next()['token'])

            # throw potential error.
            # if (isNaN(to)) {
            #     E.throwError(E.range.suceedingNaN, tokenizer)
            # }

            done = True

        else:
            done = True

        # Keep cycling through the tokenizer.  But ranges have to peek
        # before they go to the next token since there is no 'terminating'
        # character.
        if not done:
            tokenizer.next()

            # go to the next token without consuming.
            token = tokenizer.peek()

        # break and remove state information.
        else:
            break

    state['indexer'][idx] = {
        'from': _from,
        'to': to if inclusive else to - 1,
    }
