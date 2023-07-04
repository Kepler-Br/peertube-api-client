# VideoStatsTimeserieDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from peertube_api_client.models.video_stats_timeserie_data_inner import VideoStatsTimeserieDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStatsTimeserieDataInner from a JSON string
video_stats_timeserie_data_inner_instance = VideoStatsTimeserieDataInner.from_json(json)
# print the JSON string representation of the object
print VideoStatsTimeserieDataInner.to_json()

# convert the object into a dict
video_stats_timeserie_data_inner_dict = video_stats_timeserie_data_inner_instance.to_dict()
# create an instance of VideoStatsTimeserieDataInner from a dict
video_stats_timeserie_data_inner_form_dict = video_stats_timeserie_data_inner.from_dict(video_stats_timeserie_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


