document.getElementById('scrape-btn').addEventListener('click', async () => {
  const resultBox = document.getElementById('result-box');
  const textPreview = document.getElementById('text-preview');
  
  // Clear previous results
  resultBox.style.display = 'none';
  textPreview.innerText = "Checking your selection...";
  textPreview.style.display = 'block';

  // 1. Find the active tab
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // 2. Reach into the page to grab the MOUSE SELECTION
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: () => {
      // This is the specific "mouse selection" command
      return window.getSelection().toString().trim();
    }
  }, (results) => {
    const mouseSelectedText = results[0].result;

    if (!mouseSelectedText) {
      textPreview.innerText = "⚠️ No text selected! Please highlight some text with your mouse first.";
      return;
    }

    // Show a snippet of what you selected
    textPreview.innerText = `Selected: "${mouseSelectedText.substring(0, 120)}..."`;

    // 3. Send that specific text to your local ML server
    fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: mouseSelectedText })
    })
    .then(response => response.json())
    .then(data => {
      resultBox.className = `result ${data.sentiment}`;
      resultBox.innerText = `Sentiment: ${data.sentiment}`;
      resultBox.style.display = 'block';
    })
    .catch(err => {
      resultBox.className = 'result Negative';
      resultBox.innerText = "Server Error: Is FastAPI running?";
      resultBox.style.display = 'block';
    });
  });
});