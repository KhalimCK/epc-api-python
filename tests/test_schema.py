import pytest
from api.schemas import ParamSchema
from pydantic.error_wrappers import ValidationError


def test_complete_params():
    # Test setting up a complete parameter set which should be valid

    valid_params = {
        "postcode": "test",
        "local_authority": "test",
        "constituency": "test",
        "property_type": "bungalow",
        "floor_area": "unknown",
        "energy_band": "b",
        "from_month": "1",
        "from_year": "2010",
        "to_month": "2",
        "to_year": "2012",
    }

    res = ParamSchema(**valid_params)

    assert isinstance(res, ParamSchema)

    # Test setting up a complete parameter set which should be invalid

    invalid_params = {
        "postcode": "test",
        "local_authority": "test",
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
