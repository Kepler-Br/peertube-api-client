# AddVideoChannelSync200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_channel_sync** | [**VideoChannelSync**](VideoChannelSync.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.add_video_channel_sync200_response import AddVideoChannelSync200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddVideoChannelSync200Response from a JSON string
add_video_channel_sync200_response_instance = AddVideoChannelSync200Response.from_json(json)
# print the JSON string representation of the object
print AddVideoChannelSync200Response.to_json()

# convert the object into a dict
add_video_channel_sync200_response_dict = add_video_channel_sync200_response_instance.to_dict()
# create an instance of AddVideoChannelSync200Response from a dict
add_video_channel_sync200_response_form_dict = add_video_channel_sync200_response.from_dict(add_video_channel_sync200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


