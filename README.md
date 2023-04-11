# Semantic Matching Interface

This Python library defines an abstract API for semantically matching 
Asset Administration Shell objects. This standardized API should be used, 
when implementing Semantic Matching Services.

**Note that this is an early Work-in-Progress implementation and everything
will be very much subject to change!** 

## How to use

- `interface.py` defines the routes a  
  semantic matching service should offer
- `query.py` defines how the query parameters
  should look
- `response.py` defines the responses

A service that wants to implement this API may inherit from the
`interface.AbstractSemanticMatchingInterface`:

```python
from semantic_matching_interface.interface import AbstractSemanticMatchingInterface
from semantic_matching_interface import response

class MySemanticMatchingService(AbstractSemanticMatchingInterface):
    def semantic_matching_service_information(self):
        # Todo: Your implementation here
        return response.SemanticMatchingServiceInformation()

    # ...
```

Then all the functions/endpoints the `AbstractSemanticMatchingInterface`
defines but does not implement have to be implemented. 


## How to run the examples

In the `example` folder, a short example can be found on how an implementation
of a Semantic Matching Service using this interface could look like.
In order to get this running on your local machine, we suggest the following 
steps: 

- Clone this repository
- Create a new python virtual environment. With a terminal, navigated to the
  project root folder:

Windows:
```commandline
python -m venv venv
venv\Scripts\activate
```
Linux:
```commandline
python3 -m venv venv
source venv/bin/activate
```

- Install the requirements, as well as this library:

Windows:
```commandline
pip install -r requirements.txt
pip install -e . 
```
Linux:
```commandline
pip3 install -r requirements.txt
pip3 install -e . 
```

- Run the example server

Windows:
```commandline
python example\example_service.py 
```
Linux:
```commandline
python3 example/example_service.py 
```

- Open a second terminal and navigate to the project root folder 

Windows:
```commandline
python -m venv venv
venv\Scripts\activate
```
Linux:
```commandline
python3 -m venv venv
source venv/bin/activate
```

- Run the example client

Windows:
```commandline
python example\example_client.py 
```
Linux:
```commandline
python3 example/example_client.py 
```
