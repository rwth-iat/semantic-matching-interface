from fastapi import APIRouter

from semantic_matching_interface import query


class AbstractSemanticMatchingInterface:
    """
    Todo
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            "/semantic_matching_service_information",
            self.semantic_matching_service_information,
            methods=["GET"]
        )
        self.router.add_api_route(
            "/semantic_query_asset_administration_shell",
            self.semantic_query_asset_administration_shell,
            methods=["GET"]
        )
        self.router.add_api_route(
            "/semantic_query_submodel_element",
            self.semantic_query_submodel_element,
            methods=["GET"]
        )
        self.router.add_api_route(
            "/semantic_match_objects",
            self.semantic_match_objects,
            methods=["GET"]
        )

    def semantic_matching_service_information(self):
        """
        Information that the Semantic Matching Service can provide about
        itself.
        Should return a `response.SemanticMatchingServiceInformation` object.
        """
        raise NotImplementedError

    def semantic_query_asset_administration_shell(
            self,
            query: query.AssetAdministrationShellQuery
    ):
        """
        A query to a set of contained AssetAdministrationShells
        (for example in an AAS Repository).

        The query will return a List of AssetAdministrationShell-Identifiers
        with the highest matching score.
        """
        raise NotImplementedError

    def semantic_query_submodel_element(
            self,
            query: query.SubmodelElementQuery
    ):
        """
        A query to a specific AssetAdministrationShell.

        The query will return a List of idShort-Paths to SubmodelElements
        which have the highest matching score to the query.
        """
        # (s-heppner 2023-04-11):
        # Todo: We may also want to provide the whole AAS for the service to
        #       match in it.
        raise NotImplementedError

    def semantic_match_objects(
            self,
            query: query.MatchObjectsQuery
    ):
        """
        A query to match two SubmodelElements semantically.

        Returns a matching score
        """
        raise NotImplementedError
