from falcor.path_syntax.routed_tokens import ROUTED_TOKENS
from falcor.path_syntax.token_types import TOKEN_TYPES
from falcor.path_syntax import exceptions


def routed(tokenizer, openingToken, state, out):
    """
    The routing logic.

    parse-tree:
    <opening-brace><routed-token>(:<token>)<closing-brace>
    """

    routeToken = tokenizer.next()
    named = False
    name = ''

    # ensure the routed token is a valid ident.
    if routeToken['token'] not in {
            ROUTED_TOKENS['integers'],
            ROUTED_TOKENS['ranges'],
            ROUTED_TOKENS['keys']}:
        raise exceptions.Invalid(tokenizer)

    # Now its time for colon or ending brace.
    _next = tokenizer.next()

    # we are parsing a named identifier.
    if _next['type'] == TOKEN_TYPES['colon']:
        named = True

        # Get the token name or a white space character.
        _next = tokenizer.next()

        # Skip over preceeding white space
        while _next['type'] == TOKEN_TYPES['space']:
            _next = tokenizer.next()

        if _next['type'] != TOKEN_TYPES['token']:
            raise exceptions.Invalid(tokenizer)
        name = _next['token']

        # Move to the closing brace or white space character
        _next = tokenizer.next()

        # Skip over any white space to get to the closing brace
        while _next['type'] == TOKEN_TYPES['space']:
            _next = tokenizer.next()

    # must close with a brace.
    if _next['type'] == TOKEN_TYPES['closingBrace']:
        outputToken = {
            'type': routeToken['token'],
            'named': named,
            'name': name,
        }
        state['indexer'].append(outputToken)
    # closing brace expected
    else:
        raise exceptions.Invalid(tokenizer)
