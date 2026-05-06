# StartVpsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.start_vps_request_content import StartVpsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of StartVpsRequestContent from a JSON string
start_vps_request_content_instance = StartVpsRequestContent.from_json(json)
# print the JSON string representation of the object
print(StartVpsRequestContent.to_json())

# convert the object into a dict
start_vps_request_content_dict = start_vps_request_content_instance.to_dict()
# create an instance of StartVpsRequestContent from a dict
start_vps_request_content_from_dict = StartVpsRequestContent.from_dict(start_vps_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


