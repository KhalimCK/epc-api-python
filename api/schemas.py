import pydantic


class ParamSchema(pydantic.BaseModel):
    address: str
    postcode: str
    local_authority: str = pydantic.Field(alias="local-authority")

# params:
    # - address
    # - postcode
    # - local-authority
    # - constituency
    # - property-type Multiple property types can be supplied so this should be a list if supplied
    # In this initial implementation, we won't do much parameter validation and allow the api failure to handle that
    # We will validate proprty-type
    # bungalow	Filter for properties of type 'Bungalow'
    # flat	Filter for properties of type 'Flat'
    # house	Filter for properties of type 'House'
    # maisonette	Filter for properties of type 'Maisonette'
    # park home	Filter for properties of type 'Park Home'
    # - floor-area Again multiple can be supplied
    # unknown	A floor area recorded as 0
    # s	A floor area between 1m² and 55m²
    # m	A floor area between 55m² and 70m²
    # l	A floor area between 70m² and 85m²
    # xl	A floor area between 85m² and 110m²
    # xxl	A floor area greater than 110m²
    # xxxl
    # - energy-band
    # a	A rated (92+)
    # b	B rated (81-91)
    # c	C rated (69-80)
    # d	D rated (55-68)
    # e	E rated (39-54)
    # f	F rated (21-38)
    # g	G rated (1-20)
    # - from-month	A numeric month identifier 1-12, to establish the start of a date range, where 1 is January and 12 is December. If no from-month parameter is supplied 1 (January) is assumed.
    # - from-year	A numeric year identifier to estalish the start of a date range between 2008 and 2023 e.g. 2015. If no year parameter is supplied 2008 is assumed.
    # - to-month	A numeric month identifier 1-12, to establish the end of a date range, where 1 is January and 12 is December. If no to-month parameter is supplied then 12 is assumed.
    # - to-year	A numeric year identifier between 2008 and 2023 e.g. 2015. If no to-year parameter is supplied then 2023 is assumed.
params_schema = Schema(
    {
        Optional("address"): str,

    }
)
