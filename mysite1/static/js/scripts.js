btn_list = document.getElementsByClassName('edit_btn')
for (var i = 0; i < btn_list.length; i++) {
    btn_id = btn_list[i].id
    btn_list[i].addEventListener("click", function () {
        edit_forms = document.getElementsByClassName('edit_form')
        for (var i = 0; i < edit_forms.length; i++) {
            edit_forms[i].style.display = 'none'
        }
        form_id = 'edit_form_' + this.id.slice(9, this.id.length)
        document.getElementById(form_id).style.display = 'block'
    });
}
tasks = document.getElementsByClassName('task')
console.log(tasks);
for (var i = 0; i < tasks.length; i++) {
    tasks[i].addEventListener("click", function () {
        task_id = 'task_details_' + this.id.slice(5, this.id.length)
        task = document.getElementById(task_id)
        if (task.style.display === 'block') {
            task.style.display = 'none'
        }
        else {
            task.style.display = 'block'
        }
    });
}