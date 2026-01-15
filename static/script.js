document.getElementById('reportForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const generateBtn = document.getElementById('generateBtn');
    const btnText = document.getElementById('btnText');
    const spinner = document.getElementById('spinner');
    const errorDiv = document.getElementById('error');
    const successDiv = document.getElementById('success');
    const dobInput = document.getElementById('dob');

    // Reset messages
    errorDiv.classList.add('hidden');
    successDiv.classList.add('hidden');

    // Show loading state
    generateBtn.disabled = true;
    btnText.textContent = 'Generating... (60 secs)';
    spinner.classList.remove('hidden');

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                dob: dobInput.value
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to generate report');
        }

        // Get HTML content
        const htmlContent = await response.text();

        // Open in new tab
        const newWindow = window.open('', '_blank');
        newWindow.document.write(htmlContent);
        newWindow.document.close();

        // Show success
        successDiv.classList.remove('hidden');
        successDiv.textContent = '✅ Report opened in new tab!';

        // Hide success after 5 seconds
        setTimeout(() => {
            successDiv.classList.add('hidden');
        }, 5000);

    } catch (error) {
        console.error('Error:', error);
        errorDiv.textContent = `❌ Error: ${error.message}`;
        errorDiv.classList.remove('hidden');
    } finally {
        // Reset button state
        generateBtn.disabled = false;
        btnText.textContent = 'Generate Report';
        spinner.classList.add('hidden');
    }
});
