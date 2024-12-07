const TaskManager = {
    tasks: JSON.parse(localStorage.getItem("tasks")) || [],

    saveTasks: function () {
        localStorage.setItem("tasks", JSON.stringify(this.tasks));
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

    deleteTask: function (index) {
        if (confirm("Tem certeza que deseja excluir esta tarefa?")) {
            this.tasks.splice(index, 1);
            this.saveTasks();
            this.renderTasks();
        }
    },

    toggleComplete: function (index) {
        this.tasks[index].completed = !this.tasks[index].completed;
        this.saveTasks();
        this.renderTasks();
    },

    filterTasks: function (type) {
        document.querySelectorAll(".filters button").forEach((button) => button.classList.remove("active-filter"));
        document.getElementById(`filter-${type}`).classList.add("active-filter");
        this.renderTasks(type);
    },

    clearTasks: function () {
        if (confirm("Tem certeza que deseja limpar todas as tarefas?")) {
            this.tasks = [];
            this.saveTasks();
            this.renderTasks();
        }
    },

    renderTasks: function (filter = "all") {
        const taskList = document.getElementById("task-list");
        taskList.innerHTML = "";

        const filteredTasks = this.tasks.filter((task) =>
            filter === "all"
                ? true
                : filter === "completed"
                ? task.completed
                : !task.completed
        );

        filteredTasks.forEach((task, index) => {
            const li = document.createElement("li");
            li.className = "task-added";

            const textSpan = document.createElement("span");
            textSpan.textContent = task.text;
            textSpan.ondblclick = () => this.editTask(index);
            if (task.completed) {
                textSpan.style.textDecoration = "line-through";
            }

            const deleteBtn = document.createElement("button");
            deleteBtn.textContent = "Excluir";
            deleteBtn.onclick = () => this.deleteTask(index);

            const completeBtn = document.createElement("button");
            completeBtn.textContent = task.completed ? "Desfazer" : "Concluir";
            completeBtn.onclick = () => this.toggleComplete(index);

            li.appendChild(textSpan);
            li.appendChild(completeBtn);
            li.appendChild(deleteBtn);

            taskList.appendChild(li);
        });
    },

    editTask: function (index) {
        const newText = prompt("Edite a tarefa:", this.tasks[index].text);
        if (newText) {
            this.tasks[index].text = newText.trim();
            this.saveTasks();
            this.renderTasks();
        }
    },
};

function updateCharacterCount() {
    const input = document.getElementById("new-task");
    const maxLength = input.maxLength;
    document.getElementById("char-count").textContent = `${maxLength - input.value.length} caracteres restantes.`;
}

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

document.addEventListener("DOMContentLoaded", () => TaskManager.renderTasks());
