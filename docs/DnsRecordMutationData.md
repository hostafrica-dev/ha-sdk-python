# DnsRecordMutationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**records** | [**List[DnsRecordInfo]**](DnsRecordInfo.md) | Updated DNS records when returned by upstream | [optional] 

## Example

```python
from ha_sdk_python.models.dns_record_mutation_data import DnsRecordMutationData

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordMutationData from a JSON string
dns_record_mutation_data_instance = DnsRecordMutationData.from_json(json)
# print the JSON string representation of the object
print(DnsRecordMutationData.to_json())

# convert the object into a dict
dns_record_mutation_data_dict = dns_record_mutation_data_instance.to_dict()
# create an instance of DnsRecordMutationData from a dict
dns_record_mutation_data_from_dict = DnsRecordMutationData.from_dict(dns_record_mutation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


