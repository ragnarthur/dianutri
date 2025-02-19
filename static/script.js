// ============================================================================
// script.js
// Projeto: DiaNutri
// Descrição: 
//   1) Lógica do carrossel de refeições na página de Agenda Diária
//   2) Efeito "karaokê" (letra a letra), garantindo que cada palavra permaneça
//      unida (não seja cortada) graças ao contêiner ".karaoke-word".
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // Carrossel de refeições
  // -------------------------------------------------------------------------
  const scheduleContainer = document.querySelector('.schedule-container');
  const mealSections = document.querySelectorAll('.meal-section');
  const btnNext = document.getElementById('next');
  const btnPrev = document.getElementById('prev');
  
  // Índice do card atual no carrossel
  let currentIndex = 0;
  
  /**
   * Retorna a largura do card (ou, se não houver card, a largura da janela).
   */
  function getCardWidth() {
    return mealSections[0] ? mealSections[0].offsetWidth : window.innerWidth;
  }
  
  /**
   * Navega para o card com base no currentIndex
   */
  function goToCard(index) {
    const cardWidth = getCardWidth();
    scheduleContainer.scrollTo({
      left: index * cardWidth,
      behavior: 'smooth'
    });
  }
  
  /**
   * Ajusta o cardWidth quando a janela é redimensionada
   */
  window.addEventListener('resize', () => {
    goToCard(currentIndex);
  });
  
  /**
   * Eventos dos botões de navegação (próximo e anterior)
   */
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
  
  // -------------------------------------------------------------------------
  // Efeito "karaokê": animação letra por letra, garantindo que cada palavra 
  // permaneça unida dentro de um contêiner ".karaoke-word".
  // -------------------------------------------------------------------------
  const expText = document.querySelector('.explanatory-text');
  if (expText) {
    // Captura o texto original e limpa o elemento
    const originalText = expText.innerText.trim();
    expText.innerHTML = '';

    // Separa o texto em palavras (dividindo por espaço)
    const words = originalText.split(' ');

    let letterIndex = 0; // Conta global de letras para definir o animationDelay
    words.forEach((word, wIndex) => {
      // Cria um contêiner para a palavra inteira
      const wordSpan = document.createElement('span');
      wordSpan.classList.add('karaoke-word');
      
      // Para cada letra do 'word', criamos um <span class="letter">
      for (let i = 0; i < word.length; i++) {
        const letterSpan = document.createElement('span');
        letterSpan.classList.add('letter');
        letterSpan.innerText = word[i];

        // Define um delay progressivo para cada letra (0.05s por letra)
        letterSpan.style.animationDelay = (letterIndex * 0.05) + 's';
        letterIndex++;

        wordSpan.appendChild(letterSpan);
      }

      // Se não for a última palavra, adiciona um espaço após
      if (wIndex < words.length - 1) {
        const spaceSpan = document.createElement('span');
        // &nbsp; para garantir o espaço visível
        spaceSpan.innerHTML = '&nbsp;';
        wordSpan.appendChild(spaceSpan);
      }

      // Insere a palavra (contêiner) no texto explicativo
      expText.appendChild(wordSpan);
    });
  }
});
