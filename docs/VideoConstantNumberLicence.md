# VideoConstantNumberLicence


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_constant_number_licence import VideoConstantNumberLicence

# TODO update the JSON string below
json = "{}"
# create an instance of VideoConstantNumberLicence from a JSON string
video_constant_number_licence_instance = VideoConstantNumberLicence.from_json(json)
# print the JSON string representation of the object
print VideoConstantNumberLicence.to_json()

# convert the object into a dict
video_constant_number_licence_dict = video_constant_number_licence_instance.to_dict()
# create an instance of VideoConstantNumberLicence from a dict
video_constant_number_licence_form_dict = video_constant_number_licence.from_dict(video_constant_number_licence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


