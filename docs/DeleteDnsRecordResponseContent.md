# DeleteDnsRecordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DnsRecordMutationData**](DnsRecordMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_dns_record_response_content import DeleteDnsRecordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDnsRecordResponseContent from a JSON string
delete_dns_record_response_content_instance = DeleteDnsRecordResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeleteDnsRecordResponseContent.to_json())

# convert the object into a dict
delete_dns_record_response_content_dict = delete_dns_record_response_content_instance.to_dict()
# create an instance of DeleteDnsRecordResponseContent from a dict
delete_dns_record_response_content_from_dict = DeleteDnsRecordResponseContent.from_dict(delete_dns_record_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


