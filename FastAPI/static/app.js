function updateQuestionOptions() {
  const mode = document.getElementById("mode").value;
  const qSel = document.getElementById("question");
  qSel.innerHTML = "";
  const maxQuestions = mode === "thread" ? 7 : 8;
  for (let i = 1; i <= maxQuestions; i++) {
    const opt = document.createElement("option");
    opt.value = i;
    opt.textContent = i;
    qSel.appendChild(opt);
  }
}

function runScenario() {
  const mode = document.getElementById("mode").value;
  const question = document.getElementById("question").value;
  const scenario = document.getElementById("scenario").value;
  const url = `/${mode}/${question}?scenario=${scenario}`;

  const statusText = document.getElementById("statusText");
  const output = document.getElementById("output");
  const explanation = document.getElementById("explanation");

  statusText.textContent = "در حال اجرا ...";
  explanation.textContent = "";

  fetch(url)
    .then(r => r.json())
    .then(data => {
      if (Array.isArray(data.output)) {
        output.textContent = data.output.join("\n");
      } else {
        output.textContent = JSON.stringify(data, null, 2);
      }
      // ست‌کردن توضیح اگر موجود بود
      if (data.explanation) {
        explanation.textContent = data.explanation;
      } else {
        explanation.textContent = "";
      }
      statusText.textContent = "";
    })
    .catch(err => {
      output.textContent = "خطا: " + err;
      statusText.textContent = "";
      explanation.textContent = "";
    });
}

updateQuestionOptions();
