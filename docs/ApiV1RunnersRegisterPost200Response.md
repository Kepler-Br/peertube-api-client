# ApiV1RunnersRegisterPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Runner id | [optional] 
**runner_token** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_runners_register_post200_response import ApiV1RunnersRegisterPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersRegisterPost200Response from a JSON string
api_v1_runners_register_post200_response_instance = ApiV1RunnersRegisterPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersRegisterPost200Response.to_json()

# convert the object into a dict
api_v1_runners_register_post200_response_dict = api_v1_runners_register_post200_response_instance.to_dict()
# create an instance of ApiV1RunnersRegisterPost200Response from a dict
api_v1_runners_register_post200_response_form_dict = api_v1_runners_register_post200_response.from_dict(api_v1_runners_register_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


