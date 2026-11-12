# DnsZoneMutationData

Result of create-dns-zone or delete-dns-zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**zone_id** | **str** | DNS zone identifier when returned by upstream | [optional] 
**domain_id** | **str** | Domain service id when returned by upstream | [optional] 
**domain_name** | **str** | Zone domain name (FQDN) when returned by upstream | [optional] 
**backend** | [**DnsBackend**](DnsBackend.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.dns_zone_mutation_data import DnsZoneMutationData

# TODO update the JSON string below
json = "{}"
# create an instance of DnsZoneMutationData from a JSON string
dns_zone_mutation_data_instance = DnsZoneMutationData.from_json(json)
# print the JSON string representation of the object
print(DnsZoneMutationData.to_json())

# convert the object into a dict
dns_zone_mutation_data_dict = dns_zone_mutation_data_instance.to_dict()
# create an instance of DnsZoneMutationData from a dict
dns_zone_mutation_data_from_dict = DnsZoneMutationData.from_dict(dns_zone_mutation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


