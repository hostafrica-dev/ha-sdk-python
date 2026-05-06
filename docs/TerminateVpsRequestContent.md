# TerminateVpsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.terminate_vps_request_content import TerminateVpsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateVpsRequestContent from a JSON string
terminate_vps_request_content_instance = TerminateVpsRequestContent.from_json(json)
# print the JSON string representation of the object
print(TerminateVpsRequestContent.to_json())

# convert the object into a dict
terminate_vps_request_content_dict = terminate_vps_request_content_instance.to_dict()
# create an instance of TerminateVpsRequestContent from a dict
terminate_vps_request_content_from_dict = TerminateVpsRequestContent.from_dict(terminate_vps_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


