# GetMyAbuses200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[Abuse]**](Abuse.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.get_my_abuses200_response import GetMyAbuses200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyAbuses200Response from a JSON string
get_my_abuses200_response_instance = GetMyAbuses200Response.from_json(json)
# print the JSON string representation of the object
print GetMyAbuses200Response.to_json()

# convert the object into a dict
get_my_abuses200_response_dict = get_my_abuses200_response_instance.to_dict()
# create an instance of GetMyAbuses200Response from a dict
get_my_abuses200_response_form_dict = get_my_abuses200_response.from_dict(get_my_abuses200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


