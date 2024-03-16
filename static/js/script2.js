// JavaScript for the personal finance tracker

// Sample transaction data (replace with actual data)
let transactions = [];

// Update current balance and recent transactions
function updateOverview() {
    // Update current balance
    let totalBalance = transactions.reduce((acc, curr) => acc + curr.amount, 0);
    document.getElementById('currentBalance').textContent = totalBalance.toFixed(2);

    // Update recent transactions list
    let transactionList = document.getElementById('transactionList');
    transactionList.innerHTML = '';
    transactions.slice(0, 5).forEach(transaction => {
        let listItem = document.createElement('li');
        listItem.textContent = `${transaction.description}: $${transaction.amount.toFixed(2)}`;
        transactionList.appendChild(listItem);
    });
}

// Update expense breakdown chart
function updateChart() {
    let labels = [];
    let data = [];
    let colors = [];

    // Sample data (replace with actual data)
    let categories = {
        'Food': 300,
        'Transportation': 150,
        'Utilities': 100,
        'Entertainment': 200
    };

    for (let category in categories) {
        labels.push(category);
        data.push(categories[category]);
        colors.push(getRandomColor());
    }

    let ctx = document.getElementById('expenseChart').getContext('2d');
    let chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: colors
            }]
        },
        options: {}
    });
}

// Add transaction event listener
document.getElementById('addTransactionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let description = document.getElementById('description').value;
    let amount = parseFloat(document.getElementById('amount').value);

    if (description && !isNaN(amount)) {
        // Add transaction to the list
        transactions.push({ description: description, amount: amount });
        // Update overview and chart
        updateOverview();
        updateChart();
        // Reset form
        document.getElementById('addTransactionForm').reset();
    } else {
        alert('Please enter valid description and amount.');
    }
});

// Helper function to generate random colors
function getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Initial setup
updateOverview();
updateChart();
