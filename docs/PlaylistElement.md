# PlaylistElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** |  | [optional] 
**start_timestamp** | **int** |  | [optional] 
**stop_timestamp** | **int** |  | [optional] 
**video** | [**Video**](Video.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.playlist_element import PlaylistElement

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistElement from a JSON string
playlist_element_instance = PlaylistElement.from_json(json)
# print the JSON string representation of the object
print PlaylistElement.to_json()

# convert the object into a dict
playlist_element_dict = playlist_element_instance.to_dict()
# create an instance of PlaylistElement from a dict
playlist_element_form_dict = playlist_element.from_dict(playlist_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


