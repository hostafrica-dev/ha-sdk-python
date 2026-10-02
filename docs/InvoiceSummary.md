# InvoiceSummary

Summary of an invoice in the list-invoices response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique invoice identifier - must be sent as a string | 
**invoice_number** | **str** | Human-readable invoice number when assigned | 
**var_date** | **str** | Invoice issue date (ISO 8601) | 
**due_date** | **str** | Invoice due date (ISO 8601) | 
**status** | **str** | Invoice status (e.g. Paid, Unpaid, Cancelled, Refunded) | 
**tax** | **str** | Primary tax amount as a decimal string | 
**tax2** | **str** | Secondary tax amount as a decimal string. Omitted when a second tax is not configured. | [optional] 
**tax_rate** | **str** | Primary tax rate as a decimal string | 
**tax_rate2** | **str** | Secondary tax rate as a decimal string. Omitted when a second tax is not configured. | [optional] 
**total** | **str** | Invoice total including tax as a decimal string | 
**subtotal** | **str** | Invoice subtotal excluding tax as a decimal string | 
**grand_total** | **str** | Grand total as a decimal string | 

## Example

```python
from ha_sdk_python.models.invoice_summary import InvoiceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSummary from a JSON string
invoice_summary_instance = InvoiceSummary.from_json(json)
# print the JSON string representation of the object
print(InvoiceSummary.to_json())

# convert the object into a dict
invoice_summary_dict = invoice_summary_instance.to_dict()
# create an instance of InvoiceSummary from a dict
invoice_summary_from_dict = InvoiceSummary.from_dict(invoice_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


