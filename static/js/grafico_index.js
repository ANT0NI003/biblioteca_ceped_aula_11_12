console.log('grafico_index.js rodando');

const ctx = document.getElementById('graficoBiblioteca');

new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Alunos', 'Livros', 'Empréstimos'],
        datasets: [{
            data: window.dadosGrafico,
            backgroundColor: ['#4e73df', '#1cc88a', '#f6c23e']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});