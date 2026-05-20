# VpsOsInfo

Operating system information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | OS name or identifier | [optional] 
**version** | **str** | OS version | [optional] 

## Example

```python
from ha_sdk_python.models.vps_os_info import VpsOsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VpsOsInfo from a JSON string
vps_os_info_instance = VpsOsInfo.from_json(json)
# print the JSON string representation of the object
print(VpsOsInfo.to_json())

# convert the object into a dict
vps_os_info_dict = vps_os_info_instance.to_dict()
# create an instance of VpsOsInfo from a dict
vps_os_info_from_dict = VpsOsInfo.from_dict(vps_os_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


