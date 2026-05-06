# StopVpsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.stop_vps_request_content import StopVpsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of StopVpsRequestContent from a JSON string
stop_vps_request_content_instance = StopVpsRequestContent.from_json(json)
# print the JSON string representation of the object
print(StopVpsRequestContent.to_json())

# convert the object into a dict
stop_vps_request_content_dict = stop_vps_request_content_instance.to_dict()
# create an instance of StopVpsRequestContent from a dict
stop_vps_request_content_from_dict = StopVpsRequestContent.from_dict(stop_vps_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


