document.addEventListener("DOMContentLoaded", function () {
    const params = new URLSearchParams(window.location.search);
    const jobId = params.get("job_id");

    if (!jobId) {
        showErrorState("No job ID was provided.");
        return;
    }

    showLoadingState();
    startPolling(jobId);
});