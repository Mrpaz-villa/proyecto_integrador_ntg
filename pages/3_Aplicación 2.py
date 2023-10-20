import streamlit as st
import todoist

# Reemplaza 'YOUR_API_KEY' con tu clave de API de Todoist
API_KEY = 'YOUR_API_KEY'

# Crear un cliente Todoist
api = todoist.TodoistAPI(API_KEY)

def list_tasks():
    # Obtener todas las tareas
    api.sync()
    tasks = api.state['items']
    
    st.subheader("Tareas pendientes:")
    for task in tasks:
        st.write(f"{task['id']}. {task['content']}")

def add_task(task_name):
    # Agregar una nueva tarea
    api.items.add(task_name)
    api.commit()

def complete_task(task_id):
    # Marcar una tarea como completada
    api.items.get_by_id(task_id).complete()
    api.commit()

def main():
    st.title("Aplicación de Tareas Pendientes")

    st.sidebar.header("Menú")
    choice = st.sidebar.radio("Selecciona una opción:", ["Listar tareas", "Agregar tarea", "Marcar tarea como completada"])

    if choice == "Listar tareas":
        list_tasks()
    elif choice == "Agregar tarea":
        task_name = st.text_input("Ingrese el nombre de la tarea:")
        if st.button("Agregar tarea"):
            add_task(task_name)
            st.success("Tarea agregada.")
    elif choice == "Marcar tarea como completada":
        task_id = st.number_input("Ingrese el ID de la tarea a marcar como completada:")
        if st.button("Marcar como completada"):
            complete_task(int(task_id))
            st.success("Tarea marcada como completada")

if __name__ == "__main__":
    main()
