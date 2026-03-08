import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
      {/* Hero Section */}
      <section className="hero-section bg-gradient-primary text-white py-5">
        <div className="container">
          <div className="row align-items-center">
            <div className="col-lg-6">
              <h1 className="display-4 fw-bold mb-4">
                🛡️ Norse-Inspired Fashion
              </h1>
              <p className="lead mb-4">
                Discover unique apparel blending Norse mythology, cyberpunk aesthetics,
                and nature documentary storytelling. Print-on-demand quality with global shipping.
              </p>
              <div className="d-flex gap-3">
                <Link className="btn btn-light btn-lg px-4" to="/products">
                  <i className="fas fa-shopping-bag me-2"></i>Shop Now
                </Link>
                <Link className="btn btn-outline-light btn-lg px-4" to="/register">
                  Join Community
                </Link>
              </div>
            </div>
            <div className="col-lg-6 text-center">
              <div className="hero-image">
                <div className="bg-light rounded-circle d-inline-block p-5 shadow">
                  <i className="fas fa-tshirt fa-5x text-primary"></i>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="features-section py-5 bg-light">
        <div className="container">
          <div className="row text-center mb-5">
            <div className="col-12">
              <h2 className="display-5 fw-bold">Why Choose FFAng?</h2>
              <p className="lead text-muted">Experience fashion that tells a story</p>
            </div>
          </div>
          <div className="row g-4">
            <div className="col-md-4">
              <div className="card h-100 border-0 shadow-sm">
                <div className="card-body text-center p-4">
                  <div className="feature-icon mb-3">
                    <i className="fas fa-dragon fa-3x text-primary"></i>
                  </div>
                  <h5 className="card-title fw-bold">Norse Heritage</h5>
                  <p className="card-text text-muted">
                    Designs inspired by ancient Norse mythology and Viking culture,
                    reimagined for modern fashion.
                  </p>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card h-100 border-0 shadow-sm">
                <div className="card-body text-center p-4">
                  <div className="feature-icon mb-3">
                    <i className="fas fa-robot fa-3x text-success"></i>
                  </div>
                  <h5 className="card-title fw-bold">Cyberpunk Edge</h5>
                  <p className="card-text text-muted">
                    Futuristic neon accents and digital aesthetics meet traditional
                    patterns in unique combinations.
                  </p>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card h-100 border-0 shadow-sm">
                <div className="card-body text-center p-4">
                  <div className="feature-icon mb-3">
                    <i className="fas fa-leaf fa-3x text-info"></i>
                  </div>
                  <h5 className="card-title fw-bold">Nature Inspired</h5>
                  <p className="card-text text-muted">
                    Documentary-style visuals of mountains, forests, and wildlife
                    create an immersive brand experience.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="stats-section py-5 bg-primary text-white">
        <div className="container">
          <div className="row text-center">
            <div className="col-md-3">
              <div className="stat-item">
                <h3 className="display-4 fw-bold mb-2">500+</h3>
                <p className="mb-0">Happy Customers</p>
              </div>
            </div>
            <div className="col-md-3">
              <div className="stat-item">
                <h3 className="display-4 fw-bold mb-2">50+</h3>
                <p className="mb-0">Unique Designs</p>
              </div>
            </div>
            <div className="col-md-3">
              <div className="stat-item">
                <h3 className="display-4 fw-bold mb-2">30+</h3>
                <p className="mb-0">Countries Served</p>
              </div>
            </div>
            <div className="col-md-3">
              <div className="stat-item">
                <h3 className="display-4 fw-bold mb-2">4.8★</h3>
                <p className="mb-0">Average Rating</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="cta-section py-5">
        <div className="container text-center">
          <div className="row justify-content-center">
            <div className="col-lg-8">
              <h2 className="display-5 fw-bold mb-4">Ready to Join the Norse Revolution?</h2>
              <p className="lead mb-4">
                Be part of a community that celebrates mythology, technology, and nature
                through fashion that makes a statement.
              </p>
              <div className="d-flex justify-content-center gap-3">
                <Link className="btn btn-primary btn-lg px-5" to="/register">
                  <i className="fas fa-user-plus me-2"></i>Sign Up Free
                </Link>
                <Link className="btn btn-outline-primary btn-lg px-5" to="/products">
                  <i className="fas fa-eye me-2"></i>Browse Collection
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;