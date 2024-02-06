// // your_app/static/js/main.js

// document.addEventListener('DOMContentLoaded', function () {
//     // Your JavaScript code goes here
    
//     // Example: Show an alert on page load
//     alert('Welcome to the website!');

//     // Example: Add click event listener to a button
//     const loginButton = document.getElementById('loginButton');
//     if (loginButton) {
//         loginButton.addEventListener('click', function () {
//             // Your login functionality goes here
//             alert('User clicked the login button!');
//         });
//     }

//     // Example: Book Appointment
//     const bookAppointmentButton = document.getElementById('bookAppointmentButton');
//     if (bookAppointmentButton) {
//         bookAppointmentButton.addEventListener('click', function () {
//             // Your appointment booking functionality goes here
//             alert('User clicked the book appointment button!');
//         });
//     }
// });
// User Authentication and Registration

// User Registration
function registerUser() {
    const username = document.getElementById('registration-username').value;
    const email = document.getElementById('registration-email').value;
    const password = document.getElementById('registration-password').value;

    // Validate input fields (you may add more validation as needed)

    // Send AJAX request to Django view for registration
    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle registration success or failure
        if (data.success) {
            alert('Registration successful! Please log in.');
            // Redirect to login page or update UI accordingly
        } else {
            alert('Registration failed. Please try again.');
            // Handle error and update UI accordingly
        }
    })
    .catch(error => {
        console.error('Error during registration:', error);
    });
}

// User Login
function loginUser() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    // Validate input fields (you may add more validation as needed)

    // Send AJAX request to Django view for login
    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle login success or failure
        if (data.success) {
            alert('Login successful!');            
            // Redirect to home page or update UI accordingly
        } else {
            alert('Login failed. Please check your credentials.');
            // Handle error and update UI accordingly
        }
    })
    .catch(error => {
        console.error('Error during login:', error);
    });
}

// User Logout
function logoutUser() {
    // Send AJAX request to Django view for logout
    fetch('/logout/', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        // Handle logout success or failure
        if (data.success) {
            alert('Logout successful!');
            // Redirect to login page or update UI accordingly
        } else {
            alert('Logout failed. Please try again.');
            // Handle error and update UI accordingly
        }
    })
    .catch(error => {
        console.error('Error during logout:', error);
    });
}

// Profile Management

function updateProfile() {
    const firstName = document.getElementById('profile-firstname').value;
    const lastName = document.getElementById('profile-lastname').value;
    const email = document.getElementById('profile-email').value;

    // Validate input fields (you may add more validation as needed)

    // Send AJAX request to Django view for updating profile
    fetch('/update_profile/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ firstName, lastName, email }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle profile update success or failure
        if (data.success) {
            alert('Profile updated successfully!');
            // Update UI or redirect as needed
        } else {
            alert('Profile update failed. Please try again.');
            // Handle error and update UI accordingly
        }
    })
    .catch(error => {
        console.error('Error during profile update:', error);
    });
}

// Health Data Tracking

function trackHealthData() {
    const weight = document.getElementById('health-weight').value;
    const height = document.getElementById('health-height').value;
    const bloodPressure = document.getElementById('health-blood-pressure').value;

    // Validate input fields (you may add more validation as needed)

    // Send AJAX request to Django view for tracking health data
    fetch('/track_health_data/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ weight, height, bloodPressure }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle health data tracking success or failure
        if (data.success) {
            alert('Health data tracked successfully!');
            // Update UI or redirect as needed
        } else {
            alert('Health data tracking failed. Please try again.');
            // Handle error and update UI accordingly
        }
    })
    .catch(error => {
        console.error('Error during health data tracking:', error);
    });
}

// AI-Driven Personalization (Machine Learning)

function personalizeContent() {
    // Send AJAX request to Django view to get personalized content
    fetch('/personalize_content/')
    .then(response => response.json())
    .then(data => {
        // Handle personalized content retrieval
        console.log('Personalized content:', data.content);
        // Update UI with personalized content as needed
    })
    .catch(error => {
        console.error('Error during personalized content retrieval:', error);
    });
}

// Doctors Information and Appointment Booking

function getDoctorsList() {
    // Send AJAX request to Django view to get doctors' information
    fetch('/get_doctors_list/')
    .then(response => response.json())
    .then(data => {
        // Handle doctors' information retrieval
        console.log('Doctors list:', data.doctors);
        // Update UI with doctors' information as needed
    })
    .catch(error => {
        console.error('Error during doctors\' information retrieval:', error);
    });
}

function bookAppointment(doctorId, appointmentDate) {
    // Send AJAX request to Django view to book an appointment
    fetch('/book_appointment/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ doctorId, appointmentDate }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle appointment booking success or failure
        if (data.success) {
            alert('Appointment booked successfully!');
            // Update UI or redirect as needed
        } else {
            alert('Appointment booking failed. Please try again.');
            // Handle error and update UI accordingly
        }
    })
    .catch(error => {
        console.error('Error during appointment booking:', error);
    });
}

// Blogs (Related to Health Care)

function loadHealthBlogs() {
    // Send AJAX request to Django view to get blog posts
    fetch('/get_health_blogs/')
    .then(response => response.json())
    .then(data => {
        // Handle blog posts retrieval
        console.log('Health blogs:', data.blogs);
        // Update UI with blog posts as needed
    })
    .catch(error => {
        console.error('Error during health blogs retrieval:', error);
    });
}




