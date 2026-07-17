# ListDomainsRequiringDataResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListDomainsRequiringDataData**](ListDomainsRequiringDataData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_domains_requiring_data_response_content import ListDomainsRequiringDataResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomainsRequiringDataResponseContent from a JSON string
list_domains_requiring_data_response_content_instance = ListDomainsRequiringDataResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListDomainsRequiringDataResponseContent.to_json())

# convert the object into a dict
list_domains_requiring_data_response_content_dict = list_domains_requiring_data_response_content_instance.to_dict()
# create an instance of ListDomainsRequiringDataResponseContent from a dict
list_domains_requiring_data_response_content_from_dict = ListDomainsRequiringDataResponseContent.from_dict(list_domains_requiring_data_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


