// Gallery Upload Form Toggle
const uploadToggle = document.getElementById('upload-toggle');
const uploadFormContainer = document.getElementById('upload-form-container');

if (uploadToggle && uploadFormContainer) {
    uploadToggle.addEventListener('click', () => {
        if (uploadFormContainer.style.display === 'none' || !uploadFormContainer.style.display) {
            uploadFormContainer.style.display = 'block';
            uploadToggle.textContent = 'Cancel Upload';
        } else {
            uploadFormContainer.style.display = 'none';
            uploadToggle.textContent = 'Upload Photo';
        }
    });
}