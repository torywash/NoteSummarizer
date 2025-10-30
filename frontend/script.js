const button = document.getElementById('summarizeBtn');

button.addEventListener('click', async () => {
    const textEl = document.getElementById('inputText');
    const outputEl = document.getElementById('summaryText');
    if (!textEl || !outputEl) return console.error('Required DOM elements missing');

    const text = textEl.value;
    outputEl.innerText = 'Summarizing...';

    try {
        const response = await fetch(`/summarize`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        if (!response.ok) throw new Error(`Server responded ${response.status}`);
        const data = await response.json();
        outputEl.innerText = data.summary || 'No summary returned';
    } catch (err) {
        console.error(err);
        outputEl.innerText = 'Error: ' + (err.message || err);
    }
});
