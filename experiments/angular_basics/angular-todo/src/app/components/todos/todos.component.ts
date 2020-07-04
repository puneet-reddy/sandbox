import { Component, OnInit } from '@angular/core';
import { Todo } from '../../models/todo';
import { TodoService } from '../../services/todo.service';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.scss']
})
export class TodosComponent implements OnInit {

  todos: Todo[];

  constructor(private todoService: TodoService) { }

  ngOnInit() {
    this.todoService.getTodos(5).subscribe((data) => {
      this.todos = data;
    });
  }

  deleteTodo(todo: Todo) {
    // Delete from UI
    this.todos = this.todos.filter(t => t.id !== todo.id);
    // Delete from Server
    this.todoService.deleteTodo(todo).subscribe();
  }

  addTodo(todo: Todo) {
    this.todoService.addTodo(todo).subscribe(new_todo => {
      this.todos.push(new_todo);
    });
  }
}
