from falcor.token_types import TOKEN_TYPES

from falcor.parse_tree.range import _range
from falcor.parse_tree.quote import quote
from falcor.parse_tree.routed import routed
from falcor import exceptions

# var idxE = E.indexer


def indexer(tokenizer, opening_token, state, out):
    """
    The indexer is all the logic that happens in between
    the '[', opening bracket, and ']' closing bracket.
    """

    token = tokenizer.next()
    done = False
    allowedMaxLength = 1
    routedIndexer = False

    # State variables
    state['indexer'] = []

    while not token['done']:

        if token['type'] in {TOKEN_TYPES['token'], TOKEN_TYPES['quote']}:
            # ensures that token adders are properly delimited.
            if len(state['indexer']) == allowedMaxLength:
                raise exceptions.requiresComma(tokenizer)

        # Extended syntax case
        if token['type'] == TOKEN_TYPES['openingBrace']:
            routedIndexer = True
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
                raise exceptions.leadingDot(tokenizer)
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
            raise exceptions.nested(tokenizer)

        elif token['type'] == TOKEN_TYPES['commaSeparator']:
            allowedMaxLength += 1

        else:
            raise exceptions.unexpectedToken(tokenizer)

        # If done, leave loop
        if done:
            break

        # Keep cycling through the tokenizer.
        token = tokenizer.next()

    if len(state['indexer']) == 0:
        raise exceptions.empty(tokenizer)

    if len(state['indexer']) > 1 and routedIndexer:
        raise exceptions.routedTokens(tokenizer)

    # Remember, if an array of 1, keySets will be generated.
    if len(state['indexer']) == 1:
        state['indexer'] = state['indexer'][0]

    out.append(state['indexer'])

    # Clean state.
    state['indexer'] = None
