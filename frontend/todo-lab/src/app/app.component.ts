import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: true,
  imports: [HttpClientModule, CommonModule],
})
export class AppComponent implements OnInit {
  title = 'todo-app';
  tasks: any[] = [];
  private baseUrl = 'http://localhost:8000/tasks';

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.fetchTasks();
  }

  fetchTasks(): void {
    this.http.get<any[]>(this.baseUrl).subscribe(
      tasks => this.tasks = tasks,
      error => console.error('Error loading tasks', error)
    );
  }

  deleteTask(id: number): void {
    this.http.delete(`${this.baseUrl}/${id}`).subscribe(
      () => this.tasks = this.tasks.filter(task => task.id !== id),
      error => console.error('Error deleting task', error)
    );
  }

  addTask(event: Event, task: string, description: string): void {
    event.preventDefault(); // Prevent default form submission
    this.http.post<any>(this.baseUrl, { task, description }).subscribe(
      newTask => this.tasks.push(newTask),
      error => console.error('Error adding task', error)
    );
  }
}