from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Base, Task, engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

class TaskCreate(BaseModel):  # Define a Pydantic model
    task: str
    description: str

app = FastAPI()
backend_url = os.environ.get("BACKEND_URL", "localhost")
frontend_port = os.environ.get("FRONTEND_PORT", 4200)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"{backend_url}:{frontend_port}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks")
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(task=task_data.task, description=task_data.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    # This endpoint will match GET /tasks and return a list of tasks
    tasks = db.query(Task).all()
    return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    # This endpoint will match GET /tasks/1 (for example) and return a single task
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_str: str, description_str: str, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db_task.task = task_str
    db_task.description = description_str 
    
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return db_task

if __name__ == "__main__":
    backend_host = os.environ.get("BACKEND_HOST", "0.0.0.0")
    container_port = os.environ.get("CONTAINER_PORT", 80)
    uvicorn.run("main:app", host=backend_host, port=int(container_port), reload=True, log_level="debug", debug=True)