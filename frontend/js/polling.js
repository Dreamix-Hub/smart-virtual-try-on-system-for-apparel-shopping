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
                showResultImage(result.result_url);
            } else if (result.status === "failed" || result.status === "error") {
                stopPolling();
                showErrorState("The try-on job failed. Please try again.");
            }
        } catch (error) {
            console.error("Error polling job status:", error);
            stopPolling();
            showErrorState("Lost connection while checking your job status.");
        }
    }, 2500); // Poll every 2.5 seconds
}

function stopPolling() {
    if (pollingInterval) {
        clearInterval(pollingInterval);
        pollingInterval = null;
    }
}
