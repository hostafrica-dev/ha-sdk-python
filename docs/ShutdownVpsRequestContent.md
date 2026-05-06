# ShutdownVpsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.shutdown_vps_request_content import ShutdownVpsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ShutdownVpsRequestContent from a JSON string
shutdown_vps_request_content_instance = ShutdownVpsRequestContent.from_json(json)
# print the JSON string representation of the object
print(ShutdownVpsRequestContent.to_json())

# convert the object into a dict
shutdown_vps_request_content_dict = shutdown_vps_request_content_instance.to_dict()
# create an instance of ShutdownVpsRequestContent from a dict
shutdown_vps_request_content_from_dict = ShutdownVpsRequestContent.from_dict(shutdown_vps_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


