import tkinter as tk
from tkinter import messagebox


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tasks = []

        # Configuração do rótulo para entrada de tarefa
        self.label_tarefa = tk.Label(self.root, text="Digite a tarefa:")
        self.label_tarefa.grid(row=0, column=0, padx=10, pady=10)

        # Configuração da entrada de tarefa
        self.entry_tarefa = tk.Entry(self.root)
        self.entry_tarefa.grid(row=0, column=1, padx=10, pady=10)

        # Botão para adicionar tarefa
        self.botao_adicionar = tk.Button(
            self.root, text="Adicionar Tarefa", command=self.add_task)
        self.botao_adicionar.grid(row=0, column=2, padx=10, pady=10)

        # Listbox para exibir tarefas
        self.listbox_tarefas = tk.Listbox(self.root, height=10, width=50)
        self.listbox_tarefas.grid(
            row=1, column=0, columnspan=3, padx=10, pady=10)

        # Botão para remover tarefa
        self.botao_remover = tk.Button(
            self.root, text="Remover Tarefa", command=self.remove_task)
        self.botao_remover.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10)

    def add_task(self):
        task = self.entry_tarefa.get().strip()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.entry_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Entrada inválida", "Digite uma tarefa válida.")

    def remove_task(self):
        try:
            selected_task_index = self.listbox_tarefas.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning(
                "Seleção inválida", "Selecione uma tarefa para remover.")

    def update_tasks_listbox(self):
        self.listbox_tarefas.delete(0, tk.END)
        for task in self.tasks:
            self.listbox_tarefas.insert(tk.END, task)


# Executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
