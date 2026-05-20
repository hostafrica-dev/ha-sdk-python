# GetVpsDetailsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.get_vps_details_request_content import GetVpsDetailsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpsDetailsRequestContent from a JSON string
get_vps_details_request_content_instance = GetVpsDetailsRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetVpsDetailsRequestContent.to_json())

# convert the object into a dict
get_vps_details_request_content_dict = get_vps_details_request_content_instance.to_dict()
# create an instance of GetVpsDetailsRequestContent from a dict
get_vps_details_request_content_from_dict = GetVpsDetailsRequestContent.from_dict(get_vps_details_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


