# ImportVideosInChannelCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_channel_url** | **str** |  | 
**video_channel_sync_id** | **int** | If part of a channel sync process, specify its id to assign video imports to this channel synchronization | [optional] 

## Example

```python
from peertube_api_client.models.import_videos_in_channel_create import ImportVideosInChannelCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ImportVideosInChannelCreate from a JSON string
import_videos_in_channel_create_instance = ImportVideosInChannelCreate.from_json(json)
# print the JSON string representation of the object
print ImportVideosInChannelCreate.to_json()

# convert the object into a dict
import_videos_in_channel_create_dict = import_videos_in_channel_create_instance.to_dict()
# create an instance of ImportVideosInChannelCreate from a dict
import_videos_in_channel_create_form_dict = import_videos_in_channel_create.from_dict(import_videos_in_channel_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


