from fastapi import FastAPI
import uvicorn
import basyx.aas.model

from semantic_matching_interface import interface, query, response


class ExampleSemanticMatchingService(
    interface.AbstractSemanticMatchingInterface
):
    """
    todo
    """
    def semantic_matching_service_information(self):
        return response.SemanticMatchingServiceInformation(
            matching_method="Nothing",
            matching_algorithm="This is just an example",
            required_parameters=["idShort"],
            optional_parameters=[]
        )

    def semantic_query_asset_administration_shell(
            self,
            query: query.AssetAdministrationShellQuery
    ):
        print(f"Received AAS Query: {query}")
        # Now we're doing our matching
        # It returned 2 viable AssetAdministrationShells:
        aas_identifier_1 = basyx.aas.model.Identifier(
            id_="https://example.com/shells/1",
            id_type=basyx.aas.model.IdentifierType.IRI
        )
        aas_identifier_1_matching_score: float = 0.72
        aas_identifier_2 = basyx.aas.model.Identifier(
            id_="https://example.com/shells/2",
            id_type=basyx.aas.model.IdentifierType.IRI
        )
        aas_identifier_2_matching_score: float = 0.65
        # Therefore, we can construct our matching response:
        matching_result = [
            response.AssetAdministrationShellMatch(
                matching_score=aas_identifier_1_matching_score,
                aas_identifier_id=aas_identifier_1.id,
                aas_identifier_id_type="IRI"
            ),
            response.AssetAdministrationShellMatch(
                matching_score=aas_identifier_2_matching_score,
                aas_identifier_id=aas_identifier_2.id,
                aas_identifier_id_type="IRI"
            )
        ]
        return response.AssetAdministrationShellMatchingResponse(
            matching_method="Nothing",
            matching_algorithm="This is just an example",
            matching_result=matching_result
        )

    def semantic_query_submodel_element(
            self,
            query: query.SubmodelElementQuery
    ):
        print(f"Received SubmodelElement Query: {query}")
        # Now we're doing our matching
        # The matching algorithm returned the following two SubmodelElements:
        submodel_element_path_1: str = "nameplate.someInformation"
        submodel_element_score_1: float = 0.99
        submodel_element_path_2: str = "nameplate.someOther.Information"
        submodel_element_score_2: float = 0.34
        # Now we can construct our Response:
        matching_result = [
            response.SubmodelElementMatch(
                matching_score= submodel_element_score_1,
                id_short_path=submodel_element_path_1
            ),
            response.SubmodelElementMatch(
                matching_score=submodel_element_score_2,
                id_short_path=submodel_element_path_2
            ),
        ]
        return response.SubmodelElementMatchingResponse(
            matching_method="Nothing",
            matching_algorithm="This is just an example",
            matching_result=matching_result,
            aas_identifier_id=query.aas_identifier_id,
            aas_identifier_id_type=query.aas_identifier_id_type
        )

    def semantic_match_objects(
            self,
            query: query.MatchObjectsQuery
    ):
        raise NotImplementedError

if __name__ == "__main__":
    APP = FastAPI()
    APP.include_router(ExampleSemanticMatchingService().router)
    uvicorn.run(APP, host="127.0.0.1", port=8000)
