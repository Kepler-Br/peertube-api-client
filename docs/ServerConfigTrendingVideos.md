# ServerConfigTrendingVideos


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_days** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_trending_videos import ServerConfigTrendingVideos

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigTrendingVideos from a JSON string
server_config_trending_videos_instance = ServerConfigTrendingVideos.from_json(json)
# print the JSON string representation of the object
print ServerConfigTrendingVideos.to_json()

# convert the object into a dict
server_config_trending_videos_dict = server_config_trending_videos_instance.to_dict()
# create an instance of ServerConfigTrendingVideos from a dict
server_config_trending_videos_form_dict = server_config_trending_videos.from_dict(server_config_trending_videos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


