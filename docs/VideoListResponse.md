# VideoListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[Video]**](Video.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_list_response import VideoListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VideoListResponse from a JSON string
video_list_response_instance = VideoListResponse.from_json(json)
# print the JSON string representation of the object
print VideoListResponse.to_json()

# convert the object into a dict
video_list_response_dict = video_list_response_instance.to_dict()
# create an instance of VideoListResponse from a dict
video_list_response_form_dict = video_list_response.from_dict(video_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


