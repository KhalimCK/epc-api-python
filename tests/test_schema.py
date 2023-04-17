import pytest
from epc_api.schemas import ParamSchema
from pydantic.error_wrappers import ValidationError


def test_complete_params():
    # Test setting up a complete parameter set which should be valid

    valid_params = {
        "postcode": "test",
        "local-authority": "test",
        "constituency": "test",
        "property-type": "bungalow",
        "floor-area": "unknown",
        "energy-band": "b",
        "from-month": 1,
        "from-year": 2010,
        "to-month": 2,
        "to-year": 2012,
    }

    res = ParamSchema(**valid_params)

    assert isinstance(res, ParamSchema)

    # Test setting up a complete parameter set which should be invalid

    invalid_params = {
        "postcode": "test",
        "local-authority": "test",
        "constituency": "test",
        "propertytype": "BAD VALUE",
        "floor-area": "unknown",
        "energy-band": "b",
        "from-month": "1",
        "from-year": "2010",
        "to-month": "2",
        "to-year": "2012",
    }
    with pytest.raises(ValidationError):
        ParamSchema(**invalid_params)


def test_partial_params():
    # Test a partial parameter set which should valid

    valid_params = {
        "postcode": "test",
        "floor-area": "unknown",
        "energy-band": "a",
        "from-month": 3,
        "to-month": 5,
    }

    res = ParamSchema(**valid_params)

    assert isinstance(res, ParamSchema)

    invalid_params = {
        "postcode": "test",
        "floor-area": "unknown",
        "energy-band": "BAD",
        "from-month": 3,
        "to-month": 100,
    }

    with pytest.raises(ValidationError):
        ParamSchema(**invalid_params)

    invalid_extras = {
        "not_a_value": 1
    }

    with pytest.raises(ValidationError):
        ParamSchema(**invalid_extras)

    # Test a single value param dictionary where the value of the parameter has an alias
    valid_single_alias = {
        "property-type": "park home"
    }
    res = ParamSchema(**valid_single_alias)

    assert isinstance(res, ParamSchema)

    # We should be able to pass nothing
    valid_empty = {}
    res = ParamSchema(**valid_empty)
    assert isinstance(res, ParamSchema)
