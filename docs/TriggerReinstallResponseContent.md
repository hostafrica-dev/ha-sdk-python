# TriggerReinstallResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**TriggerReinstallResponseData**](TriggerReinstallResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.trigger_reinstall_response_content import TriggerReinstallResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerReinstallResponseContent from a JSON string
trigger_reinstall_response_content_instance = TriggerReinstallResponseContent.from_json(json)
# print the JSON string representation of the object
print(TriggerReinstallResponseContent.to_json())

# convert the object into a dict
trigger_reinstall_response_content_dict = trigger_reinstall_response_content_instance.to_dict()
# create an instance of TriggerReinstallResponseContent from a dict
trigger_reinstall_response_content_from_dict = TriggerReinstallResponseContent.from_dict(trigger_reinstall_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


