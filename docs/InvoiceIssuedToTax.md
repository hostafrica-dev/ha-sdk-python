# InvoiceIssuedToTax

Tax applied to the invoice recipient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tax name or region label (e.g. SA) | 
**rate** | **float** | Tax rate percentage | 
**level** | **int** | Tax level | 

## Example

```python
from ha_sdk_python.models.invoice_issued_to_tax import InvoiceIssuedToTax

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceIssuedToTax from a JSON string
invoice_issued_to_tax_instance = InvoiceIssuedToTax.from_json(json)
# print the JSON string representation of the object
print(InvoiceIssuedToTax.to_json())

# convert the object into a dict
invoice_issued_to_tax_dict = invoice_issued_to_tax_instance.to_dict()
# create an instance of InvoiceIssuedToTax from a dict
invoice_issued_to_tax_from_dict = InvoiceIssuedToTax.from_dict(invoice_issued_to_tax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


