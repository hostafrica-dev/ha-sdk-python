# ListInvoicesResponseData

Top-level data payload for the ListInvoices response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoices** | [**List[InvoiceSummary]**](InvoiceSummary.md) | List of invoices for the authenticated user | 
**total_count** | **int** | Total number of invoices returned | 

## Example

```python
from ha_sdk_python.models.list_invoices_response_data import ListInvoicesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoicesResponseData from a JSON string
list_invoices_response_data_instance = ListInvoicesResponseData.from_json(json)
# print the JSON string representation of the object
print(ListInvoicesResponseData.to_json())

# convert the object into a dict
list_invoices_response_data_dict = list_invoices_response_data_instance.to_dict()
# create an instance of ListInvoicesResponseData from a dict
list_invoices_response_data_from_dict = ListInvoicesResponseData.from_dict(list_invoices_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


