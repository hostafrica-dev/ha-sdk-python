# ListDnsZonesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**zones** | [**List[DnsZoneInfo]**](DnsZoneInfo.md) | DNS zones owned by the authenticated client | 
**total** | **int** | Total number of zones | 

## Example

```python
from ha_sdk_python.models.list_dns_zones_data import ListDnsZonesData

# TODO update the JSON string below
json = "{}"
# create an instance of ListDnsZonesData from a JSON string
list_dns_zones_data_instance = ListDnsZonesData.from_json(json)
# print the JSON string representation of the object
print(ListDnsZonesData.to_json())

# convert the object into a dict
list_dns_zones_data_dict = list_dns_zones_data_instance.to_dict()
# create an instance of ListDnsZonesData from a dict
list_dns_zones_data_from_dict = ListDnsZonesData.from_dict(list_dns_zones_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


