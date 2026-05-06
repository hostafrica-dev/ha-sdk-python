# SuspendVpsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**suspend_reason** | **str** | Reason for suspending the service | 

## Example

```python
from hostafrica_sdk_python.models.suspend_vps_request_content import SuspendVpsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of SuspendVpsRequestContent from a JSON string
suspend_vps_request_content_instance = SuspendVpsRequestContent.from_json(json)
# print the JSON string representation of the object
print(SuspendVpsRequestContent.to_json())

# convert the object into a dict
suspend_vps_request_content_dict = suspend_vps_request_content_instance.to_dict()
# create an instance of SuspendVpsRequestContent from a dict
suspend_vps_request_content_from_dict = SuspendVpsRequestContent.from_dict(suspend_vps_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


