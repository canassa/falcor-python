from falcor import Model


def test_clone():
    model_1 = Model()
    model_2 = model_1._clone()

    assert not model_2._materialized
    model_1._materialized = True
    assert not model_2._materialized


def test_thread_erros_as_values():
    model_1 = Model()
    assert not model_1._treatErrorsAsValues

    model_2 = model_1.treatErrorsAsValues()
    assert model_2._treatErrorsAsValues
    assert not model_1._treatErrorsAsValues


def test_box_values():
    model_1 = Model()
    assert not model_1._boxed

    model_2 = model_1.boxValues()
    assert model_2._boxed
    assert not model_1._boxed
