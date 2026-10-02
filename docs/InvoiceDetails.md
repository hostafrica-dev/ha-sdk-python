# InvoiceDetails

Full invoice details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique invoice identifier - must be sent as a string | 
**invoice_number** | **str** | Human-readable invoice number when assigned | 
**issued_to** | [**InvoiceIssuedTo**](InvoiceIssuedTo.md) |  | 
**var_date** | **str** | Invoice issue date (ISO 8601) | 
**due_date** | **str** | Invoice due date (ISO 8601) | 
**date_paid** | **str** | Date the invoice was paid (ISO 8601), if paid | [optional] 
**subtotal** | **str** | Invoice subtotal excluding tax as a decimal string | 
**credit** | **str** | Credit applied as a decimal string | 
**tax** | **str** | Primary tax amount as a decimal string | 
**tax2** | **str** | Secondary tax amount as a decimal string. Omitted when a second tax is not configured. | [optional] 
**total** | **str** | Invoice total including tax as a decimal string | 
**tax_rate** | **str** | Primary tax rate as a decimal string | 
**tax_rate2** | **str** | Secondary tax rate as a decimal string. Omitted when a second tax is not configured. | [optional] 
**status** | **str** | Invoice status (e.g. Paid, Unpaid, Cancelled, Refunded) | 
**payment_method** | **str** | Payment method identifier | 
**total_due** | **str** | Amount still due as a decimal string | 
**notes** | **str** | Invoice notes | 
**items** | [**List[InvoiceItem]**](InvoiceItem.md) | Invoice line items | 
**transactions** | [**List[InvoiceTransaction]**](InvoiceTransaction.md) | Payment and refund transactions on the invoice | 

## Example

```python
from ha_sdk_python.models.invoice_details import InvoiceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetails from a JSON string
invoice_details_instance = InvoiceDetails.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetails.to_json())

# convert the object into a dict
invoice_details_dict = invoice_details_instance.to_dict()
# create an instance of InvoiceDetails from a dict
invoice_details_from_dict = InvoiceDetails.from_dict(invoice_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


