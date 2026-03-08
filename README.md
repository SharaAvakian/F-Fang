# FFAng – Modern Norse-Inspired POD Clothing Store

![FFAng Logo](./logo.png)
*Next-generation print-on-demand clothing & lifestyle store with Norse + cyberpunk + nature documentary design aesthetics.*

---

## Overview

**FFAng** is a modern, immersive e-commerce platform blending:

- **Norse mythology motifs**
- **Minimalist modern design (Apple-inspired)**
- **Cyberpunk neon accents**
- **Nature documentary visuals**

It is a **print-on-demand (POD) clothing and lifestyle store** featuring immersive videos, cinematic storytelling, and a full range of apparel.

The platform is built with **Django backend**, **React frontend**, and **Bootstrap + custom CSS** for styling, running fully on **AWS Free Tier** using **Docker**.

---

## Features

### Frontend

- **React.js** – dynamic, reactive UI components
- **Bootstrap 5** – responsive layout, prebuilt components, grid system
- **Custom CSS** – Norse + cyberpunk + natural aesthetics
- Full-screen **hero video sections** on homepage and product pages
- **Interactive product pages** with images, videos, and storytelling
- Fully **reactive cart & checkout** system
- **Responsive design** for desktop, tablet, and mobile
- Dark/Light mode toggle
- Optimized for **performance & accessibility (A11y)**
- Animations using **React Spring / Framer Motion**
- Reusable components: Buttons, Cards, Modals, Product Grid, Video Hero

### Backend

- **Django 6.x** with **Django REST Framework (DRF)**
- Database support: **PostgreSQL / SQLite**
- **User management:** login, registration, password recovery, roles
- **Session management:** database-backed sessions for secure login
- **Order management:** carts, order history, POD integration
- **Admin interface:** manage products, orders, payments, media
- JWT / Token-based authentication for API access
- Email integration for order confirmations & notifications
- Middleware for security, logging, and rate-limiting
- API endpoints structured for frontend consumption:
  - `/api/products/` – list all products
  - `/api/products/<id>/` – retrieve product detail
  - `/api/cart/` – manage user cart
  - `/api/orders/` – create & view orders
  - `/api/users/` – user registration & management
  - `/api/auth/token/` – obtain authentication token

### Print-On-Demand (POD)

- Integration with **global POD providers** (China, US, EU)
- Automatic order creation via API
- Provider selection based on location, speed, and cost
- Multi-currency pricing and automatic conversion
- Real-time order tracking & shipping updates
- Dynamic inventory synchronization with POD suppliers
- Configurable product mockups for frontend display
- Automated error handling & fallback provider selection

### Payments

- **Visa & Mastercard** support (Armenia & global)
- **ArCa (Armenian card network)** support
- Stripe, PayPal, Alipay (optional)
- Secure checkout with HTTPS, CSRF protection, tokenized payments
- Saved payment methods & billing addresses
- Refund & cancellation APIs integrated
- PCI-DSS compliance for payment handling

### Deployment & Infrastructure

- **AWS EC2 Free Tier (Ubuntu 22.04 LTS)**
- **Dockerized environment:**
  - Django backend container
  - React frontend container
  - Nginx reverse proxy + SSL termination
  - PostgreSQL / SQLite database container
- **Docker Compose** setup with environment variables for secure credentials
- **CI/CD pipeline** via GitHub Actions / GitLab CI:
  - Linting & testing
  - Build Docker images
  - Auto-deploy to EC2
- Automatic SSL via Let's Encrypt
- Environment variable support for production & development
- Logging & monitoring with ELK stack / CloudWatch

### Thematic Design

- Modern minimalist layout (Apple-inspired)
- Cyberpunk neon accent elements
- Nature documentary videos for storytelling
- Norse rune-inspired icons and UI motifs
- Dark/light mode toggle
- Parallax scrolling effects on landing pages
- Cinematic product display using embedded video backgrounds
- Visual storytelling to enhance brand identity

### Product Catalog

- Clothing: shirts, hoodies, jackets, accessories
- Lifestyle items: mugs, backpacks, home goods (POD-supported)
- Categories by style, theme, season, bestsellers
- React-driven search & filtering
- Product recommendations based on user behavior
- Wishlist and favorites system
- Future: dynamic bundles, gift sets, limited collections
- Variant support: sizes, colors, designs
- Stock management integrated with POD API

---

## Development Setup

### Backend Setup
cd /home/shara/Desktop/F-Fang/F-Fang
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver  # Runs on http://localhost:8000

### Frontend Setup
cd frontend
npm install
npm run dev  # Runs on http://localhost:5173 (or next available port)

### Docker
docker-compose up --build

Admin: admin/admin123 at http://localhost:8000/admin/

Frontend: http://localhost:5173/ (Vite dev server)

Nginx proxies requests to both containers in production.

---

## Technologies Used

Frontend: React, Bootstrap 5, custom CSS, React Router, Axios

Backend: Django 6.x, Django REST Framework, PostgreSQL/SQLite

Deployment: Docker, Nginx, AWS EC2 Free Tier, GitHub Actions CI/CD

Payments: Stripe, PayPal, ArCa, Visa, Mastercard

POD Integration: Multiple international providers

Version Control: Git & GitHub

Video & Multimedia: HTML5 video, React video components

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

FFAng – Modern Norse-Inspired POD Clothing Store