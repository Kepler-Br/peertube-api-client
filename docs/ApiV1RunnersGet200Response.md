# ApiV1RunnersGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[Runner]**](Runner.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_runners_get200_response import ApiV1RunnersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersGet200Response from a JSON string
api_v1_runners_get200_response_instance = ApiV1RunnersGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersGet200Response.to_json()

# convert the object into a dict
api_v1_runners_get200_response_dict = api_v1_runners_get200_response_instance.to_dict()
# create an instance of ApiV1RunnersGet200Response from a dict
api_v1_runners_get200_response_form_dict = api_v1_runners_get200_response.from_dict(api_v1_runners_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


