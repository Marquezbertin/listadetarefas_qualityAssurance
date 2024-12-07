const TaskManager = {
    tasks: JSON.parse(localStorage.getItem("tasks")) || [],

    saveTasks: function () {
        localStorage.setItem("tasks", JSON.stringify(this.tasks));
    },

    renderTasks: function (filter = "all") {
        const taskList = document.getElementById("task-list");
        taskList.innerHTML = "";

        const filteredTasks = this.tasks.filter(task =>
            filter === "all" ? true :
            filter === "completed" ? task.completed :
            !task.completed
        );

        filteredTasks.forEach((task, index) => {
            const li = document.createElement("li");
            if (task.completed) li.classList.add("completed");

            const taskText = document.createElement("span");
            taskText.textContent = task.text;
            taskText.ondblclick = () => this.editTask(index);

            const completeBtn = document.createElement("button");
            completeBtn.textContent = task.completed ? "Desfazer" : "Concluir";
            completeBtn.onclick = () => this.toggleComplete(index);

            const deleteBtn = document.createElement("button");
            deleteBtn.textContent = "Excluir";
            deleteBtn.onclick = () => this.confirmDelete(index);

            li.appendChild(taskText);
            li.appendChild(completeBtn);
            li.appendChild(deleteBtn);

            taskList.appendChild(li);
        });
    },

    addTask: function () {
        const taskInput = document.getElementById("new-task");
        const taskText = taskInput.value.trim();

        if (!taskText) {
            alert("A tarefa não pode estar vazia.");
            return;
        }

        this.tasks.push({ text: taskText, completed: false });
        taskInput.value = "";
        updateCharacterCount();
        this.saveTasks();
        this.renderTasks();
    },

    editTask: function (index) {
        const newText = prompt("Edite a tarefa:", this.tasks[index].text);
        if (newText !== null) {
            this.tasks[index].text = newText.trim();
            this.saveTasks();
            this.renderTasks();
        }
    },

    toggleComplete: function (index) {
        this.tasks[index].completed = !this.tasks[index].completed;
        this.saveTasks();
        this.renderTasks();
    },

    confirmDelete: function (index) {
        if (confirm("Tem certeza que deseja excluir esta tarefa?")) {
            this.tasks.splice(index, 1);
            this.saveTasks();
            this.renderTasks();
        }
    },

    clearTasks: function () {
        if (confirm("Tem certeza que deseja limpar todas as tarefas?")) {
            this.tasks = [];
            this.saveTasks();
            this.renderTasks();
        }
    },

    filterTasks: function (filter) {
        document.querySelectorAll(".filters button").forEach(btn => btn.classList.remove("active-filter"));
        document.getElementById(`filter-${filter}`).classList.add("active-filter");
        this.renderTasks(filter);
    }
};

function updateCharacterCount() {
    const taskInput = document.getElementById("new-task");
    const remaining = taskInput.maxLength - taskInput.value.length;
    document.getElementById("char-count").textContent = `${remaining} caracteres restantes.`;
}

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

document.addEventListener("DOMContentLoaded", () => {
    TaskManager.renderTasks();

    document.getElementById("add-task-btn").addEventListener("click", () => TaskManager.addTask());
    document.getElementById("clear-tasks-btn").addEventListener("click", () => TaskManager.clearTasks());
    document.getElementById("dark-mode-toggle").addEventListener("click", toggleDarkMode);
});
