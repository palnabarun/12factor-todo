from typing import List, Union

from fastapi import FastAPI, Response, status

from .models import Task, TaskBase, TaskCreate, TaskUpdate

api = FastAPI()


@api.get("/", response_model=List[Task])
def list(completed: Union[bool, None] = None) -> List[Task]:
    return Task.find_all(completed=completed)


@api.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create(task: TaskCreate) -> Task:
    return Task.create(task.description)


@api.get("/{id}", response_model=Task)
def get(id: int, response: Response) -> Task:
    task = Task.find(id=id)
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return

    return task


@api.put("/{id}", response_model=Task)
def update(id: int, _task: TaskUpdate, response: Response) -> Task:
    task = Task.find(id=id)
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return

    task.update(description=_task.description)

    return task


@api.put("/{id}/complete", response_model=Task)
def mark_complete(id: int, response: Response) -> Task:
    task = Task.find(id=id)
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return

    task.mark_complete()

    return task


@api.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, response: Response):
    task = Task.find(id=id)
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return

    task.delete()
