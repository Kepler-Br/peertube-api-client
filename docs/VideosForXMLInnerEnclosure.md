# VideosForXMLInnerEnclosure

main streamable file for the video

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**length** | **int** |  | [optional] 

## Example

```python
from peertube_api_client.models.videos_for_xml_inner_enclosure import VideosForXMLInnerEnclosure

# TODO update the JSON string below
json = "{}"
# create an instance of VideosForXMLInnerEnclosure from a JSON string
videos_for_xml_inner_enclosure_instance = VideosForXMLInnerEnclosure.from_json(json)
# print the JSON string representation of the object
print VideosForXMLInnerEnclosure.to_json()

# convert the object into a dict
videos_for_xml_inner_enclosure_dict = videos_for_xml_inner_enclosure_instance.to_dict()
# create an instance of VideosForXMLInnerEnclosure from a dict
videos_for_xml_inner_enclosure_form_dict = videos_for_xml_inner_enclosure.from_dict(videos_for_xml_inner_enclosure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


