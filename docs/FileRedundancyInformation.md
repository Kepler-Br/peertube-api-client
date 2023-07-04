# FileRedundancyInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**file_url** | **str** |  | [optional] 
**strategy** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**expires_on** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.file_redundancy_information import FileRedundancyInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FileRedundancyInformation from a JSON string
file_redundancy_information_instance = FileRedundancyInformation.from_json(json)
# print the JSON string representation of the object
print FileRedundancyInformation.to_json()

# convert the object into a dict
file_redundancy_information_dict = file_redundancy_information_instance.to_dict()
# create an instance of FileRedundancyInformation from a dict
file_redundancy_information_form_dict = file_redundancy_information.from_dict(file_redundancy_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


