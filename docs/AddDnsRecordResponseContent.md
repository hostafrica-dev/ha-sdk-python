# AddDnsRecordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DnsRecordMutationData**](DnsRecordMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.add_dns_record_response_content import AddDnsRecordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of AddDnsRecordResponseContent from a JSON string
add_dns_record_response_content_instance = AddDnsRecordResponseContent.from_json(json)
# print the JSON string representation of the object
print(AddDnsRecordResponseContent.to_json())

# convert the object into a dict
add_dns_record_response_content_dict = add_dns_record_response_content_instance.to_dict()
# create an instance of AddDnsRecordResponseContent from a dict
add_dns_record_response_content_from_dict = AddDnsRecordResponseContent.from_dict(add_dns_record_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


