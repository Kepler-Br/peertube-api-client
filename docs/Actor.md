# Actor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**name** | **str** | immutable name of the user, used to find or mention its actor | [optional] 
**host** | **str** | server on which the actor is resident | [optional] 
**host_redundancy_allowed** | **bool** | whether this actor&#39;s host allows redundancy of its videos | [optional] 
**following_count** | **int** | number of actors subscribed to by this actor, as seen by this instance | [optional] 
**followers_count** | **int** | number of followers of this actor, as seen by this instance | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.actor import Actor

# TODO update the JSON string below
json = "{}"
# create an instance of Actor from a JSON string
actor_instance = Actor.from_json(json)
# print the JSON string representation of the object
print Actor.to_json()

# convert the object into a dict
actor_dict = actor_instance.to_dict()
# create an instance of Actor from a dict
actor_form_dict = actor.from_dict(actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


