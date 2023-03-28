function laugh() {
    const joke = document.getElementById("joke").value;
    fetch("/laugh", {
        method: "POST",
        body: joke
    }).then(response => JSON.parse(response))
    .then(data => {
        const score = document.getElementById("score");
        score.textContent = "Score: " + data.laughter;
    })
}