# VideoImportsList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[VideoImport]**](VideoImport.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_imports_list import VideoImportsList

# TODO update the JSON string below
json = "{}"
# create an instance of VideoImportsList from a JSON string
video_imports_list_instance = VideoImportsList.from_json(json)
# print the JSON string representation of the object
print VideoImportsList.to_json()

# convert the object into a dict
video_imports_list_dict = video_imports_list_instance.to_dict()
# create an instance of VideoImportsList from a dict
video_imports_list_form_dict = video_imports_list.from_dict(video_imports_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


