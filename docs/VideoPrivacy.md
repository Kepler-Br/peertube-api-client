# VideoPrivacy

privacy policy used to distribute the video

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**VideoPrivacySet**](VideoPrivacySet.md) |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_privacy import VideoPrivacy

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPrivacy from a JSON string
video_privacy_instance = VideoPrivacy.from_json(json)
# print the JSON string representation of the object
print VideoPrivacy.to_json()

# convert the object into a dict
video_privacy_dict = video_privacy_instance.to_dict()
# create an instance of VideoPrivacy from a dict
video_privacy_form_dict = video_privacy.from_dict(video_privacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


