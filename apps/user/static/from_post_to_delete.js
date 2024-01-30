// Функція для отримання значення cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Функція для додавання обробника подій до форми
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('deleteForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const url = this.action;

            fetch(url, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            }).then(response => {
                console.log(response);
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Something went wrong');
            }).then(data => {
                console.log(data);
                // Обробка успішного видалення
                // Наприклад, перенаправлення на іншу сторінку або виведення повідомлення
            }).catch(error => {
                console.error(error);
            });
        });
    }
});

document.getElementById('editEvent').addEventListener('submit', function(e) {
        e.preventDefault();

        // Отримання даних з форми
        let formData = new FormData(this);

        // Створення об'єкта для передачі даних
        let object = {};
        formData.forEach(function(value, key) {
            object[key] = value;
        });

        // Перетворення даних у JSON
        let json = JSON.stringify(object);

        fetch(this.action, {
            method: 'PUT', // або 'PATCH', залежно від вашого випадку
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
            body: json
        }).then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Something went wrong');
        }).then(data => {
            console.log(data);
            // Обробка успішної відповіді
        }).catch(error => {
            console.error(error);
        });
});