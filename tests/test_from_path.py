from falcor import from_path


def test_should_convert_a_string_to_path():
    _input = 'videos[1234].summary'
    output = ['videos', 1234, 'summary']
    assert from_path(_input) == output


def test_should_return_a_provided_array():
    _input = ['videos', 1234, 'summary']
    output = ['videos', 1234, 'summary']
    assert from_path(_input) == output


def test_should_convert_an_undefined():
    _input = None
    output = []
    assert from_path(_input) == output
