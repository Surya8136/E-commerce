
    // Grab all elements with class 'food-trigger'
    const triggers = document.querySelectorAll('.food-trigger');
    const popCard = document.getElementById('popCard');
    const overlay = document.getElementById('overlay');

    triggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const name = trigger.dataset.name;
            const image = trigger.dataset.image;
            const description = trigger.dataset.description;

            document.getElementById('popCardTitle').innerText = name;
            document.getElementById('popCardImage').src = image;
            document.getElementById('popCardDescription').innerText = description;

            popCard.style.display = 'block';
            overlay.style.display = 'block';
        });
    });

    // Close button
    document.getElementById('closePopCard').addEventListener('click', () => {
        popCard.style.display = 'none';
        overlay.style.display = 'none';
    });

    // Click on overlay to close
    overlay.addEventListener('click', () => {
        popCard.style.display = 'none';
        overlay.style.display = 'none';
    });
