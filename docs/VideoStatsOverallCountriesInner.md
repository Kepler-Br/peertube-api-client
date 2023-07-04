# VideoStatsOverallCountriesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_code** | **str** |  | [optional] 
**viewers** | **float** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_stats_overall_countries_inner import VideoStatsOverallCountriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStatsOverallCountriesInner from a JSON string
video_stats_overall_countries_inner_instance = VideoStatsOverallCountriesInner.from_json(json)
# print the JSON string representation of the object
print VideoStatsOverallCountriesInner.to_json()

# convert the object into a dict
video_stats_overall_countries_inner_dict = video_stats_overall_countries_inner_instance.to_dict()
# create an instance of VideoStatsOverallCountriesInner from a dict
video_stats_overall_countries_inner_form_dict = video_stats_overall_countries_inner.from_dict(video_stats_overall_countries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


