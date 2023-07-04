# VideoTokenResponseFiles


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**expires** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_token_response_files import VideoTokenResponseFiles

# TODO update the JSON string below
json = "{}"
# create an instance of VideoTokenResponseFiles from a JSON string
video_token_response_files_instance = VideoTokenResponseFiles.from_json(json)
# print the JSON string representation of the object
print VideoTokenResponseFiles.to_json()

# convert the object into a dict
video_token_response_files_dict = video_token_response_files_instance.to_dict()
# create an instance of VideoTokenResponseFiles from a dict
video_token_response_files_form_dict = video_token_response_files.from_dict(video_token_response_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


