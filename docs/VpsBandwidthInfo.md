# VpsBandwidthInfo

Bandwidth usage information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_mb** | **float** | Bandwidth usage in MB | [optional] 
**limit_mb** | **float** | Bandwidth limit in MB | [optional] 
**unlimited** | **bool** | Whether bandwidth is unlimited | 
**percent** | **float** | Bandwidth usage percentage | [optional] 

## Example

```python
from hostafrica_sdk_python.models.vps_bandwidth_info import VpsBandwidthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VpsBandwidthInfo from a JSON string
vps_bandwidth_info_instance = VpsBandwidthInfo.from_json(json)
# print the JSON string representation of the object
print(VpsBandwidthInfo.to_json())

# convert the object into a dict
vps_bandwidth_info_dict = vps_bandwidth_info_instance.to_dict()
# create an instance of VpsBandwidthInfo from a dict
vps_bandwidth_info_from_dict = VpsBandwidthInfo.from_dict(vps_bandwidth_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


