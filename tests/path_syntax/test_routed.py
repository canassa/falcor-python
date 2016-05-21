from falcor.path_syntax import parser


def test_should_create_a_routed_token_for_the_path():
    out = parser('one[{ranges}].oneMore', True)
    assert out == [
        'one', {'type': 'ranges', 'named': False, 'name': ''}, 'oneMore']


def test_should_create_a_named_routed_token_for_the_path():
    out = parser('one[{ranges:foo}].oneMore', True)
    assert out == [
        'one', {'type': 'ranges', 'named': True, 'name': 'foo'}, 'oneMore']


def test_should_create_a_named_routed_token_for_the_path_and_allow_white_space_before_the_definition():
    out = parser('one[{ranges: \t\n\rfoo}].oneMore', True)
    assert out == [
        'one', {'type': 'ranges', 'named': True, 'name': 'foo'}, 'oneMore']


def test_should_create_a_named_routed_token_for_the_path_and_allow_white_space_after_the_definition():
    out = parser('one[{ranges:foo \t\n\r}].oneMore', True)
    assert out == [
        'one', {'type': 'ranges', 'named': True, 'name': 'foo'}, 'oneMore']


def test_should_create_a_named_routed_token_for_the_path_and_allow_white_space_before_and_after_the_definition():
    out = parser('one[{ranges: \t\n\rfoo \t\n\r}].oneMore', True)
    assert out == [
        'one', {'type': 'ranges', 'named': True, 'name': 'foo'}, 'oneMore']
