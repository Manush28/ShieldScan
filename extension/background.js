chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {

    if (changeInfo.status !== "complete" || !tab.url) {
        return;
    }

    // Ignore extension pages
    if (
        tab.url.startsWith("chrome-extension://") ||
        tab.url.startsWith("chrome://")
    ) {
        return;
    }

    try {

        const res = await fetch("http://127.0.0.1:8000/detect", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: tab.url })
        });

        const data = await res.json();

        // Save latest scan result
        chrome.storage.local.set({ result: data });

        // SAFE
        if (data.label === "SAFE") {

            chrome.action.setBadgeText({
                text: "✓",
                tabId
            });

            chrome.action.setBadgeBackgroundColor({
                color: "green"
            });
        }

        // SUSPICIOUS
        else if (data.label === "SUSPICIOUS") {

            chrome.action.setBadgeText({
                text: "!",
                tabId
            });

            chrome.action.setBadgeBackgroundColor({
                color: "orange"
            });
        }

        // MALICIOUS
        else {

            chrome.action.setBadgeText({
                text: "✕",
                tabId
            });

            chrome.action.setBadgeBackgroundColor({
                color: "red"
            });

            // Redirect ONLY real malicious websites
            chrome.tabs.update(tabId, {
                url: chrome.runtime.getURL("block.html")
            });
        }

    } catch (err) {
        console.error("ShieldScan Error:", err);
    }

});