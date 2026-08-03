# ListDnssecRecordsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListDnssecRecordsData**](ListDnssecRecordsData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_dnssec_records_response_content import ListDnssecRecordsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListDnssecRecordsResponseContent from a JSON string
list_dnssec_records_response_content_instance = ListDnssecRecordsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListDnssecRecordsResponseContent.to_json())

# convert the object into a dict
list_dnssec_records_response_content_dict = list_dnssec_records_response_content_instance.to_dict()
# create an instance of ListDnssecRecordsResponseContent from a dict
list_dnssec_records_response_content_from_dict = ListDnssecRecordsResponseContent.from_dict(list_dnssec_records_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


