# ActorImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from peertube_api_client.models.actor_image import ActorImage

# TODO update the JSON string below
json = "{}"
# create an instance of ActorImage from a JSON string
actor_image_instance = ActorImage.from_json(json)
# print the JSON string representation of the object
print ActorImage.to_json()

# convert the object into a dict
actor_image_dict = actor_image_instance.to_dict()
# create an instance of ActorImage from a dict
actor_image_form_dict = actor_image.from_dict(actor_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


