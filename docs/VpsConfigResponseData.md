# VpsConfigResponseData

Response data for VPS configuration retrieval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**hostname** | **str** | Hostname of the VPS | [optional] 
**is_kvm** | **bool** | Whether the VPS uses KVM virtualisation | [optional] 
**sshkeys_enabled** | **bool** | Whether SSH key management is enabled for this VPS | [optional] 
**available_boot_order** | **object** | Available boot order options keyed by device identifier | [optional] 
**boot_order0** | **str** | Primary boot order slot (device identifier, or null) | [optional] 
**boot_order1** | **str** | Secondary boot order slot (device identifier, or null) | [optional] 
**boot_order2** | **str** | Tertiary boot order slot (device identifier, or null) | [optional] 
**sshkeys** | **str** | Current SSH key(s) configured on the VPS (cloud-init) | [optional] 

## Example

```python
from hostafrica_sdk_python.models.vps_config_response_data import VpsConfigResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of VpsConfigResponseData from a JSON string
vps_config_response_data_instance = VpsConfigResponseData.from_json(json)
# print the JSON string representation of the object
print(VpsConfigResponseData.to_json())

# convert the object into a dict
vps_config_response_data_dict = vps_config_response_data_instance.to_dict()
# create an instance of VpsConfigResponseData from a dict
vps_config_response_data_from_dict = VpsConfigResponseData.from_dict(vps_config_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


