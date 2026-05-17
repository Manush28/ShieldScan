chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
    if (changeInfo.status === "complete" && tab.url) {

        try {
            const res = await fetch("http://127.0.0.1:8000/detect", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ url: tab.url })
            });

            const data = await res.json();

            chrome.storage.local.set({ result: data });

            if (data.label === "SAFE") {
                chrome.action.setBadgeText({ text: "✓", tabId });
                chrome.action.setBadgeBackgroundColor({ color: "green" });
            }
            else if (data.label === "SUSPICIOUS") {
                chrome.action.setBadgeText({ text: "!", tabId });
                chrome.action.setBadgeBackgroundColor({ color: "orange" });
            }
            else {
                chrome.action.setBadgeText({ text: "✕", tabId });
                chrome.action.setBadgeBackgroundColor({ color: "red" });

                chrome.tabs.update(tabId, {
                    url: chrome.runtime.getURL("block.html")
                });
            }

        } catch (err) {
            console.error(err);
        }
    }
});
