# InvoiceItem

A single invoice line item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line item identifier | 
**type** | **str** | Line item type (e.g. Hosting) | 
**description** | **str** | Line item description | 
**amount** | **str** | Line item amount as a decimal string | 
**taxed** | **int** | Whether the line item is taxed (1 &#x3D; taxed, 0 &#x3D; not taxed) | 

## Example

```python
from ha_sdk_python.models.invoice_item import InvoiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItem from a JSON string
invoice_item_instance = InvoiceItem.from_json(json)
# print the JSON string representation of the object
print(InvoiceItem.to_json())

# convert the object into a dict
invoice_item_dict = invoice_item_instance.to_dict()
# create an instance of InvoiceItem from a dict
invoice_item_from_dict = InvoiceItem.from_dict(invoice_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


