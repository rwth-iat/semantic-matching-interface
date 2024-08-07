# Use Cases

This document is a living collection of the possible Use Cases for a Semantic Matching in the context of Industrie 4.0.

## System Designer 1

In this example, an engineer wants to design a system and needs an electric motor with specific properties. 
As the engineer uses ECLASS in his engineering software environment, he has the ECLASS identifier of such a pump ready: `0173-1#01-AFX880#003`.
Now he wants to use this identifier to search a manufacturer's asset administration shell repository server for AAS, which describes an electric motor as an asset, but the manufacturer uses CDD identifiers for its products, e.g: `0112/2///61360_4#AAA167#001`.
Semantic matching of the ECLASS identifier to the CDD identifier is therefore necessary. 

## System Designer 2

In the second step, the engineer now searches within the matching AAS for special technical properties of the motor to see whether the motor found meets the requirements of his system, for example the power output of the motor.
Again, semantic matching is required when searching within a AAS.

## Submodel Templates

In this example, a company that has created proprietary AAS submodels for its products, now wants to check the conformity of its submodel instances to a newly published submodel template.
All the required information may already be available in the proprietary submodels, but not in the standardised form and can therefore be converted to the form of the submodel template. 
Semantic matching is required to check conformity and possibly even to automatically transfer the submodel instances into the standardised form specified by the submodel template.

## Harmonization of Semantic Catalogues
Semantic Catalogues, such as ECLASS or the IEC 61360-4 Common Data Dictionary contain semantic definitions. 
These catalogues may have overlaps in their definition space, however may also slightly differ in the specifics of their definition.
Harmonization is an ongoing process between these catalogues, where their definitions are compared and adapted to each other. 
This process can be simplified by methods of semantic matching. 

## Data Integration

A similar use case is the transfer of data, which is available in non-standardised form but with semantic annotations, into AAS submodels if the semantic annotations and the `semanticIds` of the submodels can be semantically matched.

## Matching of Skills

Another use case is the matching of skills in a process plant. 
Here, a process recipe defines a required capability, e.g. the mixing of two chemicals with a strong exothermic reaction. 
This capability must be matched to the existing capabilities offered by the process engineering components, e.g. to the existing mixing container, which must fulfil the requirements of the chemicals and their chemical reaction.
With a heterogeneous semantic description of capabilities, semantic matching is necessary for this.

## Data Analysis

This example deals with the automated application of data pre-processing algorithms. 
A data analyst has a series of algorithms for data preprocessing that are equipped with a semantic description. 
If they now wants to find out which algorithm can be applied to a data series with semantically described metadata, they also needs semantic matching for this. 

## Matching between Information Models
Information models, such as Asset Administration Shell Submodels and OPC UA Companion Specifications may contain similar information, however modeled slightly differently.
Semantic Matching can be the first step for transforming information in one model to the information in another. 

# Classification of Use Cases

The presented use cases can be classified to several specific functional requirements:

## Find AAS with given Semantic
- [System Designer 1](#system-designer-1)

## Find a SubmodelElement with given Semantic (inside a given AAS) 
- [System Designer 2](#system-designer-2)
- [Submodel Templates](#submodel-templates)
- [Data Integration](#data-integration)

## Are Properties A and B semantically equivalent?
- [Matching of Skills](#matching-of-skills)
- [Data Analysis](#data-analysis)
