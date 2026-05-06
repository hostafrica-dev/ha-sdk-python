# VpsAvailableFeatures

Available features for the VPS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**power_start** | **bool** | Can start the VPS | 
**power_stop** | **bool** | Can stop the VPS | 
**power_reboot** | **bool** | Can reboot the VPS | 
**power_shutdown** | **bool** | Can shutdown the VPS | 
**novnc_console** | **bool** | Has noVNC console access | 
**backups** | **bool** | Has backup capabilities | 
**backup_jobs** | **bool** | Has backup jobs feature | 
**backup_schedule** | **bool** | Has backup schedule feature | 
**firewall** | **bool** | Has firewall feature | 
**reinstall** | **bool** | Can reinstall OS | 
**change_hostname** | **bool** | Can change hostname | 
**change_iso_image** | **bool** | Can change ISO image | 
**network_stats** | **bool** | Has network statistics feature | 
**graphs** | **bool** | Has graphs feature | 
**os_templates** | **List[str]** | List of available OS templates | 

## Example

```python
from hostafrica_sdk_python.models.vps_available_features import VpsAvailableFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of VpsAvailableFeatures from a JSON string
vps_available_features_instance = VpsAvailableFeatures.from_json(json)
# print the JSON string representation of the object
print(VpsAvailableFeatures.to_json())

# convert the object into a dict
vps_available_features_dict = vps_available_features_instance.to_dict()
# create an instance of VpsAvailableFeatures from a dict
vps_available_features_from_dict = VpsAvailableFeatures.from_dict(vps_available_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


