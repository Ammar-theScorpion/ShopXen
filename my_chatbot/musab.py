import json

# Open and read the JSON file
with open('newData.json', 'r') as file:
    data = json.load(file)

# Extract the tags from the JSON objects
tags = [item['tag'] for item in data]

# Print the extracted tags
print(tags)
"""
'product_warranty', 'product_return', 'product_free_shipping', 'product_discount', 'shipping_options', 'payment', 'payment', 'payment', 'product_features', 'order_status', 'return_policy', 'product_price', 'customer_service', 'product_colors', 'payment_methods', 'shipping_options', 'return_policies', 'product_feedback', 'return_reason', 'product_recommendation', 'product_features', 'product_list', 'product_availability', 'product_price_range', 'product_dimensions_and_weight', 'product_images', 'product_customization_options', 'order_status', 'delivery_date', 'tracking_number', 'shipping_address_change', 'payment_confirmation', 'parcel_arrival', 'order_delay', 'return_initiation', 'product_exchange', 'refund_processing_time', 'sale_product_return_policy', 'discount_code', 'payment_declined', 'split_payment', 'save_payment_information', 'installments', 'submit_another_payment_method', 'foreign_currency_fees', 'account_creation', 'shipping_address_update', 'password_reset', 'email_address_change', 'account_deletion', 'expedited_shipping', 'taxes', 'shipping_carrier', 'signature_confirmation', 'change_delivery_date', 'free_gifts', 'promo_code_stacking', 'black_friday_deals', 'buy_two_get_one_free', 'physical_store_locations', 'track_returns', 'technical_support', 'email_receipts', 'password_reset', 'login_troubleshooting', 'form_filling_troubleshooting', 'zoom_troubleshooting', 'image_loading_troubleshooting'
""" 