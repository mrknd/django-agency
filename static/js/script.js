document.addEventListener("DOMContentLoaded", () => {
  /* =========================
     BURGER MENU
  ========================= */
  const burger = document.getElementById("burger");
  const nav = document.getElementById("nav");

  if (burger && nav) {
    burger.addEventListener("click", () => {
      burger.classList.toggle("active");
      nav.classList.toggle("active");
      document.body.classList.toggle("menu-open");
    });

    const navLinks = nav.querySelectorAll(".nav__link");

    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        burger.classList.remove("active");
        nav.classList.remove("active");
        document.body.classList.remove("menu-open");
      });
    });
  }

  /* =========================
     SERVICES CAROUSEL
  ========================= */
  const servicesTrack = document.getElementById("servicesTrack");
  const servicesDots = document.getElementById("servicesDots");
  const prevBtn = document.querySelector(".services-carousel__nav--prev");
  const nextBtn = document.querySelector(".services-carousel__nav--next");
  const viewport = document.querySelector(".services-carousel__viewport");

  if (servicesTrack && servicesDots && viewport) {
    const slides = Array.from(servicesTrack.children);
    let currentIndex = 0;

    function isMobile() {
      return window.innerWidth <= 768;
    }

    function getSlidesPerView() {
      if (window.innerWidth <= 768) return 1;
      if (window.innerWidth <= 1200) return 2;
      return 3;
    }

    function getGap() {
      if (window.innerWidth <= 768) return 16;
      return 28;
    }

    function getMaxIndex() {
      return Math.max(0, slides.length - getSlidesPerView());
    }

    function createDots() {
      servicesDots.innerHTML = "";
      const dotsCount = getMaxIndex() + 1;

      for (let i = 0; i < dotsCount; i++) {
        const dot = document.createElement("button");
        dot.className = "services-carousel__dot";
        dot.type = "button";
        dot.setAttribute("aria-label", `Перейти к слайду ${i + 1}`);

        dot.addEventListener("click", () => {
          currentIndex = i;

          if (isMobile()) {
            const slideWidth = slides[0].offsetWidth + getGap();
            viewport.scrollTo({
              left: currentIndex * slideWidth,
              behavior: "smooth",
            });
          } else {
            updateSlider();
          }
        });

        servicesDots.appendChild(dot);
      }
    }

    function updateDots() {
      const dots = Array.from(servicesDots.children);

      dots.forEach((dot, index) => {
        dot.classList.toggle("active", index === currentIndex);
      });
    }

    function updateButtons() {
      if (!prevBtn || !nextBtn) return;

      if (isMobile()) {
        prevBtn.style.display = "none";
        nextBtn.style.display = "none";
        return;
      }

      prevBtn.style.display = "flex";
      nextBtn.style.display = "flex";

      prevBtn.disabled = currentIndex === 0;
      nextBtn.disabled = currentIndex >= getMaxIndex();

      prevBtn.style.opacity = currentIndex === 0 ? "0.45" : "1";
      nextBtn.style.opacity = currentIndex >= getMaxIndex() ? "0.45" : "1";
    }

    function updateSlider() {
      if (!slides.length) return;

      if (isMobile()) {
        servicesTrack.style.transform = "none";
        updateDots();
        updateButtons();
        return;
      }

      const slideWidth = slides[0].offsetWidth;
      const offset = currentIndex * (slideWidth + getGap());

      servicesTrack.style.transform = `translateX(-${offset}px)`;

      updateDots();
      updateButtons();
    }

    if (prevBtn) {
      prevBtn.addEventListener("click", () => {
        if (currentIndex > 0) {
          currentIndex--;
          updateSlider();
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        if (currentIndex < getMaxIndex()) {
          currentIndex++;
          updateSlider();
        }
      });
    }

    viewport.addEventListener(
      "scroll",
      () => {
        if (!isMobile() || !slides.length) return;

        const slideWidth = slides[0].offsetWidth + getGap();
        const index = Math.round(viewport.scrollLeft / slideWidth);

        currentIndex = Math.max(0, Math.min(index, getMaxIndex()));
        updateDots();
      },
      { passive: true }
    );

    window.addEventListener("resize", () => {
      const maxIndex = getMaxIndex();

      if (currentIndex > maxIndex) {
        currentIndex = maxIndex;
      }

      createDots();
      updateSlider();
    });

    createDots();
    updateSlider();
  }
});
// --------------------------------- Vacancy Page ---------------------------------
const vacancyItems = document.querySelectorAll(".vacancy-item");

if (vacancyItems.length) {
  vacancyItems.forEach((item) => {
    const body = item.querySelector(".vacancy-item__body");

    if (item.classList.contains("active")) {
      body.style.height = body.scrollHeight + "px";
    }
  });

  vacancyItems.forEach((item) => {
    const head = item.querySelector(".vacancy-item__head");
    const body = item.querySelector(".vacancy-item__body");

    head.addEventListener("click", () => {
      const isActive = item.classList.contains("active");

      vacancyItems.forEach((otherItem) => {
        const otherBody = otherItem.querySelector(".vacancy-item__body");
        otherItem.classList.remove("active");
        otherBody.style.height = 0;
      });

      if (!isActive) {
        item.classList.add("active");
        body.style.height = body.scrollHeight + "px";
      }
    });
  });

  window.addEventListener("resize", () => {
    vacancyItems.forEach((item) => {
      const body = item.querySelector(".vacancy-item__body");
      if (item.classList.contains("active")) {
        body.style.height = body.scrollHeight + "px";
      }
    });
  });
}

