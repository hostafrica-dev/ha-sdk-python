# VpsDiskInfo

Disk usage information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_bytes** | **int** | Disk usage in bytes | [optional] 
**total_bytes** | **int** | Total disk space in bytes | [optional] 
**percent** | **float** | Disk usage percentage | [optional] 
**usage_human** | **str** | Human-readable disk usage (e.g., &#39;50 GB&#39;) | [optional] 
**total_human** | **str** | Human-readable total disk space (e.g., &#39;100 GB&#39;) | [optional] 

## Example

```python
from ha_sdk_python.models.vps_disk_info import VpsDiskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VpsDiskInfo from a JSON string
vps_disk_info_instance = VpsDiskInfo.from_json(json)
# print the JSON string representation of the object
print(VpsDiskInfo.to_json())

# convert the object into a dict
vps_disk_info_dict = vps_disk_info_instance.to_dict()
# create an instance of VpsDiskInfo from a dict
vps_disk_info_from_dict = VpsDiskInfo.from_dict(vps_disk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


