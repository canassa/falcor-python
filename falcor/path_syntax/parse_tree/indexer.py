from falcor.path_syntax.token_types import TOKEN_TYPES

from falcor.path_syntax.parse_tree.range import _range
from falcor.path_syntax.parse_tree.quote import quote
from falcor.path_syntax.parse_tree.routed import routed
from falcor.path_syntax import exceptions

# var idxE = E.indexer


def indexer(tokenizer, opening_token, state, out):
    """
    The indexer is all the logic that happens in between
    the '[', opening bracket, and ']' closing bracket.
    """

    token = tokenizer.next()
    done = False
    allowed_max_length = 1
    routed_indexer = False

    # State variables
    state['indexer'] = []

    while not token['done']:

        if token['type'] in {TOKEN_TYPES['token'], TOKEN_TYPES['quote']}:
            # ensures that token adders are properly delimited.
            if len(state['indexer']) == allowed_max_length:
                raise exceptions.RequiresComma(tokenizer)

        # Extended syntax case
        if token['type'] == TOKEN_TYPES['openingBrace']:
            routed_indexer = True
            routed(tokenizer, token, state, out)

        elif token['type'] == TOKEN_TYPES['token']:
            t = int(token['token'])
            # if (isNaN(t)) {
            #     raise exceptions.needQuotes(tokenizer)
            # }
            state['indexer'].append(t)

        # dotSeparators at the top level have no meaning
        elif token['type'] == TOKEN_TYPES['dotSeparator']:
            if not len(state['indexer']):
                raise exceptions.LeadingDot(tokenizer)
            _range(tokenizer, token, state, out)

        # Spaces do nothing.
        elif token['type'] == TOKEN_TYPES['space']:
            pass

        elif token['type'] == TOKEN_TYPES['closingBracket']:
            done = True

        # The quotes require their own tree due to what can be in it.
        elif token['type'] == TOKEN_TYPES['quote']:
            quote(tokenizer, token, state, out)

        # Its time to decend the parse tree.
        elif token['type'] == TOKEN_TYPES['openingBracket']:
            raise exceptions.Nested(tokenizer)

        elif token['type'] == TOKEN_TYPES['commaSeparator']:
            allowed_max_length += 1

        else:
            raise exceptions.UnexpectedToken(tokenizer)

        # If done, leave loop
        if done:
            break

        # Keep cycling through the tokenizer.
        token = tokenizer.next()

    if len(state['indexer']) == 0:
        raise exceptions.Empty(tokenizer)

    if len(state['indexer']) > 1 and routed_indexer:
        raise exceptions.RoutedTokens(tokenizer)

    # Remember, if an array of 1, keySets will be generated.
    if len(state['indexer']) == 1:
        state['indexer'] = state['indexer'][0]

    out.append(state['indexer'])

    # Clean state.
    state['indexer'] = None
