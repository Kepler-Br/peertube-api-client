# PutMirroredVideoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | **int** |  | 

## Example

```python
from peertube_api_client.models.put_mirrored_video_request import PutMirroredVideoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutMirroredVideoRequest from a JSON string
put_mirrored_video_request_instance = PutMirroredVideoRequest.from_json(json)
# print the JSON string representation of the object
print PutMirroredVideoRequest.to_json()

# convert the object into a dict
put_mirrored_video_request_dict = put_mirrored_video_request_instance.to_dict()
# create an instance of PutMirroredVideoRequest from a dict
put_mirrored_video_request_form_dict = put_mirrored_video_request.from_dict(put_mirrored_video_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


