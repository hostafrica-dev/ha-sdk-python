# VpsCpuInfo

CPU usage information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_ratio** | **float** | CPU usage ratio (0.0 to 1.0) | [optional] 
**percent** | **float** | CPU usage percentage | [optional] 
**cores** | **int** | Number of CPU cores | [optional] 

## Example

```python
from hostafrica_sdk_python.models.vps_cpu_info import VpsCpuInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VpsCpuInfo from a JSON string
vps_cpu_info_instance = VpsCpuInfo.from_json(json)
# print the JSON string representation of the object
print(VpsCpuInfo.to_json())

# convert the object into a dict
vps_cpu_info_dict = vps_cpu_info_instance.to_dict()
# create an instance of VpsCpuInfo from a dict
vps_cpu_info_from_dict = VpsCpuInfo.from_dict(vps_cpu_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


