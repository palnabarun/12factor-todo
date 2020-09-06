from typing import List, TypeVar

from pydantic import BaseModel
import web

from . import config

Task = TypeVar("Task")
db = web.database(
    dbn="postgres",
    db=config.DB_NAME,
    host=config.DB_HOST,
    port=config.DB_PORT,
    user=config.DB_USER,
    pw=config.DB_PASSWORD,
)


class TaskBase(BaseModel):
    description: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    completed: bool

    def update(self, description: str):
        self.description = description
        self.save()

    def mark_complete(self):
        self.completed = True
        self.save()

    def save(self):
        db.update(
            "task",
            where="id=$id",
            description=self.description,
            completed=self.completed,
            vars={"id": self.id},
        )

    def delete(self):
        db.delete("task", where="id=$id", vars={"id": self.id})

    @staticmethod
    def create(description: str) -> Task:
        _id = db.insert("task", description=description)
        return Task(id=_id, description=description, completed=False)

    @staticmethod
    def find_all(completed: bool) -> List[Task]:
        if completed is not None:
            results = db.where("task", completed=completed)
        else:
            results = db.where("task")

        return [
            Task(id=r.id, description=r.description, completed=r.completed)
            for r in results.list()
        ]

    @staticmethod
    def find(id: int) -> Task:
        results = db.where("task", id=id)
        if not results:
            return

        task = results[0]

        return Task(id=task.id, description=task.description, completed=task.completed)
