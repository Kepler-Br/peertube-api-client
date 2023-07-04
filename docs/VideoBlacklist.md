# VideoBlacklist


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**video_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**views** | **int** |  | [optional] 
**likes** | **int** |  | [optional] 
**dislikes** | **int** |  | [optional] 
**nsfw** | **bool** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_blacklist import VideoBlacklist

# TODO update the JSON string below
json = "{}"
# create an instance of VideoBlacklist from a JSON string
video_blacklist_instance = VideoBlacklist.from_json(json)
# print the JSON string representation of the object
print VideoBlacklist.to_json()

# convert the object into a dict
video_blacklist_dict = video_blacklist_instance.to_dict()
# create an instance of VideoBlacklist from a dict
video_blacklist_form_dict = video_blacklist.from_dict(video_blacklist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


