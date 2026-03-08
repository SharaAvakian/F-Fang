import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
      <div className="container-fluid">
        <Link className="navbar-brand fw-bold" to="/">🛡️ FFAng</Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <div className="navbar-nav ms-auto">
            <Link className="nav-link" to="/">Home</Link>
            <Link className="nav-link" to="/products">Products</Link>
            <Link className="nav-link" to="/cart">
              <i className="fas fa-shopping-cart"></i> Cart
            </Link>
            <Link className="nav-link" to="/login">Login</Link>
            <Link className="nav-link" to="/register">Register</Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;