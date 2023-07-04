# VideosForXMLInnerMediaPlayer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | video watch path, relative to the canonical URL domain (MRSS) | [optional] 

## Example

```python
from peertube_api_client.models.videos_for_xml_inner_media_player import VideosForXMLInnerMediaPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of VideosForXMLInnerMediaPlayer from a JSON string
videos_for_xml_inner_media_player_instance = VideosForXMLInnerMediaPlayer.from_json(json)
# print the JSON string representation of the object
print VideosForXMLInnerMediaPlayer.to_json()

# convert the object into a dict
videos_for_xml_inner_media_player_dict = videos_for_xml_inner_media_player_instance.to_dict()
# create an instance of VideosForXMLInnerMediaPlayer from a dict
videos_for_xml_inner_media_player_form_dict = videos_for_xml_inner_media_player.from_dict(videos_for_xml_inner_media_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


