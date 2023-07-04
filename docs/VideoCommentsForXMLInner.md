# VideoCommentsForXMLInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**pub_date** | **datetime** |  | [optional] 
**contentencoded** | **str** |  | [optional] 
**dccreator** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_comments_for_xml_inner import VideoCommentsForXMLInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideoCommentsForXMLInner from a JSON string
video_comments_for_xml_inner_instance = VideoCommentsForXMLInner.from_json(json)
# print the JSON string representation of the object
print VideoCommentsForXMLInner.to_json()

# convert the object into a dict
video_comments_for_xml_inner_dict = video_comments_for_xml_inner_instance.to_dict()
# create an instance of VideoCommentsForXMLInner from a dict
video_comments_for_xml_inner_form_dict = video_comments_for_xml_inner.from_dict(video_comments_for_xml_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


