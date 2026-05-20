# RebootVpsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.reboot_vps_request_content import RebootVpsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of RebootVpsRequestContent from a JSON string
reboot_vps_request_content_instance = RebootVpsRequestContent.from_json(json)
# print the JSON string representation of the object
print(RebootVpsRequestContent.to_json())

# convert the object into a dict
reboot_vps_request_content_dict = reboot_vps_request_content_instance.to_dict()
# create an instance of RebootVpsRequestContent from a dict
reboot_vps_request_content_from_dict = RebootVpsRequestContent.from_dict(reboot_vps_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


