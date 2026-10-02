# InvoiceTransaction

A payment or refund transaction recorded against an invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction identifier | 
**gateway** | **str** | Payment gateway identifier | [optional] 
**var_date** | **str** | Transaction date (ISO 8601 or upstream date string) | [optional] 
**description** | **str** | Transaction description | [optional] 
**amount_in** | **str** | Amount received as a decimal string | [optional] 
**fees** | **str** | Gateway fees as a decimal string | [optional] 
**amount_out** | **str** | Amount paid out (e.g. refund) as a decimal string | [optional] 
**trans_id** | **str** | Gateway transaction reference | [optional] 

## Example

```python
from ha_sdk_python.models.invoice_transaction import InvoiceTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTransaction from a JSON string
invoice_transaction_instance = InvoiceTransaction.from_json(json)
# print the JSON string representation of the object
print(InvoiceTransaction.to_json())

# convert the object into a dict
invoice_transaction_dict = invoice_transaction_instance.to_dict()
# create an instance of InvoiceTransaction from a dict
invoice_transaction_from_dict = InvoiceTransaction.from_dict(invoice_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


