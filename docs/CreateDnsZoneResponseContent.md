# CreateDnsZoneResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DnsZoneMutationData**](DnsZoneMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.create_dns_zone_response_content import CreateDnsZoneResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDnsZoneResponseContent from a JSON string
create_dns_zone_response_content_instance = CreateDnsZoneResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateDnsZoneResponseContent.to_json())

# convert the object into a dict
create_dns_zone_response_content_dict = create_dns_zone_response_content_instance.to_dict()
# create an instance of CreateDnsZoneResponseContent from a dict
create_dns_zone_response_content_from_dict = CreateDnsZoneResponseContent.from_dict(create_dns_zone_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


