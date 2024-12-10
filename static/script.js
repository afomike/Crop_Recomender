document.getElementById('prediction-form').onsubmit = async function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Collect form data
    const formData = new FormData(event.target);

    try {
        // Send form data to the server
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        // Get the result from the server
        const result = await response.json();
        document.getElementById('result').innerText = `Prediction: ${result.prediction}`;
    } catch (error) {
        // Display error message
        document.getElementById('result').innerText = `An error occurred: ${error.message}`;
    }
};
