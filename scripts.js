const from = document.getElementById('image-uploaded');
from.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('image', document.getElementById('image-uploaded').files[0]);

    try {
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        document.getElementById('proceesed img').src = data.processed_image;
    }
    catch (error) {
        console.error(error);
    }
});