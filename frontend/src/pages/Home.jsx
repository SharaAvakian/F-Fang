import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="text-center">
      <div className="bg-primary text-white rounded p-5 mb-4">
        <h1 className="display-4">Welcome to FFAng</h1>
        <p className="lead">Norse-inspired POD clothing store with modern design.</p>
        <hr className="my-4" />
        <p>Explore our collection of unique apparel and lifestyle items.</p>
        <Link className="btn btn-light btn-lg" to="/products">Browse Products</Link>
      </div>
      <div className="row">
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Authentic Designs</h5>
              <p className="card-text">Inspired by Norse mythology and nature.</p>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Print-on-Demand</h5>
              <p className="card-text">High-quality, sustainable production.</p>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Global Shipping</h5>
              <p className="card-text">Fast delivery worldwide.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;