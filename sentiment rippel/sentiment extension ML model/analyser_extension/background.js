// 1. Create the right-click menu option
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "analyze-text",
    title: "Analyze Sentiment ML analyser",
    contexts: ["selection"]
  });
});

// 2. Listen for the right-click menu action
chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "analyze-text") {
    const selectedText = info.selectionText;

    // 3. Send text to your FastAPI server
    fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: selectedText })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Server HTTP error: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      // A. Save the result to local history (Storage API)
      chrome.storage.local.get({ history: [] }, (result) => {
        let newHistory = [data.sentiment, ...result.history].slice(0, 5);
        chrome.storage.local.set({ history: newHistory });
      });

      // B. Inject a script to visually highlight text on the web page
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: (sentimentText, descriptionText) => {
          const selection = window.getSelection();
          if (!selection || !selection.rangeCount) return;
          
          const range = selection.getRangeAt(0);
          const span = document.createElement("span");
          
          // Case-insensitive check matching your FastAPI response strings
          const isPositive = sentimentText.toLowerCase().includes("positive");
          
          // Styling rules based on evaluation
          span.style.backgroundColor = isPositive ? "#c8e6c9" : "#ffcdd2"; // Green vs Red
          span.style.color = "#000000"; 
          span.style.borderRadius = "2px";
          span.style.padding = "2px 4px";
          span.title = descriptionText; // Hovering shows description
          
          try {
            range.surroundContents(span);
          } catch (e) {
            console.error("Could not surround text block safely: ", e);
          }
        },
        args: [data.sentiment, data.description] // Passes variables from background to webpage
      });
    })
    .catch(error => {
      console.error("Failed to analyze sentiment:", error);
    });
  }
});
