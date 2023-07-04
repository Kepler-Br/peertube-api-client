# VideosForXMLInnerMediaEmbed


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | video embed path, relative to the canonical URL domain (MRSS) | [optional] 

## Example

```python
from peertube_api_client.models.videos_for_xml_inner_media_embed import VideosForXMLInnerMediaEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of VideosForXMLInnerMediaEmbed from a JSON string
videos_for_xml_inner_media_embed_instance = VideosForXMLInnerMediaEmbed.from_json(json)
# print the JSON string representation of the object
print VideosForXMLInnerMediaEmbed.to_json()

# convert the object into a dict
videos_for_xml_inner_media_embed_dict = videos_for_xml_inner_media_embed_instance.to_dict()
# create an instance of VideosForXMLInnerMediaEmbed from a dict
videos_for_xml_inner_media_embed_form_dict = videos_for_xml_inner_media_embed.from_dict(videos_for_xml_inner_media_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


