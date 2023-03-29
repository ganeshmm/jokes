async function laugh() {
    const joke = document.getElementById("joke").value
    console.log("B")
    fetch("/laugh", {
        method: "POST",
        body: joke
    })
    .then(response => {
        if (!response.ok) {
            console.log("VERY BAD");
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    // data = response.json()
    // console.log("DATA")
    // console.log(data)
    // const favicon = document.getElementById("favicon")
    // favicon.setAttribute("href", "/static/" + rofl + ".png")
    
    // const score = document.getElementById("score")
    // score.textContent = "Score: " + data.laughter

    // const emoji = document.getElementById("emoji")
    // emoji.textContent = data.emoji
}