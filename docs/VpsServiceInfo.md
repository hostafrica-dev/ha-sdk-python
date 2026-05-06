# VpsServiceInfo

VPS service information matching upstream API format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Service ID (integer) | 
**product** | **str** | Product name | 
**hostname** | **str** | Hostname of the VPS | 
**status** | **str** | Service status | 
**ips** | **List[str]** | List of IP addresses assigned to this VPS | 
**created_at** | **str** | Service creation date (YYYY-MM-DD format) | 

## Example

```python
from hostafrica_sdk_python.models.vps_service_info import VpsServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VpsServiceInfo from a JSON string
vps_service_info_instance = VpsServiceInfo.from_json(json)
# print the JSON string representation of the object
print(VpsServiceInfo.to_json())

# convert the object into a dict
vps_service_info_dict = vps_service_info_instance.to_dict()
# create an instance of VpsServiceInfo from a dict
vps_service_info_from_dict = VpsServiceInfo.from_dict(vps_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


