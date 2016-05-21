

class Nested(Exception):
    'Indexers cannot be nested.',


class NeedQuotes(Exception):
    'unquoted indexers must be numeric.',


class Empty(Exception):
    'cannot have empty indexers.',


class LeadingDot(Exception):
    'Indexers cannot have leading dots.',


class LeadingComma(Exception):
    'Indexers cannot have leading comma.',


class RequiresComma(Exception):
    'Indexers require commas between indexer args.',


class RoutedTokens(Exception):
    'Only one token can be used per indexer when specifying routed tokens.'


class PrecedingNaN(Exception):
    'ranges must be preceded by numbers.',


class SuceedingNaN(Exception):
    'ranges must be suceeded by numbers.'


class Invalid(Exception):
    'Invalid routed token.  only integers|ranges|keys are supported.'


class IllegalEscape(Exception):
    'Invalid escape character.  Only quotes are escapable.'


class UnexpectedToken(Exception):
    'Unexpected token.',


class InvalidIdentifier(Exception):
    'Invalid Identifier.',


class InvalidPath(Exception):
    'Please provide a valid path.',
