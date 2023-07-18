from typing import List

from pydantic import BaseModel


class SemanticMatchingServiceInformation(BaseModel):
    """
    The information a semantic matching service provides about itself,
    so that a client knows how to formulate the query
    """
    # (s-heppner 2023-04-11):
    # Note, that this is not yet final and subject to very much change
    matching_method: str
    matching_algorithm: str
    required_parameters: List[str]
    optional_parameters: List[str]


class BaseResponse(BaseModel):
    """
    The base response with the attributes all the other responses have in
    common.

    :cvar matching_method: The method used for the matching. For example:
        "NLP" for a semantic matching service using NLP
    :cvar matching_algorithm: The precise algorithm used for the matching
        In the above example, this would be the name of the model
    """
    matching_method: str
    matching_algorithm: str


class AssetAdministrationShellMatch(BaseModel):
    """
    The result of a semantic matching for a singular AAS

    :cvar matching_score: A float between 0 and 1 defining the confidence
        the semantic matching service had on the match
    :cvar aas_identifier_id: The `id`-field of a JSON-serialized AAS
        `Identifier`-object.
    :cvar aas_identifier_id_type: The `idType`-field of a JSON-serialized
        AAS `Identifier`-object.
    """
    matching_score: float
    aas_identifier_id: str
    aas_identifier_id_type: str


class AssetAdministrationShellMatchingResponse(BaseResponse):
    """
    The result of a successful `semantic_query_asset_administration_shell`.

    :cvar matching_method: The method used for the matching. For example:
        "NLP" for a semantic matching service using NLP
    :cvar matching_algorithm: The precise algorithm used for the matching
        In the above example, this would be the name of the model
    :cvar matching_result: List of the AssetAdministrationShells together
        with their matching scores
    """
    matching_result: List[AssetAdministrationShellMatch]


class SubmodelElementMatch(BaseModel):
    """
    The result of a semantic matching for an individual SubmodelElement

    :cvar matching_score: A float between 0 and 1 defining the confidence
        the semantic matching service had on the match
    :cvar id_short_path: idShort path to the SubmodelElement, according to
        "Specification of the AssetAdministrationShell Part 2"
    """
    matching_score: float
    id_short_path: str


class SubmodelElementMatchingResponse(BaseResponse):
    """
    The result of a successful `semantic_query_submodel_element`.

    :cvar matching_method: The method used for the matching. For example:
        "NLP" for a semantic matching service using NLP
    :cvar matching_algorithm: The precise algorithm used for the matching
        In the above example, this would be the name of the model
    :cvar matching_result: List of SubmodelElements together with their
        matching scores
    """
    aas_identifier_id: str
    aas_identifier_id_type: str
    matching_result: List[SubmodelElementMatch]


class MatchObjectsMatchingResponse(BaseResponse):
    """
    The result of a successful `semantic_match_objects`.
    """
    matching_score: float
