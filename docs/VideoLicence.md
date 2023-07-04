# VideoLicence

licence under which the video is distributed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_licence import VideoLicence

# TODO update the JSON string below
json = "{}"
# create an instance of VideoLicence from a JSON string
video_licence_instance = VideoLicence.from_json(json)
# print the JSON string representation of the object
print VideoLicence.to_json()

# convert the object into a dict
video_licence_dict = video_licence_instance.to_dict()
# create an instance of VideoLicence from a dict
video_licence_form_dict = video_licence.from_dict(video_licence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


