# TriggerReinstallResponseData

Response data for trigger reinstall operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**task_id** | **int** | Task ID for the reinstall process | 

## Example

```python
from ha_sdk_python.models.trigger_reinstall_response_data import TriggerReinstallResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerReinstallResponseData from a JSON string
trigger_reinstall_response_data_instance = TriggerReinstallResponseData.from_json(json)
# print the JSON string representation of the object
print(TriggerReinstallResponseData.to_json())

# convert the object into a dict
trigger_reinstall_response_data_dict = trigger_reinstall_response_data_instance.to_dict()
# create an instance of TriggerReinstallResponseData from a dict
trigger_reinstall_response_data_from_dict = TriggerReinstallResponseData.from_dict(trigger_reinstall_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


