package com.hrportal.portal.entity;


import jakarta.persistence.*;

@Entity
@Table(name = "employee")
public class Employee{


    @Id
    private Long empId;
    private String name;

    private String department;

    @Column(nullable = false,unique = true)
    private String email;

    private Long salary;




    public String getEmail() {
        return email;
    }

    public Long getEmpId() {
        return empId;
    }

    public Long getSalary() {
        return salary;
    }

    public String getDepartment() {
        return department;
    }

    public String getName() {
        return name;
    }



    public void setEmail(String email) {
        this.email = email;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public void setEmpId(Long empId) {
        this.empId = empId;
    }

    public void setSalary(Long salary) {
        this.salary = salary;
    }


}