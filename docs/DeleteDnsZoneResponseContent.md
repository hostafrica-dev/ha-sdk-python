# DeleteDnsZoneResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DnsZoneMutationData**](DnsZoneMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_dns_zone_response_content import DeleteDnsZoneResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDnsZoneResponseContent from a JSON string
delete_dns_zone_response_content_instance = DeleteDnsZoneResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeleteDnsZoneResponseContent.to_json())

# convert the object into a dict
delete_dns_zone_response_content_dict = delete_dns_zone_response_content_instance.to_dict()
# create an instance of DeleteDnsZoneResponseContent from a dict
delete_dns_zone_response_content_from_dict = DeleteDnsZoneResponseContent.from_dict(delete_dns_zone_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


