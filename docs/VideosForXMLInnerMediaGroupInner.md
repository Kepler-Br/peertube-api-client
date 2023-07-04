# VideosForXMLInnerMediaGroupInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**framerate** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.videos_for_xml_inner_media_group_inner import VideosForXMLInnerMediaGroupInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideosForXMLInnerMediaGroupInner from a JSON string
videos_for_xml_inner_media_group_inner_instance = VideosForXMLInnerMediaGroupInner.from_json(json)
# print the JSON string representation of the object
print VideosForXMLInnerMediaGroupInner.to_json()

# convert the object into a dict
videos_for_xml_inner_media_group_inner_dict = videos_for_xml_inner_media_group_inner_instance.to_dict()
# create an instance of VideosForXMLInnerMediaGroupInner from a dict
videos_for_xml_inner_media_group_inner_form_dict = videos_for_xml_inner_media_group_inner.from_dict(videos_for_xml_inner_media_group_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


