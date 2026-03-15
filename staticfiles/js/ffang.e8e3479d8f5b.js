/* ═══════════════════════════════════════════════════════════
   FFAng JS — Cart AJAX + UI helpers
═══════════════════════════════════════════════════════════ */

'use strict';

// ─── CSRF helper ─────────────────────────────────────────────
function getCsrf() {
  return document.querySelector('[name=csrfmiddlewaretoken]')?.value
    || document.cookie.split('; ').find(r => r.startsWith('csrftoken='))?.split('=')[1] || '';
}

// ─── Toast notification ──────────────────────────────────────
function showToast(message, type = 'success') {
  const existing = document.getElementById('ffang-toast');
  if (existing) existing.remove();

  const icons = { success: 'bi-check-circle-fill', error: 'bi-exclamation-circle-fill', info: 'bi-info-circle-fill' };
  const colors = { success: '#2ecc71', error: '#e74c3c', info: '#00d4ff' };

  const toast = document.createElement('div');
  toast.id = 'ffang-toast';
  toast.style.cssText = `
    position: fixed; bottom: 2rem; right: 2rem; z-index: 9999;
    background: var(--bg-elevated, #17171e);
    border: 1px solid var(--border, #2a2a36);
    border-left: 3px solid ${colors[type] || colors.success};
    border-radius: 10px; padding: .85rem 1.25rem;
    display: flex; align-items: center; gap: .75rem;
    box-shadow: 0 8px 32px rgba(0,0,0,.6);
    font-size: .875rem; color: var(--text-primary, #e8e6f0);
    transform: translateY(20px); opacity: 0;
    transition: transform .25s ease, opacity .25s ease;
    max-width: 320px;
  `;
  toast.innerHTML = `<i class="bi ${icons[type] || icons.success}" style="color:${colors[type]};font-size:1rem;"></i><span>${message}</span>`;
  document.body.appendChild(toast);

  requestAnimationFrame(() => {
    toast.style.transform = 'translateY(0)';
    toast.style.opacity = '1';
  });

  setTimeout(() => {
    toast.style.transform = 'translateY(20px)';
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// ─── Update cart badge in navbar ─────────────────────────────
function updateCartBadge(count) {
  document.querySelectorAll('.cart-badge').forEach(badge => {
    if (count > 0) {
      badge.textContent = count;
      badge.style.display = 'flex';
    } else {
      badge.style.display = 'none';
    }
  });
}

// ─── AJAX Add-to-cart ────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {

  // Intercept all add-to-cart forms for AJAX
  document.querySelectorAll('.add-to-cart-form').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('.add-to-cart-btn');
      const original = btn.innerHTML;

      btn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span>';
      btn.disabled = true;

      try {
        const data = new FormData(form);
        const res = await fetch(form.action, {
          method: 'POST',
          headers: { 'X-Requested-With': 'XMLHttpRequest', 'X-CSRFToken': getCsrf() },
          body: data,
        });
        const json = await res.json();
        if (json.success) {
          updateCartBadge(json.cart_count);
          showToast(json.message || 'Added to cart!', 'success');
        } else {
          showToast(json.error || 'Something went wrong.', 'error');
        }
      } catch (err) {
        showToast('Network error. Please try again.', 'error');
      } finally {
        btn.innerHTML = original;
        btn.disabled = false;
      }
    });
  });

  // Password toggle utility
  window.togglePwd = function(inputId, btn) {
    const input = document.getElementById(inputId);
    if (!input) return;
    const isText = input.type === 'text';
    input.type = isText ? 'password' : 'text';
    btn.querySelector('i').className = isText ? 'bi bi-eye' : 'bi bi-eye-slash';
  };

  // Auto-dismiss flash messages after 5s
  setTimeout(() => {
    document.querySelectorAll('.ffang-alert').forEach(alert => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert.close();
    });
  }, 5000);

  // Navbar scroll effect
  const navbar = document.querySelector('.ffang-navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 20);
    }, { passive: true });
  }

  // Lazy load images with fade-in
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('loaded');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('img[loading="lazy"]').forEach(img => observer.observe(img));
  }

  // Animate stat numbers on scroll
  const stats = document.querySelectorAll('.stat-number');
  if (stats.length && 'IntersectionObserver' in window) {
    const statObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animation = 'statPop .4s ease forwards';
          statObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    stats.forEach(s => statObserver.observe(s));
  }
});

// ─── CSS animation for stats ─────────────────────────────────
const style = document.createElement('style');
style.textContent = `
  @keyframes statPop {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .ffang-navbar.scrolled {
    background: rgba(10,10,12,.98) !important;
    border-bottom-color: rgba(200,169,110,.2) !important;
  }
  img[loading="lazy"] { opacity: 0; transition: opacity .3s ease; }
  img[loading="lazy"].loaded { opacity: 1; }
`;
document.head.appendChild(style);
