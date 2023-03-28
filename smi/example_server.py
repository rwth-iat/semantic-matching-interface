import time

from fastapi import FastAPI

from basyx.aas import model

from model import Query, QueryResult, query_result_to_json_str

app = FastAPI()


PROPERTY: model.Property = model.Property(
    id_short="testProperty",
    value_type=model.datatypes.String,
    value="Hello World",
    semantic_id=model.Reference(
        key=(model.Key(
            type_=model.KeyElements.GLOBAL_REFERENCE,
            local=False,
            value="https://find_me.com",
            id_type=model.KeyType.IRI
        ),)
    )
)
SUBMODEL: model.Submodel = model.Submodel(
    identification=model.Identifier(
        id_="https://example.com/submodels/exampleSubmdoel",
        id_type=model.IdentifierType.IRI
    ),
    submodel_element=[PROPERTY],
    id_short="testSubmodel",
    semantic_id=model.Reference(
        key=(model.Key(
            type_=model.KeyElements.GLOBAL_REFERENCE,
            local=False,
            value="https://example.com/submodelSemantic",
            id_type=model.KeyType.IRI
        ),)
    )
)


@app.get("/semantic_query")
def semantic_query(query: Query):
    """
    Query the Semantic Matching Service and return the Result

    :param query: The Query-Parameters
    :return: The JSON-serialized QueryResult
    """
    print("Received Query:")
    print(f"\treturn_matches: {query.return_matches}")
    print("\tquery_parameters:")
    for query_parameter in query.query_parameters:
        print(f"\t\t({query_parameter.attribute_name}: "
              f"{query_parameter.attribute_value})")
    # In Reality, we would take the query here and try to find the suiting semantically
    # matched SubmodelElement. using the semantic matching service.
    # Here, we just act, as if we did that.
    time.sleep(1)
    # Our semantic matching service resulted in PROPERTY, part of SUBMODEL
    found_identifiable = SUBMODEL
    found_object_path = "./testProperty"
    query_result = QueryResult(
        matching_method="BogusMethod",
        matching_algorithm="I did not match anything at all",
        matching_confidence=1.,
        matched_identifiable=found_identifiable,
        matched_object_path=found_object_path
    )
    return query_result_to_json_str(query_result)  # Todo: This should be a list


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
