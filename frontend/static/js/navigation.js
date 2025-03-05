const toggleOpen = document.getElementById('toggleOpen');
const toggleClose = document.getElementById('toggleClose');
const collapseMenu = document.getElementById('collapseMenu');

function handleClick () {
  if (collapseMenu.style.display === 'block') {
    collapseMenu.style.display = 'none';
  } else {
    collapseMenu.style.display = 'block';
  }
}

toggleOpen.addEventListener('click', handleClick);
toggleClose.addEventListener('click', handleClick);

document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  const navLinks = document.querySelectorAll('header ul li a');

  // sourcery skip: avoid-function-declarations-in-blocks
  function onScroll () {
    if (window.scrollY > 50) {
      header.classList.add('bg-white', 'shadow-md', '!text-black');
      header.classList.remove('!bg-transparent', '!text-white');
    } else {
      header.classList.add('!bg-transparent', '!text-white');
      header.classList.remove('bg-white', 'shadow-md', '!text-black');
    }

    // Change active link color on scroll
    const fromTop = window.scrollY + 100;
    navLinks.forEach((link) => {
      const section = document.querySelector(link.getAttribute('href'));
      if (
        section &&
        section.offsetTop <= fromTop &&
        section.offsetTop + section.offsetHeight > fromTop
      ) {
        link.classList.add('text-primary-600', 'font-bold');
      } else {
        link.classList.remove('text-primary-600', 'font-bold');
      }
    });
  }

  window.addEventListener('scroll', onScroll);
});

// Testimonials
document.addEventListener('DOMContentLoaded', function () {
  const tabs = document.querySelectorAll('.tab');
  const contents = document.querySelectorAll('.tab-content');

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function (e) {
      const targetId = tab.id.replace('Tab', 'Content');

      // Hide all content divs
      contents.forEach(function (content) {
        content.classList.add('hidden');
      });

      // Remove active class from all tabs
      tabs.forEach(function (tab) {
        tab.classList.remove(
          'border-primary-600',
          'font-bold',
          'text-primary-600'
        );
        tab.classList.add(
          'border-transparent',
          'text-gray-600',
          'font-semibold'
        );
      });

      // Show the target content
      document.getElementById(targetId).classList.remove('hidden');

      // Add active class to the clicked tab
      tab.classList.add('border-primary-600', 'font-bold', 'text-primary-600');
      tab.classList.remove(
        'border-transparent',
        'text-gray-600',
        'font-semibold'
      );
    });
  });
});
