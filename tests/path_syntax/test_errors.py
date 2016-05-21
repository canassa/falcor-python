import pytest

from falcor.path_syntax import parser
from falcor.path_syntax import exceptions


def test_should_create_a_named_routed_token_for_the_path_and_fail_if_white_space_divides_the_token_name():
    with pytest.raises(exceptions.Invalid):
        parser('one[{ranges:f o o}].oneMore', True)
