# UpdateVpsConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**name** | **str** | New name for the VPS | [optional] 
**hostname** | **str** | New hostname for the VPS | [optional] 
**auto_start** | **int** | Auto-start on boot (0 or 1) | [optional] 
**boot** | **str** | Boot order configuration | [optional] 
**ide2** | **str** | IDE2 device configuration | [optional] 
**cdrom** | **str** | CD-ROM configuration | [optional] 

## Example

```python
from hostafrica_sdk_python.models.update_vps_config_input import UpdateVpsConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVpsConfigInput from a JSON string
update_vps_config_input_instance = UpdateVpsConfigInput.from_json(json)
# print the JSON string representation of the object
print(UpdateVpsConfigInput.to_json())

# convert the object into a dict
update_vps_config_input_dict = update_vps_config_input_instance.to_dict()
# create an instance of UpdateVpsConfigInput from a dict
update_vps_config_input_from_dict = UpdateVpsConfigInput.from_dict(update_vps_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


