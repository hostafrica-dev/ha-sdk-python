# VpsIpAddressDetail

Detailed IP address assignment for a VPS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | Primary IP address | 
**address** | **str** | IP address (may mirror ip) | [optional] 
**subnet** | **str** | Subnet mask | [optional] 
**gateway** | **str** | Gateway address | [optional] 
**mac** | **str** | MAC address when available | [optional] 

## Example

```python
from ha_sdk_python.models.vps_ip_address_detail import VpsIpAddressDetail

# TODO update the JSON string below
json = "{}"
# create an instance of VpsIpAddressDetail from a JSON string
vps_ip_address_detail_instance = VpsIpAddressDetail.from_json(json)
# print the JSON string representation of the object
print(VpsIpAddressDetail.to_json())

# convert the object into a dict
vps_ip_address_detail_dict = vps_ip_address_detail_instance.to_dict()
# create an instance of VpsIpAddressDetail from a dict
vps_ip_address_detail_from_dict = VpsIpAddressDetail.from_dict(vps_ip_address_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


