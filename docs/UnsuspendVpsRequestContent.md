# UnsuspendVpsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.unsuspend_vps_request_content import UnsuspendVpsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UnsuspendVpsRequestContent from a JSON string
unsuspend_vps_request_content_instance = UnsuspendVpsRequestContent.from_json(json)
# print the JSON string representation of the object
print(UnsuspendVpsRequestContent.to_json())

# convert the object into a dict
unsuspend_vps_request_content_dict = unsuspend_vps_request_content_instance.to_dict()
# create an instance of UnsuspendVpsRequestContent from a dict
unsuspend_vps_request_content_from_dict = UnsuspendVpsRequestContent.from_dict(unsuspend_vps_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


