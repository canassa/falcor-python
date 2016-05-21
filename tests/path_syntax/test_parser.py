"""
Based on:

https://github.com/Netflix/falcor-path-syntax/blob/master/test/parse-tree/parser.spec.js
"""

from falcor.path_syntax import parser


def test_parse_a_simple_key_string():
    out = parser('one.two.three')
    assert out == ['one', 'two', 'three']


def test_parse_a_string_with_indexers():
    out = parser('one[0]')
    assert out == ['one', 0]


def test_parse_a_string_with_indexers_followed_by_dot_separators():
    out = parser('one[0].oneMore')
    assert out == ['one', 0, 'oneMore']


def test_parse_a_string_with_a_range():
    out = parser('one[0..5].oneMore')
    assert out == ['one', {'from': 0, 'to': 5}, 'oneMore']


def test_parse_a_string_with_a_set_of_tokens():
    out = parser('one["test", \'test2\'].oneMore')
    assert out == ['one', ['test', 'test2'], 'oneMore']


def test_treat_07_as_7():
    out = parser('one[07, 0001].oneMore')
    assert out == ['one', [7, 1], 'oneMore']


def test_parse_out_a_range():
    out = parser('one[0..1].oneMore')
    assert out == ['one', {'from': 0, 'to': 1}, 'oneMore']


def test_parse_out_multiple_ranges():
    out = parser('one[0..1,3..4].oneMore')
    assert out == ['one', [{'from': 0, 'to': 1}, {'from': 3, 'to': 4}], 'oneMore']


def test_parse_paths_with_newlines_and_whitespace_between_indexer_keys():
    out = parser("""one[
        0, 1, 2, 3, 4,
        5, 6, 7, 8, 9].oneMore""")
    assert out == ['one', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'oneMore']
