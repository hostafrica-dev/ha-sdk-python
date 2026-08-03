# GetDnsZoneDetailsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.get_dns_zone_details_request_content import GetDnsZoneDetailsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetDnsZoneDetailsRequestContent from a JSON string
get_dns_zone_details_request_content_instance = GetDnsZoneDetailsRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetDnsZoneDetailsRequestContent.to_json())

# convert the object into a dict
get_dns_zone_details_request_content_dict = get_dns_zone_details_request_content_instance.to_dict()
# create an instance of GetDnsZoneDetailsRequestContent from a dict
get_dns_zone_details_request_content_from_dict = GetDnsZoneDetailsRequestContent.from_dict(get_dns_zone_details_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


