async function uploadImages(formData) {
    const response = await fetch(`${API_BASE_URL}/api/try-on/upload-images`, {
        method: 'POST',
        body: formData
    });
    if (!response.ok) {
        throw new Error('Failed to upload images');
    }
    return response.json();
}

async function getJobStatus(jobId) {
    const response = await fetch(`${API_BASE_URL}/api/try-on/${jobId}/status`);
    if (!response.ok) {
        throw new Error('Failed to get job status');
    }
    return response.json();
}
