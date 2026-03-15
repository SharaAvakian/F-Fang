"""
POD (Print-on-Demand) integration layer.

Currently a stub that logs orders. To integrate a real provider:
- Printful: https://developers.printful.com/
- Printify: https://printify.com/app/api-documentation
- SPOD: https://www.spod.com/api/

Each provider needs:
1. API key stored in environment variables
2. Product variant mapping (your variant ID -> provider's variant ID)
3. Webhook endpoint to receive status updates
"""

import logging

logger = logging.getLogger(__name__)


def dispatch_order_to_pod(order):
    """
    Send a confirmed order to the POD provider.
    Returns True on success, False on failure.
    """
    try:
        logger.info(f"[POD] Dispatching Order #{order.id} to provider: {order.pod_provider or 'default'}")

        # Build the line items
        line_items = []
        for item in order.items.all():
            line_items.append({
                'product_name': item.product_name,
                'sku': item.product_sku,
                'quantity': item.quantity,
                'size': item.size,
                'color': item.color,
                'pod_variant_id': item.variant.pod_variant_id if item.variant else '',
            })

        payload = {
            'order_id': str(order.id),
            'recipient': {
                'name': order.shipping_name,
                'email': order.shipping_email,
                'phone': order.shipping_phone,
                'address': order.shipping_address,
                'city': order.shipping_city,
                'country_code': order.shipping_country,
                'zip': order.shipping_zip,
            },
            'items': line_items,
        }

        logger.info(f"[POD] Payload: {payload}")

        # ---- REAL INTEGRATION EXAMPLE (Printful) ----
        # import requests
        # response = requests.post(
        #     'https://api.printful.com/orders',
        #     json={'recipient': payload['recipient'], 'items': payload['items']},
        #     headers={'Authorization': f'Bearer {settings.PRINTFUL_API_KEY}'}
        # )
        # data = response.json()
        # order.pod_order_id = data['result']['id']
        # order.pod_provider = 'printful'
        # order.status = 'sent_to_pod'
        # order.save()
        # ---------------------------------------------

        # For now, mark as sent
        order.status = 'processing'
        order.pod_provider = 'stub'
        order.pod_order_id = f'STUB-{order.id}'
        order.save()

        logger.info(f"[POD] Order #{order.id} successfully dispatched.")
        return True

    except Exception as e:
        logger.error(f"[POD] Failed to dispatch Order #{order.id}: {e}")
        return False


def get_pod_order_status(pod_order_id, provider='printful'):
    """
    Poll the POD provider for order/tracking status.
    Call this from a management command or webhook handler.
    """
    logger.info(f"[POD] Checking status for {provider} order {pod_order_id}")
    # Stub: return None — implement with real API call
    return None
