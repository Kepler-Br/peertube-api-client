# VideoRedundancy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**redundancies** | [**VideoRedundancyRedundancies**](VideoRedundancyRedundancies.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_redundancy import VideoRedundancy

# TODO update the JSON string below
json = "{}"
# create an instance of VideoRedundancy from a JSON string
video_redundancy_instance = VideoRedundancy.from_json(json)
# print the JSON string representation of the object
print VideoRedundancy.to_json()

# convert the object into a dict
video_redundancy_dict = video_redundancy_instance.to_dict()
# create an instance of VideoRedundancy from a dict
video_redundancy_form_dict = video_redundancy.from_dict(video_redundancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


