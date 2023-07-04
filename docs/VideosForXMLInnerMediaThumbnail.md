# VideosForXMLInnerMediaThumbnail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.videos_for_xml_inner_media_thumbnail import VideosForXMLInnerMediaThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of VideosForXMLInnerMediaThumbnail from a JSON string
videos_for_xml_inner_media_thumbnail_instance = VideosForXMLInnerMediaThumbnail.from_json(json)
# print the JSON string representation of the object
print VideosForXMLInnerMediaThumbnail.to_json()

# convert the object into a dict
videos_for_xml_inner_media_thumbnail_dict = videos_for_xml_inner_media_thumbnail_instance.to_dict()
# create an instance of VideosForXMLInnerMediaThumbnail from a dict
videos_for_xml_inner_media_thumbnail_form_dict = videos_for_xml_inner_media_thumbnail.from_dict(videos_for_xml_inner_media_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


