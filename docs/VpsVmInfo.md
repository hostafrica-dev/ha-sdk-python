# VpsVmInfo

VM information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | VM status (e.g., running, stopped) | 
**uptime** | **str** | Uptime in human-readable format | [optional] 
**uptime_seconds** | **int** | Uptime in seconds | [optional] 
**hostname** | **str** | Hostname of the VM | [optional] 
**boot_devices** | **str** | Boot devices configuration | [optional] 
**vmid** | **str** | Proxmox VM ID | 
**node** | **str** | Proxmox node name | 
**virtualization** | **str** | Virtualization type (qemu or lxc) | 

## Example

```python
from hostafrica_sdk_python.models.vps_vm_info import VpsVmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VpsVmInfo from a JSON string
vps_vm_info_instance = VpsVmInfo.from_json(json)
# print the JSON string representation of the object
print(VpsVmInfo.to_json())

# convert the object into a dict
vps_vm_info_dict = vps_vm_info_instance.to_dict()
# create an instance of VpsVmInfo from a dict
vps_vm_info_from_dict = VpsVmInfo.from_dict(vps_vm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


