// function showTodo(todo: {title: string, text: string}) {
//     console.log(todo.title+': '+todo.text);
// }

let myTodo = {title: 'Trash', text: 'Take out trash'};


interface Todo{
    title: string;
    text: string;
}

function showTodo(todo: Todo) {
    console.log(todo.title+ ': '+ todo.text);
}


showTodo(myTodo);
