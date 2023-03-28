import dataclasses
from typing import List
import json

from pydantic import BaseModel

from basyx.aas import model
from basyx.aas.adapter.json import json_serialization


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


class Query(BaseModel):
    """
    A full query for a semantic matching service.

    Note: This can be expanded, if needed

    :cvar return_matches: How many matches the semantic matching service shoulr return
    :cvar query_parameters: List of QueryParameters
    """
    return_matches: int = 5
    query_parameters: List[QueryParameter]


@dataclasses.dataclass
class QueryResult:
    """
    The singular result of a semantic matching query

    :cvar matching_method: The method used for matching. This should be the class of
        matching algorithm used, for example:  "NLP with paraphrase classification"
        Todo: Determine a naming scheme, possibly via semanticID
    :cvar matching_algorithm: The specific matching algorithm used
    Todo: I have not yet decided what would be the best way to return the found object
    :cvar matched_identifiable:
    :cvar matched_object_path: 
    """
    matching_method: str
    matching_algorithm: str
    matching_confidence: float
    matched_identifiable: model.Identifiable
    matched_object_path: str


def query_result_to_json_str(query_result: QueryResult) -> str:
    return json.dumps(
        {
            "matching_method": query_result.matching_method,
            "matching_algorithm": query_result.matching_algorithm,
            "matching_confidence": query_result.matching_confidence,
            "matched_identifiable": query_result.matched_identifiable,
            "matched_object_path": query_result.matched_object_path
        },
        cls=json_serialization.AASToJsonEncoder
    )
