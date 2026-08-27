let pollingInterval;

function startPolling(jobId) {
    if (pollingInterval) {
        clearInterval(pollingInterval);
    }
    
    pollingInterval = setInterval(async () => {
        try {
            const result = await getJobStatus(jobId);
            
            if (result.status === "done") {
                stopPolling();
                alert("Job is done! UI should be updated here.");
                // TODO: Update UI with result
            } else if (result.status === "failed" || result.status === "error") {
                stopPolling();
                alert("Job failed.");
            }
        } catch (error) {
            console.error("Error polling job status:", error);
            stopPolling();
        }
    }, 2500); // Poll every 2.5 seconds
}

function stopPolling() {
    if (pollingInterval) {
        clearInterval(pollingInterval);
        pollingInterval = null;
    }
}
