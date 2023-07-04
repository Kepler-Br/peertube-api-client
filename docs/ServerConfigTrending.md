# ServerConfigTrending


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**videos** | [**ServerConfigTrendingVideos**](ServerConfigTrendingVideos.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.server_config_trending import ServerConfigTrending

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigTrending from a JSON string
server_config_trending_instance = ServerConfigTrending.from_json(json)
# print the JSON string representation of the object
print ServerConfigTrending.to_json()

# convert the object into a dict
server_config_trending_dict = server_config_trending_instance.to_dict()
# create an instance of ServerConfigTrending from a dict
server_config_trending_form_dict = server_config_trending.from_dict(server_config_trending_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


