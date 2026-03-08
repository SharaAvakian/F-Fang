import React, { useEffect, useState } from 'react';
import { getProducts } from '../api';

const Products = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await getProducts();
        setProducts(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to load products. Please try again.');
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  const addToCart = (product) => {
    // TODO: Implement cart functionality
    alert(`${product.name} added to cart!`);
  };

  if (loading) {
    return (
      <div className="container py-5">
        <div className="text-center">
          <div className="spinner-border text-primary" role="status" style={{width: '3rem', height: '3rem'}}>
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3">Loading amazing products...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container py-5">
        <div className="alert alert-danger text-center" role="alert">
          <i className="fas fa-exclamation-triangle fa-2x mb-3"></i>
          <h4 className="alert-heading">Oops!</h4>
          <p>{error}</p>
          <button className="btn btn-primary" onClick={() => window.location.reload()}>
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="container py-5">
      {/* Header */}
      <div className="row mb-5">
        <div className="col-12 text-center">
          <h1 className="display-4 fw-bold mb-3">
            <i className="fas fa-tshirt text-primary me-3"></i>
            Our Collection
          </h1>
          <p className="lead text-muted">
            Discover unique Norse-inspired apparel and accessories
          </p>
        </div>
      </div>

      {/* Products Grid */}
      {products.length === 0 ? (
        <div className="text-center py-5">
          <i className="fas fa-box-open fa-4x text-muted mb-4"></i>
          <h3 className="text-muted">No products available</h3>
          <p className="text-muted">Check back soon for new arrivals!</p>
        </div>
      ) : (
        <div className="row g-4">
          {products.map(product => (
            <div key={product.id} className="col-lg-4 col-md-6">
              <div className="card h-100 border-0 shadow-sm product-card">
                {/* Product Image Placeholder */}
                <div className="card-img-top bg-light d-flex align-items-center justify-content-center" style={{height: '250px'}}>
                  <i className="fas fa-image fa-3x text-muted"></i>
                </div>

                <div className="card-body d-flex flex-column">
                  <h5 className="card-title fw-bold">{product.name}</h5>
                  <p className="card-text text-muted flex-grow-1">{product.description}</p>

                  <div className="d-flex justify-content-between align-items-center mb-3">
                    <span className="h4 text-primary fw-bold mb-0">${product.price}</span>
                    <small className="text-muted">Stock: {product.stock}</small>
                  </div>

                  <button
                    className="btn btn-primary w-100"
                    onClick={() => addToCart(product)}
                    disabled={product.stock === 0}
                  >
                    <i className="fas fa-cart-plus me-2"></i>
                    {product.stock > 0 ? 'Add to Cart' : 'Out of Stock'}
                  </button>
                </div>

                <div className="card-footer bg-transparent border-0">
                  <small className="text-muted">
                    <i className="fas fa-tag me-1"></i>
                    Category: {product.category?.name || 'General'}
                  </small>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Call to Action */}
      <div className="text-center mt-5">
        <div className="bg-light rounded p-4">
          <h3 className="mb-3">Love what you see?</h3>
          <p className="text-muted mb-4">Create an account to save favorites and track orders</p>
          <div className="d-flex justify-content-center gap-3">
            <a href="/register" className="btn btn-primary">
              <i className="fas fa-user-plus me-2"></i>Sign Up
            </a>
            <a href="/login" className="btn btn-outline-primary">
              <i className="fas fa-sign-in-alt me-2"></i>Login
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Products;