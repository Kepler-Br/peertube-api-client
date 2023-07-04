# VideoImport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**target_url** | **str** | remote URL where to find the import&#39;s source video | [optional] 
**magnet_uri** | **str** | magnet URI allowing to resolve the import&#39;s source video | [optional] 
**torrentfile** | **bytearray** | Torrent file containing only the video file | [optional] 
**torrent_name** | **str** |  | [optional] [readonly] 
**state** | [**VideoImportStateConstant**](VideoImportStateConstant.md) |  | [optional] [readonly] 
**error** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**video** | [**Video**](Video.md) |  | [optional] [readonly] 

## Example

```python
from peertube_api_client.models.video_import import VideoImport

# TODO update the JSON string below
json = "{}"
# create an instance of VideoImport from a JSON string
video_import_instance = VideoImport.from_json(json)
# print the JSON string representation of the object
print VideoImport.to_json()

# convert the object into a dict
video_import_dict = video_import_instance.to_dict()
# create an instance of VideoImport from a dict
video_import_form_dict = video_import.from_dict(video_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


