# NotificationVideoImport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**video** | [**VideoInfo**](VideoInfo.md) |  | [optional] 
**torrent_name** | **str** |  | [optional] 
**magnet_uri** | [**MagnetUri**](MagnetUri.md) |  | [optional] 
**target_uri** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.notification_video_import import NotificationVideoImport

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationVideoImport from a JSON string
notification_video_import_instance = NotificationVideoImport.from_json(json)
# print the JSON string representation of the object
print NotificationVideoImport.to_json()

# convert the object into a dict
notification_video_import_dict = notification_video_import_instance.to_dict()
# create an instance of NotificationVideoImport from a dict
notification_video_import_form_dict = notification_video_import.from_dict(notification_video_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


