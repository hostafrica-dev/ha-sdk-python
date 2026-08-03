# ListDnssecRecordsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**records** | [**List[DnssecRecordInfo]**](DnssecRecordInfo.md) | DNSSEC DS records configured for the domain | 

## Example

```python
from ha_sdk_python.models.list_dnssec_records_data import ListDnssecRecordsData

# TODO update the JSON string below
json = "{}"
# create an instance of ListDnssecRecordsData from a JSON string
list_dnssec_records_data_instance = ListDnssecRecordsData.from_json(json)
# print the JSON string representation of the object
print(ListDnssecRecordsData.to_json())

# convert the object into a dict
list_dnssec_records_data_dict = list_dnssec_records_data_instance.to_dict()
# create an instance of ListDnssecRecordsData from a dict
list_dnssec_records_data_from_dict = ListDnssecRecordsData.from_dict(list_dnssec_records_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


