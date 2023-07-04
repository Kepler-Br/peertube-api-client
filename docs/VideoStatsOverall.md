# VideoStatsOverall


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_watch_time** | **float** |  | [optional] 
**total_watch_time** | **float** |  | [optional] 
**viewers_peak** | **float** |  | [optional] 
**viewers_peak_date** | **datetime** |  | [optional] 
**countries** | [**List[VideoStatsOverallCountriesInner]**](VideoStatsOverallCountriesInner.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_stats_overall import VideoStatsOverall

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStatsOverall from a JSON string
video_stats_overall_instance = VideoStatsOverall.from_json(json)
# print the JSON string representation of the object
print VideoStatsOverall.to_json()

# convert the object into a dict
video_stats_overall_dict = video_stats_overall_instance.to_dict()
# create an instance of VideoStatsOverall from a dict
video_stats_overall_form_dict = video_stats_overall.from_dict(video_stats_overall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


