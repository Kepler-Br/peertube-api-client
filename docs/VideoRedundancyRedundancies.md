# VideoRedundancyRedundancies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileRedundancyInformation]**](FileRedundancyInformation.md) |  | [optional] 
**streaming_playlists** | [**List[FileRedundancyInformation]**](FileRedundancyInformation.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_redundancy_redundancies import VideoRedundancyRedundancies

# TODO update the JSON string below
json = "{}"
# create an instance of VideoRedundancyRedundancies from a JSON string
video_redundancy_redundancies_instance = VideoRedundancyRedundancies.from_json(json)
# print the JSON string representation of the object
print VideoRedundancyRedundancies.to_json()

# convert the object into a dict
video_redundancy_redundancies_dict = video_redundancy_redundancies_instance.to_dict()
# create an instance of VideoRedundancyRedundancies from a dict
video_redundancy_redundancies_form_dict = video_redundancy_redundancies.from_dict(video_redundancy_redundancies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


