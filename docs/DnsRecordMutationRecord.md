# DnsRecordMutationRecord

DNS record fields for add, edit, or delete via DNSManager.  See `DnsRecordInfo` for how `content` and structured fields map to upstream record data. Delete requires only `id`, `name`, and `type`. For edit and delete, `id` must be the numeric zone line from get-dns-zone-details (a positive integer string).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Record line from get-dns-zone-details (positive integer string); required for edit and delete | [optional] 
**name** | **str** | Record host/name (e.g. @, www, mail); required for add | [optional] 
**type** | **str** | Record type (e.g. A, AAAA, CNAME, MX, TXT, NS, SRV); required for add | [optional] 
**content** | **str** | Primary record value; required for add and edit. Meaning depends on type — see DnsRecordInfo | [optional] 
**ttl** | **int** | Time-to-live in seconds; defaults to 3600 on add when omitted | [optional] 
**priority** | **int** | MX preference when type is MX; SRV priority when type is SRV | [optional] 
**weight** | **int** | SRV weight when type is SRV | [optional] 
**port** | **int** | SRV port when type is SRV; required for add and edit when type is SRV | [optional] 

## Example

```python
from ha_sdk_python.models.dns_record_mutation_record import DnsRecordMutationRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordMutationRecord from a JSON string
dns_record_mutation_record_instance = DnsRecordMutationRecord.from_json(json)
# print the JSON string representation of the object
print(DnsRecordMutationRecord.to_json())

# convert the object into a dict
dns_record_mutation_record_dict = dns_record_mutation_record_instance.to_dict()
# create an instance of DnsRecordMutationRecord from a dict
dns_record_mutation_record_from_dict = DnsRecordMutationRecord.from_dict(dns_record_mutation_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


