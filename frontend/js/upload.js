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

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("upload-form");
  const selfImageInput = document.getElementById("self_image");
  const garmentImageInput = document.getElementById("garment_image");
  const categorySelect = document.getElementById("category");
  const selfPreview = document.getElementById("self_preview");
  const garmentPreview = document.getElementById("garment_preview");

  selfImageInput.addEventListener("change", function () {
    previewImage(selfImageInput, selfPreview);
  });

  garmentImageInput.addEventListener("change", function () {
    previewImage(garmentImageInput, garmentPreview);
  });

  form.addEventListener("submit", function (event) {
    if (!selfImageInput.files.length || !garmentImageInput.files.length || !categorySelect.value) {
      event.preventDefault();
      alert("Please provide self image, garment image, and select a category.");
    }
  });
});
