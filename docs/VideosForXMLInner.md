# VideosForXMLInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | video watch page URL | [optional] 
**guid** | **str** | video canonical URL | [optional] 
**pub_date** | **datetime** | video publication date | [optional] 
**description** | **str** | video description | [optional] 
**contentencoded** | **str** | video description | [optional] 
**dccreator** | **str** | publisher user name | [optional] 
**mediacategory** | **int** | video category (MRSS) | [optional] 
**mediacommunity** | [**VideosForXMLInnerMediaCommunity**](VideosForXMLInnerMediaCommunity.md) |  | [optional] 
**mediaembed** | [**VideosForXMLInnerMediaEmbed**](VideosForXMLInnerMediaEmbed.md) |  | [optional] 
**mediaplayer** | [**VideosForXMLInnerMediaPlayer**](VideosForXMLInnerMediaPlayer.md) |  | [optional] 
**mediathumbnail** | [**VideosForXMLInnerMediaThumbnail**](VideosForXMLInnerMediaThumbnail.md) |  | [optional] 
**mediatitle** | **str** | see [media:title](https://www.rssboard.org/media-rss#media-title) (MRSS). We only use &#x60;plain&#x60; titles. | [optional] 
**mediadescription** | **str** |  | [optional] 
**mediarating** | **str** | see [media:rating](https://www.rssboard.org/media-rss#media-rating) (MRSS) | [optional] 
**enclosure** | [**VideosForXMLInnerEnclosure**](VideosForXMLInnerEnclosure.md) |  | [optional] 
**mediagroup** | [**List[VideosForXMLInnerMediaGroupInner]**](VideosForXMLInnerMediaGroupInner.md) | list of streamable files for the video. see [media:peerLink](https://www.rssboard.org/media-rss#media-peerlink) and [media:content](https://www.rssboard.org/media-rss#media-content) or  (MRSS) | [optional] 

## Example

```python
from peertube_api_client.models.videos_for_xml_inner import VideosForXMLInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideosForXMLInner from a JSON string
videos_for_xml_inner_instance = VideosForXMLInner.from_json(json)
# print the JSON string representation of the object
print VideosForXMLInner.to_json()

# convert the object into a dict
videos_for_xml_inner_dict = videos_for_xml_inner_instance.to_dict()
# create an instance of VideosForXMLInner from a dict
videos_for_xml_inner_form_dict = videos_for_xml_inner.from_dict(videos_for_xml_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


