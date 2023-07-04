# VideoStatsTimeserie


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VideoStatsTimeserieDataInner]**](VideoStatsTimeserieDataInner.md) |  | [optional] 

## Example

```python
from peertube_api_client.models.video_stats_timeserie import VideoStatsTimeserie

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStatsTimeserie from a JSON string
video_stats_timeserie_instance = VideoStatsTimeserie.from_json(json)
# print the JSON string representation of the object
print VideoStatsTimeserie.to_json()

# convert the object into a dict
video_stats_timeserie_dict = video_stats_timeserie_instance.to_dict()
# create an instance of VideoStatsTimeserie from a dict
video_stats_timeserie_form_dict = video_stats_timeserie.from_dict(video_stats_timeserie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