// --------------------------------- Modal ---------------------------------
// ======================
    // CONTACT MODAL
    // ======================
    const modal = document.getElementById("contactModal");
    const openButtons = document.querySelectorAll(".open-modal");
    const closeBtn = document.getElementById("modalClose");
    const overlay = document.getElementById("modalOverlay");

    // відкриття
    openButtons.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.preventDefault();

            if (modal) {
                modal.classList.add("active");
                document.body.classList.add("modal-open");
            }
        });
    });

    // функція закриття
    const closeModal = () => {
        if (modal) {
            modal.classList.remove("active");
            document.body.classList.remove("modal-open");
        }
    };

    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    if (overlay) overlay.addEventListener("click", closeModal);

    // ESC
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            closeModal();
            closeSuccessModal();
        }
    });


    // ======================
    // SUCCESS MODAL
    // ======================
    const form = document.querySelector(".modal__form");
    const successModal = document.getElementById("successModal");
    const successClose = document.getElementById("successClose");

    // submit
    if (form && successModal) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();

            // закриваємо першу модалку
            closeModal();

            // відкриваємо success
            successModal.classList.add("active");
            document.body.classList.add("modal-open");

            form.reset();
        });
    }

    // закриття success
    const closeSuccessModal = () => {
        if (successModal) {
            successModal.classList.remove("active");
            document.body.classList.remove("modal-open");
        }
    };

    if (successClose) {
        successClose.addEventListener("click", closeSuccessModal);
    }

// ==============================================================
    // ==================== FAQ ==================
document.addEventListener('DOMContentLoaded', function () {
  const faqItems = document.querySelectorAll('.faq-item__faq');

  faqItems.forEach(function (item) {
    const question = item.querySelector('.faq-question__faq');

    question.addEventListener('click', function () {
      const isActive = item.classList.contains('active__faq');

      faqItems.forEach(function (faqItem) {
        faqItem.classList.remove('active__faq');
      });

      if (!isActive) {
        item.classList.add('active__faq');
      }
    });
  });
});
// -------------------------------------- BLOG Zmist
document.addEventListener("DOMContentLoaded", function () {
    const section = document.querySelector(".orbitflow__section");
    const left = document.querySelector(".orbitflow__left");
    const right = document.querySelector(".orbitflow__right");
    const pinArea = document.querySelector(".orbitflow__pin-area");
    const circleWrap = document.querySelector(".orbitflow__circle-wrap");
    const progressCircle = document.querySelector(".orbitflow__circle-progress");
    const currentStep = document.getElementById("orbitflowStep");
    const cards = document.querySelectorAll(".orbitflow__card");

    if (!section || !left || !right || !pinArea || !circleWrap || !progressCircle || !currentStep || !cards.length) {
        return;
    }

    const totalSteps = cards.length;
    const radius = 124;
    const circumference = 2 * Math.PI * radius;

    progressCircle.style.strokeDasharray = circumference;
    progressCircle.style.strokeDashoffset = circumference;

    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("orbitflow__is-visible");
                }
            });
        },
        { threshold: 0.15 }
    );

    cards.forEach((card) => revealObserver.observe(card));

    function setOrbitflowMetrics() {
        if (window.innerWidth <= 991) {
            pinArea.style.minHeight = "auto";
            section.style.setProperty("--orbitflow-fixed-left", "200px");
            circleWrap.classList.remove("orbitflow__is-fixed", "orbitflow__is-bottom");
            return;
        }

        pinArea.style.minHeight = `${right.offsetHeight}px`;

        const leftRect = left.getBoundingClientRect();
        const centerX = leftRect.left + window.scrollX + (leftRect.width / 2);

        section.style.setProperty("--orbitflow-fixed-left", `${centerX}px`);
    }

    function updateOrbitflow() {
        if (window.innerWidth <= 991) {
            return;
        }

        const sectionRect = section.getBoundingClientRect();
        const pinRect = pinArea.getBoundingClientRect();
        const circleHeight = circleWrap.offsetHeight;
        const viewportCenter = window.innerHeight / 2;

        circleWrap.classList.remove("orbitflow__is-fixed", "orbitflow__is-bottom");

        const startPin = pinRect.top <= viewportCenter - (circleHeight / 2);
        const endPin = pinRect.bottom <= viewportCenter + (circleHeight / 2);

        if (!startPin) {
            // лишається зверху
        } else if (endPin) {
            circleWrap.classList.add("orbitflow__is-bottom");
        } else {
            circleWrap.classList.add("orbitflow__is-fixed");
        }

        const scrollableDistance = Math.max(section.offsetHeight - window.innerHeight, 1);
        const passed = Math.max(0, -sectionRect.top);
        let progress = passed / scrollableDistance;

        progress = Math.max(0, Math.min(progress, 1));

        progressCircle.style.strokeDashoffset = circumference - (progress * circumference);

        let activeStep = Math.round(progress * totalSteps);

        if (sectionRect.top > 0) {
            activeStep = 0;
        }

        if (sectionRect.bottom <= window.innerHeight) {
            activeStep = totalSteps;
        }

        activeStep = Math.max(0, Math.min(activeStep, totalSteps));
        currentStep.textContent = activeStep;

        cards.forEach((card, index) => {
            card.classList.toggle("orbitflow__is-active", index === activeStep - 1);
        });
    }

    function handleAll() {
        setOrbitflowMetrics();
        updateOrbitflow();
    }

    handleAll();

    let ticking = false;

    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(() => {
                updateOrbitflow();
                ticking = false;
            });
            ticking = true;
        }
    }

    window.addEventListener("scroll", requestTick, { passive: true });
    window.addEventListener("resize", handleAll);
});


