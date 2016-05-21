"""
Based on:

https://github.com/Netflix/falcor-path-syntax/blob/master/src/tokenizer/index.js
"""
from falcor.path_syntax.token_types import TOKEN_TYPES


DOT_SEPARATOR = '.'
COMMA_SEPARATOR = ','
OPENING_BRACKET = '['
CLOSING_BRACKET = ']'
OPENING_BRACE = '{'
CLOSING_BRACE = '}'
COLON = ':'
ESCAPE = '\\'
DOUBLE_OUOTES = '"'
SINGE_OUOTES = "'"
TAB = "\t"
SPACE = " "
LINE_FEED = '\n'
CARRIAGE_RETURN = '\r'
SPECIAL_CHARACTERS = '\\\'"[]., \t\n\r'
EXT_SPECIAL_CHARACTERS = '\\{}\'"[]., :\t\n\r'


class Tokenizer:
    def __init__(self, string, ext):
        self._string = string
        self._idx = -1
        self._extended = ext
        self.parse_string = ''
        self._next_token = None

    def next(self):
        """
        grabs the next token either from the peek operation or generates the
        next token.
        """
        next_token = self._next_token or get_next(self._string, self._idx, self._extended)

        self._idx = next_token['idx']
        self._next_token = False
        self.parse_string += str(next_token['token'].get('token'))

        return next_token['token']

    def peek(self):
        """
        will peak but not increment the tokenizer
        """
        next_token = self._next_token or get_next(self._string, self._idx, self._extended)
        self._next_token = next_token

        return next_token['token']

    @classmethod
    def to_number(cls, x):
        return int(x)


def to_output(token, _type, done):
    return {
        'token': token,
        'done': done,
        'type': _type
    }


def get_next(string, idx, ext):
    output = False
    token = ''
    special_chars = EXT_SPECIAL_CHARACTERS if ext else SPECIAL_CHARACTERS
    done = None

    while not done:
        done = idx + 1 >= len(string)
        if done:
            break

        # we have to peek at the next token
        character = string[idx + 1]

        if character not in special_chars:
            token += character
            idx += 1
            continue
        # The token to delimiting character transition.
        elif len(token):
            break

        idx += 1
        _type = None
        MAP = {
            DOT_SEPARATOR: TOKEN_TYPES['dotSeparator'],
            COMMA_SEPARATOR: TOKEN_TYPES['commaSeparator'],
            OPENING_BRACKET: TOKEN_TYPES['openingBracket'],
            CLOSING_BRACKET: TOKEN_TYPES['closingBracket'],
            OPENING_BRACE: TOKEN_TYPES['openingBrace'],
            CLOSING_BRACE: TOKEN_TYPES['closingBrace'],
            TAB: TOKEN_TYPES['space'],
            SPACE: TOKEN_TYPES['space'],
            LINE_FEED: TOKEN_TYPES['space'],
            CARRIAGE_RETURN: TOKEN_TYPES['space'],
            DOUBLE_OUOTES: TOKEN_TYPES['quote'],
            SINGE_OUOTES: TOKEN_TYPES['quote'],
            ESCAPE: TOKEN_TYPES['escape'],
            COLON: TOKEN_TYPES['colon'],
        }

        _type = MAP.get(character, TOKEN_TYPES['unknown'])
        output = to_output(character, _type, False)
        break

    if not output and len(token):
        output = to_output(token, TOKEN_TYPES['token'], False)

    if not output:
        output = {'done': True}

    return {
        'token': output,
        'idx': idx
    }
