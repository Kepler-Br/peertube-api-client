# MRSSPeerLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from peertube_api_client.models.mrss_peer_link import MRSSPeerLink

# TODO update the JSON string below
json = "{}"
# create an instance of MRSSPeerLink from a JSON string
mrss_peer_link_instance = MRSSPeerLink.from_json(json)
# print the JSON string representation of the object
print MRSSPeerLink.to_json()

# convert the object into a dict
mrss_peer_link_dict = mrss_peer_link_instance.to_dict()
# create an instance of MRSSPeerLink from a dict
mrss_peer_link_form_dict = mrss_peer_link.from_dict(mrss_peer_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


