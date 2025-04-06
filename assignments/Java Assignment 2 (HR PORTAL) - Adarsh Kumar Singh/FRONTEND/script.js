const loginForm = document.getElementById("login-form");
const signupForm = document.getElementById("signup-form");
const toggleText = document.querySelector(".toggle-text");
const formTitle = document.getElementById("form-title");

toggleText.addEventListener("click", function (e) {
  e.preventDefault();

  const isLoginActive = loginForm.classList.contains("active");

  loginForm.classList.toggle("active");
  signupForm.classList.toggle("active");

  formTitle.textContent = isLoginActive ? "Sign Up" : "Login";
  toggleText.innerHTML = isLoginActive
    ? `Already have an account? <a href="#" id="toggle-link">Login</a>`
    : `Don't have an account? <a href="#" id="toggle-link">Sign Up</a>`;
});

let passShow = document.getElementById("showPass");

passShow.onclick = function (e) {
  e.preventDefault();

  let p = document.getElementById("signup-password");

  if (p.type == "password") {
    p.type = "text";
  } else {
    p.type = "password";
  }
};

let submitBtn = document.querySelector(".signup-btn");

submitBtn.onclick = async function (e) {
  e.preventDefault();
  let name = document.getElementById("signup-name");
  let email = document.getElementById("signup-email");
  let password = document.getElementById("signup-password");

  const data = {
    name: name.value,
    email: email.value,
    password: password.value,
  };

  try {
    const res = await fetch("http://localhost:8080/auth/signup", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const response = await res.text();

    if (res.ok) {
      alert("Signup Successful! Please Log in now");
    } else {
      alert("Please try again later");
    }
  } catch (error) {
    console.error;
    alert("SOME ERROR OCCURRED!", error);
  }
};

let loginBtn = document.querySelector(".login-btn");

loginBtn.onclick = async function (e) {
  e.preventDefault();

  let email = document.getElementById("login-email");
  let password = document.getElementById("login-password");

  try {
    const response = await fetch("http://localhost:8080/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({ email: email.value, password: password.value }),
    });

    const res = response.text();

    if (response.ok) {
      alert("LOGGED IN SUCCESSFULLY!", res);
      document.querySelector(".containerLog").style.display = "none";
      document.getElementById("dashboard").style.display = "flex";
      
    } else {
      alert("Something went wrong.", res);
    }
  } catch (error) {
    alert("SOMETHING WENT WRONG", error);
  }
};



async function loadEmployees() {
  const res = await fetch("http://localhost:8080/employees/fetchEmployees", {
    method: "GET",
    headers: {
      "Content-type": "application/json",
    },
  });

  if (!res.ok) {
    const errorText = await res.text();
    console.error("Failed to load employees:", res.status, errorText);
    alert("Failed to load employees: " + res.status);
    return;
  }
  const data = await res.json();

  const tbody = document.getElementById("employeeTableBody");
  tbody.innerHTML = "";

  data.forEach((emp) => {
    const row = document.createElement("tr");

    row.innerHTML = `
        <td>${emp.empId}</td>
        <td>${emp.name}</td>
        <td>${emp.department}</td>
        <td>${emp.salary}</td>
        <td>${emp.email}</td>
        <td><button onclick="editEmployee(${emp.empId})">Edit</button>
        <button onclick="deleteEmployee(${emp.empId})">Delete</button></td>
      `;

    tbody.appendChild(row);
  });
}

loadEmployees();

async function addemp(e) {
  
  e.preventDefault();
  let eid = document.getElementById("empid");
  let name = document.getElementById("name");
  let dept = document.getElementById("dept");
  let salary = document.getElementById("salary");
  let email = document.getElementById("email");
  let form = document.getElementById("employeeForm");

  const data = {
    empId : eid.value,
    department : dept.value,
    name: name.value,
    salary : salary.value,
    email : email.value
  };

  try {
    const response = await fetch("http://localhost:8080/employees/add", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(data)
    });

    let res = response.text();
    if(response.ok){
      alert("EMPLOYEE ADDED!");
      form.reset();
      loadEmployees();
    }
    else{
      alert("Something went wrong!",res);
    }
  } catch (error) {
    alert("SOME ERROR OCCURRED",error);
  }
}






async function editEmployee(id) {

    let eid = document.getElementById("edit-id"); 
    let name = document.getElementById("edit-name");
    let dept =  document.getElementById("edit-dept");
    let salary = document.getElementById("edit-salary");
    let email = document.getElementById("edit-email");

  try {
    const response = await fetch(`http://localhost:8080/employees/fetchEmployees/${id}`); 
    if (!response.ok) {
      throw new Error("Failed to fetch employee details");
    }

    const emp = await response.json();

    eid.value = emp.empId;
    name.value = emp.name;
    dept.value = emp.department;
    salary.value = emp.salary;
    email.value = emp.email;

    document.getElementById("editOverlay").style.display = "block";

  } catch (error) {
    alert("Error loading employee data: " + error.message);
  }
}


async function saveEmp(e){
  e.preventDefault();
  let eid = document.getElementById("edit-id"); 
  let name = document.getElementById("edit-name");
  let dept =  document.getElementById("edit-dept");
  let salary = document.getElementById("edit-salary");
  let email = document.getElementById("edit-email");

  let id = eid.value;
  const updatedData = {
    empId : eid.value,
    name : name.value,
    department : dept.value,
    salary : salary.value,
    email : email.value
  }

  try {
    const response = await fetch(`http://localhost:8080/employees/editemp/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(updatedData)
    });

    if (response.ok) {
      alert("Employee updated successfully.");
      loadEmployees();
      document.getElementById("editOverlay").style.display = "none";
    } else {
      const errorText = await response.text();
      alert("Failed to update employee: " + errorText);
    }
  } catch (error) {
    alert("Error occurred while updating employee: " + error.message);
  }
}

function cancelEdit(){
  document.getElementById("editOverlay").style.display = "none";
}


async function deleteEmployee(id){

  if(!confirm("ARE YOU SURE TO DELETE THE EMPLOYEE?")){
    return;
  }
  try{
    const response = await fetch(`http://localhost:8080/employees/delete/${id}`,{
      method : "DELETE"
    });

    if(response.ok){
      alert("DELETED EMPLOYEE!");
      loadEmployees();
    }
    else{
      alert("SOME ERROR OCCURRED");
    }
  }
  catch(error){
    alert("Something went wrong.",error.message);
  }
}