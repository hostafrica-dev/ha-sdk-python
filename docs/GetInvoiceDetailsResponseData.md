# GetInvoiceDetailsResponseData

Top-level data payload for the GetInvoiceDetails response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**InvoiceDetails**](InvoiceDetails.md) |  | 
**selcom_metadata** | [**SelcomMetadata**](SelcomMetadata.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.get_invoice_details_response_data import GetInvoiceDetailsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceDetailsResponseData from a JSON string
get_invoice_details_response_data_instance = GetInvoiceDetailsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceDetailsResponseData.to_json())

# convert the object into a dict
get_invoice_details_response_data_dict = get_invoice_details_response_data_instance.to_dict()
# create an instance of GetInvoiceDetailsResponseData from a dict
get_invoice_details_response_data_from_dict = GetInvoiceDetailsResponseData.from_dict(get_invoice_details_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


