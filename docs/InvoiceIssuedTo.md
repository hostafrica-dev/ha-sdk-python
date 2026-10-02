# InvoiceIssuedTo

Recipient / billed-to details on an invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Company name on the invoice | 
**full_name** | **str** | Full name of the billed contact | 
**address** | **str** | Street address | 
**city_state_zip** | **str** | City, state/province, and postal code | 
**country** | **str** | ISO country code | 
**country_name** | **str** | Country display name | 
**tax** | [**InvoiceIssuedToTax**](InvoiceIssuedToTax.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.invoice_issued_to import InvoiceIssuedTo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceIssuedTo from a JSON string
invoice_issued_to_instance = InvoiceIssuedTo.from_json(json)
# print the JSON string representation of the object
print(InvoiceIssuedTo.to_json())

# convert the object into a dict
invoice_issued_to_dict = invoice_issued_to_instance.to_dict()
# create an instance of InvoiceIssuedTo from a dict
invoice_issued_to_from_dict = InvoiceIssuedTo.from_dict(invoice_issued_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


