# VideoInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | [**Uuid**](Uuid.md) |  | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_info import VideoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VideoInfo from a JSON string
video_info_instance = VideoInfo.from_json(json)
# print the JSON string representation of the object
print VideoInfo.to_json()

# convert the object into a dict
video_info_dict = video_info_instance.to_dict()
# create an instance of VideoInfo from a dict
video_info_form_dict = video_info.from_dict(video_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


