import Swal from 'sweetalert2';

document.addEventListener('DOMContentLoaded', function () {
  const taskForm = document.getElementById('taskCreateForm');

  if (taskForm) {
    taskForm.addEventListener('submit', function (event) {
      event.preventDefault();

      const form = this;
      const actionUrl = form.action;
      const formData = new FormData(form);

      fetch(actionUrl, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      })
        .then((response) =>
          response
            .json()
            .catch(() => ({ success: false, error: 'Invalid JSON response' }))
        )
        .then((data) => {
          if (data.success) {
            Swal({
              title: 'Success!',
              text: 'Task created successfully.',
              icon: 'success',
              confirmButtonText: 'OK'
            }).then(() => {
              window.location.href = '/tasks/';
            });

            form.reset();
          } else {
            let errorMessage = data.error || 'Something went wrong.';
            if (typeof data.error === 'object') {
              errorMessage = Object.values(data.error).join('\n');
            }

            Swal({
              title: 'Error!',
              text: errorMessage,
              icon: 'error',
              confirmButtonText: 'OK'
            });
          }
        })
        .catch((error) => {
          console.error('Fetch Error:', error);
          Swal({
            title: 'Error!',
            text: 'Something went wrong. Please try again.',
            icon: 'error',
            confirmButtonText: 'OK'
          });
        });
    });
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const previewButtons = document.querySelectorAll(
    '[data-modal-target="readTaskModal"]'
  );
  const modal = document.getElementById('readTaskModal');

  previewButtons.forEach((button) => {
    button.addEventListener('click', function () {
      const taskTitle = this.getAttribute('data-title');
      const taskDescription = this.getAttribute('data-description');
      const taskStatus = this.getAttribute('data-status');
      const taskPriority = this.getAttribute('data-priority');

      document.getElementById('modalTaskTitle').textContent = taskTitle;
      document.getElementById('modalTaskDescription').textContent =
        taskDescription;
      document.getElementById('modalTaskStatus').textContent = taskStatus;
      document.getElementById('modalTaskPriority').textContent = taskPriority;

      // Show the modal
      modal.classList.remove('hidden');
    });
  });

  // Close modal when clicking the close button
  document
    .querySelector('[data-modal-toggle="readTaskModal"]')
    .addEventListener('click', function () {
      modal.classList.add('hidden');
    });
});

document.addEventListener('DOMContentLoaded', function () {
  const deleteButtons = document.querySelectorAll('.delete-task-btn');
  const deleteModal = document.getElementById('deleteModal');
  const closeModalButtons = document.querySelectorAll('.close-delete-modal');
  const deleteForm = document.getElementById('deleteForm');

  deleteButtons.forEach((button) => {
    button.addEventListener('click', function () {
      const taskId = this.getAttribute('data-id');
      deleteForm.action = `/tasks/delete/${taskId}/`;
      deleteModal.classList.remove('hidden');
    });
  });

  closeModalButtons.forEach((button) => {
    button.addEventListener('click', function () {
      deleteModal.classList.add('hidden');
    });
  });

  deleteForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission

    fetch(this.action, {
      method: 'POST',
      headers: {
        'X-CSRFToken': document.querySelector(
          'input[name="csrfmiddlewaretoken"]'
        ).value
      }
    })
      .then((response) => response.json())
      .then((data) => {
        deleteModal.classList.add('hidden');

        if (data.success) {
          Swal({
            title: 'Deleted!',
            text: 'The task has been removed.',
            icon: 'success',
            timer: 2000,
            showConfirmButton: false
          }).then(() => {
            window.location.reload();
          });
        } else {
          Swal({
            title: 'Error',
            text: 'Task deletion failed.',
            icon: 'error'
          });
        }
      })
      .catch(() => {
        Swal({
          title: 'Error',
          text: 'Something went wrong!',
          icon: 'error'
        });
      });
  });
});
