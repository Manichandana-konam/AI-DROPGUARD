async function predict() {

    const flow = document.getElementById("flow").value;
    const duration = document.getElementById("duration").value;
    const presence = document.getElementById("presence").value;

    if (flow === "" || duration === "") {
        document.getElementById("result").innerHTML =
            "⚠️ Please enter Flow Rate and Duration.";
        return;
    }

    try {

        const response = await fetch("http://127.0.0.1:5000/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                Flow_Rate: flow,
                Duration: duration,
                Presence: presence
            })

        });

        const data = await response.json();

        document.getElementById("result").innerHTML = data.Prediction;

    } catch (error) {

        document.getElementById("result").innerHTML =
            "❌ Cannot connect to AI DropGuard server.";

        console.error(error);
    }
}