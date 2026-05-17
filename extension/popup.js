function updateUI(res) {

    if (!res) return;

    const status = document.getElementById("status");
    const url = document.getElementById("url");
    const score = document.getElementById("score");
    const reasons = document.getElementById("reasons");
    const explanation = document.getElementById("explanation");
    const bar = document.getElementById("riskBar");

    // URL
    url.innerText = res.url;

    // Risk level
    let riskLevel = "";

    if (res.score < 0.3) {
        riskLevel = "LOW RISK";
        status.style.color = "green";
        bar.style.background = "green";
    }
    else if (res.score < 0.65) {
        riskLevel = "MEDIUM RISK";
        status.style.color = "orange";
        bar.style.background = "orange";
    }
    else {
        riskLevel = "HIGH RISK";
        status.style.color = "red";
        bar.style.background = "red";
    }

    // Status
    status.innerText =
        `${res.label} (${riskLevel})`;

    // Score
    score.innerText =
        `Risk Score: ${Math.round(res.score * 100)}%
Confidence: ${res.confidence}`;

    // Risk bar
    bar.style.width = `${res.score * 100}%`;

    // Reasons
    reasons.innerHTML = "";

    res.reasons.forEach(reason => {
        const div = document.createElement("div");
        div.innerText = "• " + reason;
        reasons.appendChild(div);
    });

    // Explanation
    explanation.innerText = res.explanation;
}


// Initial load
chrome.storage.local.get("result", (data) => {
    updateUI(data.result);
});


// Live updates
chrome.storage.onChanged.addListener((changes) => {
    if (changes.result) {
        updateUI(changes.result.newValue);
    }
});