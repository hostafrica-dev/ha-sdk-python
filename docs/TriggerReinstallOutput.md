# TriggerReinstallOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**TriggerReinstallResponseData**](TriggerReinstallResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.trigger_reinstall_output import TriggerReinstallOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerReinstallOutput from a JSON string
trigger_reinstall_output_instance = TriggerReinstallOutput.from_json(json)
# print the JSON string representation of the object
print(TriggerReinstallOutput.to_json())

# convert the object into a dict
trigger_reinstall_output_dict = trigger_reinstall_output_instance.to_dict()
# create an instance of TriggerReinstallOutput from a dict
trigger_reinstall_output_from_dict = TriggerReinstallOutput.from_dict(trigger_reinstall_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


