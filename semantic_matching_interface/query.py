from typing import List

from pydantic import BaseModel


class QueryParameter(BaseModel):
    """
    A parameter for a semantic matching query

    Example: If I want to query an object's id_short with value "testProperty",
        attribute_name is "idShort" (following the official JSON-Schema and
        attribute_value would be "testProperty"

    :cvar attribute_name: The name of the attribute to query
    :cvar attribute_value: The value of the attribute to query
    """
    attribute_name: str
    attribute_value: str


class BaseQuery(BaseModel):
    """
    A base query for a semantic matching service.

    :cvar return_matches: How many matches the semantic matching service
        should return
    :cvar query_parameters: List of `QueryParameter`s
    """
    return_matches: int = 5
    query_parameters: List[QueryParameter]


class AssetAdministrationShellQuery(BaseQuery):
    """
    The necessary query parameters for finding the best matching
    `AssetAdministrationShells` within the server's repository of AASs.

    :cvar return_matches: How many matches the semantic matching service
        should return
    :cvar query_parameters: List of `QueryParameter`s
    """
    pass


class SubmodelElementQuery(BaseQuery):
    """
    The necessary query parameters for finding the best matching
    `SubmodelElement`s in a given `AssetAdministrationShell`

    :cvar return_matches: How many matches the semantic matching service
        should return
    :cvar query_parameters: List of `QueryParameter`s.
    :cvar aas_identifier_id: The `id`-field of a JSON-serialized AAS
        `Identifier`-object.
    :cvar aas_identifier_id_type: The `idType`-field of a JSON-serialized
        AAS `Identifier`-object.
    """
    aas_identifier_id: str
    aas_identifier_id_type: str


class MatchObjectsQuery(BaseModel):
    """
    The necessary query parameters for matching two `SubmodelElement` objects
    and returning their matching score
    """
    # (s-heppner 2023-04-11):
    # This is not yet defined.
    # Todo: Define parameters needed for this kind of query
    pass
