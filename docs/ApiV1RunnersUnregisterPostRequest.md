# ApiV1RunnersUnregisterPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runner_token** | **str** |  | 

## Example

```python
from peertube_api_client.models.api_v1_runners_unregister_post_request import ApiV1RunnersUnregisterPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RunnersUnregisterPostRequest from a JSON string
api_v1_runners_unregister_post_request_instance = ApiV1RunnersUnregisterPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1RunnersUnregisterPostRequest.to_json()

# convert the object into a dict
api_v1_runners_unregister_post_request_dict = api_v1_runners_unregister_post_request_instance.to_dict()
# create an instance of ApiV1RunnersUnregisterPostRequest from a dict
api_v1_runners_unregister_post_request_form_dict = api_v1_runners_unregister_post_request.from_dict(api_v1_runners_unregister_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


