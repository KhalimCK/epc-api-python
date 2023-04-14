from enum import Enum
from typing import Optional

import pydantic


class PropertyType(str, Enum):
    bungalow = "bungalow"
    flat = "flat"
    house = "house"
    maisonette = "maisonette"
    park_home = "park home"


class FloorArea(Enum):
    unknown = "unknown"
    s = "s"
    m = "m"
    l = "l"
    xl = "xl"
    xxl = "xxl"
    xxxl = "xxxl"


class EnergyBand(Enum):
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"


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

    class Config:
        extra = pydantic.Extra.forbid
