from falcor.token_types import TOKEN_TYPES
from falcor import exceptions


def quote(tokenizer, openingToken, state, out):
    """
    quote is all the parse tree in between quotes.  This includes the only
    escaping logic.

    parse-tree:
    <opening-quote>(.|(<escape><opening-quote>))*<opening-quote>
    """

    token = tokenizer.next()
    innerToken = ''
    openingQuote = openingToken['token']
    escaping = False
    done = False

    while not token['done']:
        if token['type'] in {
                TOKEN_TYPES['token'],
                TOKEN_TYPES['space'],
                TOKEN_TYPES['dotSeparator'],
                TOKEN_TYPES['commaSeparator'],
                TOKEN_TYPES['openingBracket'],
                TOKEN_TYPES['closingBracket'],
                TOKEN_TYPES['openingBrace'],
                TOKEN_TYPES['closingBrace']}:
            if escaping:
                raise exceptions.IllegalEscape(tokenizer)

            innerToken += token['token']

        elif token['type'] == TOKEN_TYPES['quote']:
            # the simple case.  We are escaping
            if escaping:
                innerToken += token['token']
                escaping = False

            # its not a quote that is the opening quote
            elif token['token'] != openingQuote:
                innerToken += token['token']

            # last thing left.  Its a quote that is the opening quote
            # therefore we must produce the inner token of the indexer.
            else:
                done = True

        elif token['type'] == TOKEN_TYPES['escape']:
            escaping = True

        else:
            raise exceptions.UnexpectedToken(tokenizer)

        # If done, leave loop
        if done:
            break

        # Keep cycling through the tokenizer.
        token = tokenizer.next()

    if len(innerToken) == 0:
        raise exceptions.Empty(tokenizer)

    state['indexer'].append(innerToken)
