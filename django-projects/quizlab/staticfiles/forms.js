document.addEventListener('DOMContentLoaded', () => {
    const addForm = document.querySelector('.add-form');
    const openBtn = document.querySelector('.open-create-form-btn');
    const closeBtn = document.querySelector('.close-creation-form');

    // Open the form
    if (openBtn) {
        openBtn.addEventListener('click', () => {
            addForm.classList.remove('hidden');
        });
    }

    // Close the form using the 'X' button
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            addForm.classList.add('hidden');
        });
    }

    // Optional: Close the form when clicking outside the modal box (on the backdrop)
    addForm.addEventListener('click', (e) => {
        if (e.target === addForm) {
            addForm.classList.add('hidden');
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const deleteFormModal = document.querySelector('.delete-form');
    const closeDeleteBtns = document.querySelectorAll('.close-delete-form');
    const deleteQuizIdInput = document.getElementById('delete-quiz-id');

    // Barcha o'chirish tugmalarini topamiz
    document.querySelectorAll('.open-delete-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            // Tugmadan quiz ID'sini olamiz
            const quizId = btn.getAttribute('data-quiz-id');
            
            // Yashirin inputga qiymatni beramiz (mana shu qism ishlamayotgan edi)
            deleteQuizIdInput.value = quizId;
            
            // Modalni ochamiz
            deleteFormModal.classList.remove('hidden');
        });
    });

    // Yopish tugmalari
    closeDeleteBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            deleteFormModal.classList.add('hidden');
        });
    });

    // Orqa fonni bosganda yopish
    deleteFormModal.addEventListener('click', (e) => {
        if (e.target === deleteFormModal) {
            deleteFormModal.classList.add('hidden');
        }
    });
});


function openEditModal(quizId) {
    const modal = document.getElementById(`edit-modal-${quizId}`);
    if (modal) {
        modal.classList.remove('hidden');
    }
}

function closeEditModal(quizId) {
    const modal = document.getElementById(`edit-modal-${quizId}`);
    if (modal) {
        modal.classList.add('hidden');
    }
}