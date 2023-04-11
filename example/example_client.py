import json
import requests

from semantic_matching_interface import query, response


if __name__ == '__main__':
    # Above all, we try to find out what the server we connect to can do.
    print("Finding out about the Service")
    print("Get 'http://localhost:8000/semantic_matching_service_information'")
    response = requests.get(
        "http://localhost:8000/semantic_matching_service_information"
    )
    print(json.dumps(response.json(), indent=2))
    print("\n")
    # First, we're going to query an AAS
    print("Finding AAS that match to my query")
    print("Get http://localhost:8000/semantic_query_asset_administration_shell")
    aas_query = query.AssetAdministrationShellQuery(
        return_matches=2,
        query_parameters = [
            query.QueryParameter(
                attribute_name="idShort",
                attribute_value="doesNotMatter"
            )
        ]
    )
    response = requests.get(
        "http://localhost:8000/semantic_query_asset_administration_shell",
        data=aas_query.json()
    )
    print(json.dumps(response.json(), indent=2))

    # Now, we're going to query an AAS for specific SubmodelElements
    print("Finding SubmodelElements that match to my query")
    print("Get http://localhost:8000/semantic_query_submodel_element")
    submodel_element_query = query.SubmodelElementQuery(
        return_matches=2,
        query_parameters=[
            query.QueryParameter(
                attribute_name="idShort",
                attribute_value="doesNotMatter"
            )
        ],
        aas_identifier_id="https://example.com/shells/1",
        aas_identifier_id_type="IRI"
    )
    response = requests.get(
        "http://localhost:8000/semantic_query_submodel_element",
        data=submodel_element_query.json()
    )
    print(json.dumps(response.json(), indent=2))
