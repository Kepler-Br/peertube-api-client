# VideoSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_source import VideoSource

# TODO update the JSON string below
json = "{}"
# create an instance of VideoSource from a JSON string
video_source_instance = VideoSource.from_json(json)
# print the JSON string representation of the object
print VideoSource.to_json()

# convert the object into a dict
video_source_dict = video_source_instance.to_dict()
# create an instance of VideoSource from a dict
video_source_form_dict = video_source.from_dict(video_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


