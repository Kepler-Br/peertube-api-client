# VideoPrivacyConstant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**VideoPrivacySet**](VideoPrivacySet.md) |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_privacy_constant import VideoPrivacyConstant

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPrivacyConstant from a JSON string
video_privacy_constant_instance = VideoPrivacyConstant.from_json(json)
# print the JSON string representation of the object
print VideoPrivacyConstant.to_json()

# convert the object into a dict
video_privacy_constant_dict = video_privacy_constant_instance.to_dict()
# create an instance of VideoPrivacyConstant from a dict
video_privacy_constant_form_dict = video_privacy_constant.from_dict(video_privacy_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


