function deleteCollege(button) {
    var college_code = button.getAttribute('college-code');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this college?\nStudents and Courses under this College will also be deleted.")) {
        fetch(`/college/delete/${college_code}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });        
    }
}
function deleteCourse(button) {
    var course_code = button.getAttribute('course-code');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this course?")) {
        fetch(`/course/delete/${course_code}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });        
    }
}
function deleteStudent(button) {
    var stud_ID = button.getAttribute('student-id');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this student?")) {
        fetch(`/student/delete/${stud_ID}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });        
    }
}
function editStudent(studentID, firstName, lastName, gender, courseCode, yearLevel, imageUrl) {
    // Fill in the form fields with the student's information
    document.getElementById('editStudentID').value = studentID;
    document.getElementById('editFirstName').value = firstName;
    document.getElementById('editLastName').value = lastName;
    document.getElementById('editGender').value = gender;
    document.getElementById('editCourseCode').value = courseCode;
    document.getElementById('editYearLevel').value = yearLevel;

    // Show the edit form
    document.getElementById('editForm').style.display = 'block';
}

function cancelEdit() {
    // Hide the edit form
    document.getElementById('editForm').style.display = 'none';
}

