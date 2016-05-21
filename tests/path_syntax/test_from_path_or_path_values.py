from falcor.path_syntax import from_paths_or_path_values


def test_convert_a_string_to_path():
    _input = ['videos[1234].summary']
    output = [['videos', 1234, 'summary']]
    assert from_paths_or_path_values(_input) == output


def test_convert_an_undefined_to_path():
    _input = None
    output = []
    assert from_paths_or_path_values(_input) == output


def test_return_a_provided_array():
    _input = [['videos', 1234, 'summary']]
    output = [['videos', 1234, 'summary']]
    assert from_paths_or_path_values(_input) == output


def test_convert_with_a_bunch_of_values():
    _input = [
        ['videos', 1234, 'summary'],
        'videos[555].summary',
        {'path': 'videos[444].summary', 'value': 5}
    ]
    output = [
        ['videos', 1234, 'summary'],
        ['videos', 555, 'summary'],
        {'path': ['videos', 444, 'summary'], 'value': 5}
    ]
    assert from_paths_or_path_values(_input) == output
