# VpsMemoryInfo

Memory usage information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_bytes** | **int** | Memory usage in bytes | [optional] 
**total_bytes** | **int** | Total memory in bytes | [optional] 
**percent** | **float** | Memory usage percentage | [optional] 
**usage_human** | **str** | Human-readable memory usage (e.g., &#39;2.5 GB&#39;) | [optional] 
**total_human** | **str** | Human-readable total memory (e.g., &#39;8 GB&#39;) | [optional] 

## Example

```python
from ha_sdk_python.models.vps_memory_info import VpsMemoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VpsMemoryInfo from a JSON string
vps_memory_info_instance = VpsMemoryInfo.from_json(json)
# print the JSON string representation of the object
print(VpsMemoryInfo.to_json())

# convert the object into a dict
vps_memory_info_dict = vps_memory_info_instance.to_dict()
# create an instance of VpsMemoryInfo from a dict
vps_memory_info_from_dict = VpsMemoryInfo.from_dict(vps_memory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


