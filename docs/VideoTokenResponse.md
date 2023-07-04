# VideoTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**VideoTokenResponseFiles**](VideoTokenResponseFiles.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_token_response import VideoTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VideoTokenResponse from a JSON string
video_token_response_instance = VideoTokenResponse.from_json(json)
# print the JSON string representation of the object
print VideoTokenResponse.to_json()

# convert the object into a dict
video_token_response_dict = video_token_response_instance.to_dict()
# create an instance of VideoTokenResponse from a dict
video_token_response_form_dict = video_token_response.from_dict(video_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


