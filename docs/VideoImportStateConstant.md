# VideoImportStateConstant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The video import state (Pending &#x3D; &#x60;1&#x60;, Success &#x3D; &#x60;2&#x60;, Failed &#x3D; &#x60;3&#x60;) | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_import_state_constant import VideoImportStateConstant

# TODO update the JSON string below
json = "{}"
# create an instance of VideoImportStateConstant from a JSON string
video_import_state_constant_instance = VideoImportStateConstant.from_json(json)
# print the JSON string representation of the object
print VideoImportStateConstant.to_json()

# convert the object into a dict
video_import_state_constant_dict = video_import_state_constant_instance.to_dict()
# create an instance of VideoImportStateConstant from a dict
video_import_state_constant_form_dict = video_import_state_constant.from_dict(video_import_state_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


