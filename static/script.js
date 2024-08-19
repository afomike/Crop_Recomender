 // Example of handling form submission
 document.getElementById('prediction-form').onsubmit = async function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Collect form data
    const formData = new FormData(event.target);

    // Send form data to the server
    const response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    // Get the result from the server
    const result = await response.json();
    document.getElementById('result').innerText = `Prediction: ${result.prediction}`;
};