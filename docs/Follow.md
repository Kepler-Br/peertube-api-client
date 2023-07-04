# Follow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**follower** | [**Actor**](Actor.md) |  | [optional] 
**following** | [**Actor**](Actor.md) |  | [optional] 
**score** | **float** | score reflecting the reachability of the actor, with steps of &#x60;10&#x60; and a base score of &#x60;1000&#x60;. | [optional] 
**state** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.follow import Follow

# TODO update the JSON string below
json = "{}"
# create an instance of Follow from a JSON string
follow_instance = Follow.from_json(json)
# print the JSON string representation of the object
print Follow.to_json()

# convert the object into a dict
follow_dict = follow_instance.to_dict()
# create an instance of Follow from a dict
follow_form_dict = follow.from_dict(follow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


