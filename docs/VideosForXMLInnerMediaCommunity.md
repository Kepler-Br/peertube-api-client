# VideosForXMLInnerMediaCommunity

see [media:community](https://www.rssboard.org/media-rss#media-community) (MRSS)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mediastatistics** | [**VideosForXMLInnerMediaCommunityMediaStatistics**](VideosForXMLInnerMediaCommunityMediaStatistics.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.videos_for_xml_inner_media_community import VideosForXMLInnerMediaCommunity

# TODO update the JSON string below
json = "{}"
# create an instance of VideosForXMLInnerMediaCommunity from a JSON string
videos_for_xml_inner_media_community_instance = VideosForXMLInnerMediaCommunity.from_json(json)
# print the JSON string representation of the object
print VideosForXMLInnerMediaCommunity.to_json()

# convert the object into a dict
videos_for_xml_inner_media_community_dict = videos_for_xml_inner_media_community_instance.to_dict()
# create an instance of VideosForXMLInnerMediaCommunity from a dict
videos_for_xml_inner_media_community_form_dict = videos_for_xml_inner_media_community.from_dict(videos_for_xml_inner_media_community_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


