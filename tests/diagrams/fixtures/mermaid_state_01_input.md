# Test: Order Lifecycle State Machine

Create a Mermaid state diagram for an e-commerce order:

States:
- Created: Initial state when order is placed
- Pending Payment: Waiting for payment confirmation
- Confirmed: Payment received, ready for fulfillment
- Shipped: Order dispatched to customer
- Delivered: Order received by customer
- Cancelled: Order cancelled (can happen from Created or Pending Payment)
- Error: Payment failed (can retry or cancel)

Requirements:
- Show start and end states
- Include error state with recovery path
- Show cancellation paths
