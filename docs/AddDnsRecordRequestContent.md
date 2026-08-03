# AddDnsRecordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | DNS zone domain name (FQDN); optional when zone_id is provided | [optional] 
**zone_id** | **str** | DNS zone identifier from list-dns-zones or get-dns-zone-details | 
**record** | [**DnsRecordMutationRecord**](DnsRecordMutationRecord.md) |  | 

## Example

```python
from ha_sdk_python.models.add_dns_record_request_content import AddDnsRecordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of AddDnsRecordRequestContent from a JSON string
add_dns_record_request_content_instance = AddDnsRecordRequestContent.from_json(json)
# print the JSON string representation of the object
print(AddDnsRecordRequestContent.to_json())

# convert the object into a dict
add_dns_record_request_content_dict = add_dns_record_request_content_instance.to_dict()
# create an instance of AddDnsRecordRequestContent from a dict
add_dns_record_request_content_from_dict = AddDnsRecordRequestContent.from_dict(add_dns_record_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


