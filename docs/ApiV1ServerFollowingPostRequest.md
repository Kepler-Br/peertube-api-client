# ApiV1ServerFollowingPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** |  | [optional] 
**handles** | **List[str]** |  | [optional] 

## Example

```python
from peertube_api_client.models.api_v1_server_following_post_request import ApiV1ServerFollowingPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ServerFollowingPostRequest from a JSON string
api_v1_server_following_post_request_instance = ApiV1ServerFollowingPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ServerFollowingPostRequest.to_json()

# convert the object into a dict
api_v1_server_following_post_request_dict = api_v1_server_following_post_request_instance.to_dict()
# create an instance of ApiV1ServerFollowingPostRequest from a dict
api_v1_server_following_post_request_form_dict = api_v1_server_following_post_request.from_dict(api_v1_server_following_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


