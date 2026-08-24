function previewImage(inputEl, previewEl) {
  const file = inputEl.files[0];
  if (!file) {
    previewEl.style.display = "none";
    previewEl.src = "#";
    return;
  }

  const reader = new FileReader();
  reader.onload = function (event) {
    previewEl.src = event.target.result;
    previewEl.style.display = "block";
  };
  reader.readAsDataURL(file);
}

function isFileSizeValid(file, maxSizeBytes) {
  return file && file.size <= maxSizeBytes;
}

function clearPreview(previewEl) {
  previewEl.style.display = "none";
  previewEl.src = "#";
}

document.addEventListener("DOMContentLoaded", function () {
  const MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024;
  const form = document.getElementById("upload-form");
  const selfImageInput = document.getElementById("self_image");
  const garmentImageInput = document.getElementById("garment_image");
  const categorySelect = document.getElementById("category");
  const selfPreview = document.getElementById("self_preview");
  const garmentPreview = document.getElementById("garment_preview");

  selfImageInput.addEventListener("change", function () {
    const file = selfImageInput.files[0];
    if (file && !isFileSizeValid(file, MAX_FILE_SIZE_BYTES)) {
      alert("Self image must be less than or equal to 5MB.");
      selfImageInput.value = "";
      clearPreview(selfPreview);
      return;
    }
    previewImage(selfImageInput, selfPreview);
  });

  garmentImageInput.addEventListener("change", function () {
    const file = garmentImageInput.files[0];
    if (file && !isFileSizeValid(file, MAX_FILE_SIZE_BYTES)) {
      alert("Garment image must be less than or equal to 5MB.");
      garmentImageInput.value = "";
      clearPreview(garmentPreview);
      return;
    }
    previewImage(garmentImageInput, garmentPreview);
  });

  form.addEventListener("submit", function (event) {
    const selfFile = selfImageInput.files[0];
    const garmentFile = garmentImageInput.files[0];

    if (selfFile && !isFileSizeValid(selfFile, MAX_FILE_SIZE_BYTES)) {
      event.preventDefault();
      alert("Self image must be less than or equal to 5MB.");
      selfImageInput.value = "";
      clearPreview(selfPreview);
      return;
    }

    if (garmentFile && !isFileSizeValid(garmentFile, MAX_FILE_SIZE_BYTES)) {
      event.preventDefault();
      alert("Garment image must be less than or equal to 5MB.");
      garmentImageInput.value = "";
      clearPreview(garmentPreview);
      return;
    }

    if (!selfImageInput.files.length || !garmentImageInput.files.length || !categorySelect.value) {
      event.preventDefault();
      alert("Please provide self image, garment image, and select a category.");
    }
  });
});
