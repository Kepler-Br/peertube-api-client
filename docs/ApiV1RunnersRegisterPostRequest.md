# ApiV1RunnersRegisterPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_token** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_runners_register_post_request import ApiV1RunnersRegisterPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersRegisterPostRequest from a JSON string
api_v1_runners_register_post_request_instance = ApiV1RunnersRegisterPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersRegisterPostRequest.to_json()

# convert the object into a dict
api_v1_runners_register_post_request_dict = api_v1_runners_register_post_request_instance.to_dict()
# create an instance of ApiV1RunnersRegisterPostRequest from a dict
api_v1_runners_register_post_request_form_dict = api_v1_runners_register_post_request.from_dict(api_v1_runners_register_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


