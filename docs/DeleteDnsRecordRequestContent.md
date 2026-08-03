# DeleteDnsRecordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | DNS zone domain name (FQDN); optional when zone_id is provided | [optional] 
**zone_id** | **str** | DNS zone identifier from list-dns-zones or get-dns-zone-details | 
**record** | [**DnsRecordMutationRecord**](DnsRecordMutationRecord.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_dns_record_request_content import DeleteDnsRecordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDnsRecordRequestContent from a JSON string
delete_dns_record_request_content_instance = DeleteDnsRecordRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteDnsRecordRequestContent.to_json())

# convert the object into a dict
delete_dns_record_request_content_dict = delete_dns_record_request_content_instance.to_dict()
# create an instance of DeleteDnsRecordRequestContent from a dict
delete_dns_record_request_content_from_dict = DeleteDnsRecordRequestContent.from_dict(delete_dns_record_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


