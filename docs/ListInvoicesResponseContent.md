# ListInvoicesResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListInvoicesResponseData**](ListInvoicesResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_invoices_response_content import ListInvoicesResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoicesResponseContent from a JSON string
list_invoices_response_content_instance = ListInvoicesResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListInvoicesResponseContent.to_json())

# convert the object into a dict
list_invoices_response_content_dict = list_invoices_response_content_instance.to_dict()
# create an instance of ListInvoicesResponseContent from a dict
list_invoices_response_content_from_dict = ListInvoicesResponseContent.from_dict(list_invoices_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


