import React from 'react';

const Cart = () => {
  return (
    <div>
      <h1>Shopping Cart</h1>
      <p>Your cart is empty. <a href="/products">Browse products</a> to add items.</p>
      <div className="alert alert-info">
        Cart functionality will be implemented here.
      </div>
    </div>
  );
};

export default Cart;