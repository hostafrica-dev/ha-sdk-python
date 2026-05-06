# RebootVpsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.reboot_vps_input import RebootVpsInput

# TODO update the JSON string below
json = "{}"
# create an instance of RebootVpsInput from a JSON string
reboot_vps_input_instance = RebootVpsInput.from_json(json)
# print the JSON string representation of the object
print(RebootVpsInput.to_json())

# convert the object into a dict
reboot_vps_input_dict = reboot_vps_input_instance.to_dict()
# create an instance of RebootVpsInput from a dict
reboot_vps_input_from_dict = RebootVpsInput.from_dict(reboot_vps_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


