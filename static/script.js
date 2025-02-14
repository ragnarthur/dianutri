document.addEventListener('DOMContentLoaded', () => {
    const scheduleContainer = document.querySelector('.schedule-container');
    const mealSections = document.querySelectorAll('.meal-section');
    const btnNext = document.getElementById('next');
    const btnPrev = document.getElementById('prev');
  
    // Índice do card atual
    let currentIndex = 0;
  
    function getCardWidth() {
      // Se existir pelo menos um mealSection, pegamos a largura dele;
      // caso contrário, fallback para a largura da janela
      return mealSections[0] ? mealSections[0].offsetWidth : window.innerWidth;
    }
  
    // Navega para o card com base no currentIndex
    function goToCard(index) {
      const cardWidth = getCardWidth();
      scheduleContainer.scrollTo({
        left: index * cardWidth,
        behavior: 'smooth'
      });
    }
  
    // Ajusta o cardWidth quando a janela é redimensionada
    window.addEventListener('resize', () => {
      goToCard(currentIndex);
    });
  
    if (btnNext && btnPrev && mealSections.length > 0) {
      btnNext.addEventListener('click', () => {
        if (currentIndex < mealSections.length - 1) {
          currentIndex++;
          goToCard(currentIndex);
        }
      });
  
      btnPrev.addEventListener('click', () => {
        if (currentIndex > 0) {
          currentIndex--;
          goToCard(currentIndex);
        }
      });
    }
  });
  