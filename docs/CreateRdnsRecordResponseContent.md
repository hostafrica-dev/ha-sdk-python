# CreateRdnsRecordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**CreateRdnsRecordResponseData**](CreateRdnsRecordResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_rdns_record_response_content import CreateRdnsRecordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRdnsRecordResponseContent from a JSON string
create_rdns_record_response_content_instance = CreateRdnsRecordResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateRdnsRecordResponseContent.to_json())

# convert the object into a dict
create_rdns_record_response_content_dict = create_rdns_record_response_content_instance.to_dict()
# create an instance of CreateRdnsRecordResponseContent from a dict
create_rdns_record_response_content_from_dict = CreateRdnsRecordResponseContent.from_dict(create_rdns_record_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


