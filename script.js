// Carrega as tarefas do localStorage ao iniciar
document.addEventListener('DOMContentLoaded', loadTasks);

// Função para adicionar uma nova tarefa
function addTask() {
    const taskInput = document.getElementById('new-task');
    const taskText = taskInput.value.trim();

    if (taskText === '') {
        alert('Por favor, digite uma tarefa.');
        return;
    }

    const taskItem = createTaskElement(taskText, false);
    document.getElementById('task-list').appendChild(taskItem);

    saveTask(taskText, false);
    taskInput.value = '';
}

// Cria o elemento HTML de uma tarefa com opções de edição e status
function createTaskElement(taskText, completed) {
    const taskItem = document.createElement('li');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = completed;
    checkbox.onchange = function() { toggleCompleted(taskItem, taskText); };

    const taskSpan = document.createElement('span');
    taskSpan.textContent = taskText;
    taskSpan.contentEditable = true;
    taskSpan.onblur = function() { updateTaskText(taskItem, taskSpan.textContent); };

    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Excluir';
    deleteBtn.classList.add('delete-btn');
    deleteBtn.onclick = function() { deleteTask(taskItem); };

    if (completed) taskItem.classList.add('completed');

    taskItem.appendChild(checkbox);
    taskItem.appendChild(taskSpan);
    taskItem.appendChild(deleteBtn);

    return taskItem;
}

// Atualiza o status de conclusão de uma tarefa
function toggleCompleted(taskItem, taskText) {
    taskItem.classList.toggle('completed');
    const completed = taskItem.classList.contains('completed');
    updateTaskStatus(taskText, completed);
}

// Atualiza o texto de uma tarefa no localStorage
function updateTaskText(taskItem, newText) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    const oldText = taskItem.querySelector('span').textContent;
    const taskIndex = tasks.findIndex(task => task.text === oldText);
    
    if (taskIndex !== -1) {
        tasks[taskIndex].text = newText;
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }
}

// Exclui uma tarefa e atualiza no localStorage
function deleteTask(taskItem) {
    const taskText = taskItem.querySelector('span').textContent;
    taskItem.remove();
    removeTaskFromStorage(taskText);
}

// Salva uma nova tarefa no localStorage
function saveTask(taskText, completed) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.push({ text: taskText, completed: completed });
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Atualiza o status de conclusão de uma tarefa no localStorage
function updateTaskStatus(taskText, completed) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    const taskIndex = tasks.findIndex(task => task.text === taskText);
    if (taskIndex !== -1) {
        tasks[taskIndex].completed = completed;
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }
}

// Remove uma tarefa do localStorage
function removeTaskFromStorage(taskText) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    const updatedTasks = tasks.filter(task => task.text !== taskText);
    localStorage.setItem('tasks', JSON.stringify(updatedTasks));
}

// Carrega as tarefas do localStorage e exibe
function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.forEach(task => {
        const taskItem = createTaskElement(task.text, task.completed);
        document.getElementById('task-list').appendChild(taskItem);
    });
}

// Filtra as tarefas
function filterTasks(status) {
    const tasks = document.querySelectorAll('#task-list li');
    tasks.forEach(task => {
        switch(status) {
            case 'all':
                task.style.display = 'flex';
                break;
            case 'completed':
                task.style.display = task.classList.contains('completed') ? 'flex' : 'none';
                break;
            case 'pending':
                task.style.display = task.classList.contains('completed') ? 'none' : 'flex';
                break;
        }
    });
}