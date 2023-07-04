# MRSSGroupContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**framerate** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.mrss_group_content import MRSSGroupContent

# TODO update the JSON string below
json = "{}"
# create an instance of MRSSGroupContent from a JSON string
mrss_group_content_instance = MRSSGroupContent.from_json(json)
# print the JSON string representation of the object
print MRSSGroupContent.to_json()

# convert the object into a dict
mrss_group_content_dict = mrss_group_content_instance.to_dict()
# create an instance of MRSSGroupContent from a dict
mrss_group_content_form_dict = mrss_group_content.from_dict(mrss_group_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


