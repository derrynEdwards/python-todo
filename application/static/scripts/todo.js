// Tasks Delete Buttons
const deletebuttons = document.querySelectorAll('.delete-button');
for (let i = 0; i < deletebuttons.length; i++) {
    const button = deletebuttons[i];
    button.onclick = function(e) {
        const todoId = e.target.dataset['id'];
        fetch('/' + todoId + '/delete-task', {
            method: 'DELETE'
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse) {
            location.reload(true);
        })
    }
}
// Lists Delete Buttons
const lists_deletebuttons = document.querySelectorAll('.list_delete-button');
for (let i = 0; i < lists_deletebuttons.length; i++) {
    const button = lists_deletebuttons[i];
    button.onclick = function(e) {
        const listId = e.target.dataset['id'];
        fetch('/' + listId + '/delete-list', {
            method: 'DELETE'
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse) {
            location.reload(true);
        })
    }
}
// Tasks Check Boxes
const checkboxes = document.querySelectorAll('.check-completed');
for (let i = 0; i < checkboxes.length; i++) {
    const checkbox = checkboxes[i];
    checkbox.onchange = function(e) {
        const newCompleted = e.target.checked;
        const todoId = e.target.dataset['id'];
        fetch('/' + todoId + '/set-completed', {
            method: 'POST',
            body: JSON.stringify({
                'completed': newCompleted
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse) {
            location.reload(true);
        })
    }
}
// Lists Check Boxes
const list_checkboxes = document.querySelectorAll('.check-list-completed');
for (let i = 0; i < list_checkboxes.length; i++) {
    const list_checkbox = list_checkboxes[i];
    list_checkbox.onchange = function(e) {
        const newCompleted = e.target.checked;
        const listId = e.target.dataset['id'];
        fetch('/' + listId + '/set-list-completed', {
            method: 'POST',
            body: JSON.stringify({
                'completed': newCompleted
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse) {
            location.reload(true);
        })
    }
}
// Tasks Form
try {
    document.getElementById('form').onsubmit = function(e) {
        e.preventDefault();
        fetch('/create-todo', {
            method: 'POST',
            body: JSON.stringify({
                'description': document.getElementById('description').value,
                'list_id': parseInt(document.getElementById('form').dataset['id'])
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse) {
            location.reload(true);
        })
        .catch(function() {
            document.getElementById('error').className = '';
        })
    }
}
catch(err) {}
// Lists Form
document.getElementById('list-form').onsubmit = function(e) {
    e.preventDefault();
    fetch('/create-list', {
        method: 'POST',
        body: JSON.stringify({
            'name': document.getElementById('list-name').value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(jsonResponse) {
        location.reload(true);
    })
    .catch(function() {
        document.getElementById('error').className = '';
    })
}