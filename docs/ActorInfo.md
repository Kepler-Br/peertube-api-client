# ActorInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**avatars** | [**List[ActorImage]**](ActorImage.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.actor_info import ActorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ActorInfo from a JSON string
actor_info_instance = ActorInfo.from_json(json)
# print the JSON string representation of the object
print ActorInfo.to_json()

# convert the object into a dict
actor_info_dict = actor_info_instance.to_dict()
# create an instance of ActorInfo from a dict
actor_info_form_dict = actor_info.from_dict(actor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


