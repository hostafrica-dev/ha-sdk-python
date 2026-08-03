# EditDnsRecordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DnsRecordMutationData**](DnsRecordMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.edit_dns_record_response_content import EditDnsRecordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of EditDnsRecordResponseContent from a JSON string
edit_dns_record_response_content_instance = EditDnsRecordResponseContent.from_json(json)
# print the JSON string representation of the object
print(EditDnsRecordResponseContent.to_json())

# convert the object into a dict
edit_dns_record_response_content_dict = edit_dns_record_response_content_instance.to_dict()
# create an instance of EditDnsRecordResponseContent from a dict
edit_dns_record_response_content_from_dict = EditDnsRecordResponseContent.from_dict(edit_dns_record_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


