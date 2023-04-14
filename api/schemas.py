import pydantic
from enum import Enum
from typing import Literal, Optional


class PropertyType(Enum):
    bungalow: str
    flat: str
    house: str
    maisonette: str
    park_home: str = pydantic.Field(alias="park home")


class FloorArea(Enum):
    unknown: str
    s: str
    m: str
    l: str
    xl: str
    xxl: str
    xxxl: str


class EnergyBand(Enum):
    a: str
    b: str
    c: str
    d: str
    e: str
    f: str
    g: str


class ParamSchema(pydantic.BaseModel):
    address: Optional[str]
    postcode: Optional[str]
    local_authority: Optional[str] = pydantic.Field(alias="local-authority")
    constituency: Optional[str]
    property_type: Optional[PropertyType] = pydantic.Field(alias="property-type")
    floor_area: Optional[FloorArea] = pydantic.Field(alias="floor-area")
    energy_band: Optional[EnergyBand] = pydantic.Field(alias="energy-band")
    from_month: Optional[int] = pydantic.Field(None, ge=1, le=12, alias="from-month")
    from_year: Optional[int] = pydantic.Field(None, ge=2008, alias="from-year")
    to_month: Optional[int] = pydantic.Field(None, ge=1, le=12, alias="to-month")
    to_year: Optional[int] = pydantic.Field(None, ge=2008, alias="to-year")
