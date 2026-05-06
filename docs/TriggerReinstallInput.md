# TriggerReinstallInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**template** | **str** | Template identifier for the OS to reinstall | 

## Example

```python
from hostafrica_sdk_python.models.trigger_reinstall_input import TriggerReinstallInput

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerReinstallInput from a JSON string
trigger_reinstall_input_instance = TriggerReinstallInput.from_json(json)
# print the JSON string representation of the object
print(TriggerReinstallInput.to_json())

# convert the object into a dict
trigger_reinstall_input_dict = trigger_reinstall_input_instance.to_dict()
# create an instance of TriggerReinstallInput from a dict
trigger_reinstall_input_from_dict = TriggerReinstallInput.from_dict(trigger_reinstall_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


