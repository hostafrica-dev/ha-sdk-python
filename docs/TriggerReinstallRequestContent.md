# TriggerReinstallRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**template** | **str** | Template identifier for the OS to reinstall | 

## Example

```python
from ha_sdk_python.models.trigger_reinstall_request_content import TriggerReinstallRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerReinstallRequestContent from a JSON string
trigger_reinstall_request_content_instance = TriggerReinstallRequestContent.from_json(json)
# print the JSON string representation of the object
print(TriggerReinstallRequestContent.to_json())

# convert the object into a dict
trigger_reinstall_request_content_dict = trigger_reinstall_request_content_instance.to_dict()
# create an instance of TriggerReinstallRequestContent from a dict
trigger_reinstall_request_content_from_dict = TriggerReinstallRequestContent.from_dict(trigger_reinstall_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


