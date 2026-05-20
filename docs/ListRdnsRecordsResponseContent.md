# ListRdnsRecordsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListRdnsResponseData**](ListRdnsResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_rdns_records_response_content import ListRdnsRecordsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListRdnsRecordsResponseContent from a JSON string
list_rdns_records_response_content_instance = ListRdnsRecordsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListRdnsRecordsResponseContent.to_json())

# convert the object into a dict
list_rdns_records_response_content_dict = list_rdns_records_response_content_instance.to_dict()
# create an instance of ListRdnsRecordsResponseContent from a dict
list_rdns_records_response_content_from_dict = ListRdnsRecordsResponseContent.from_dict(list_rdns_records_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


