package com.hrportal.portal.repository;

import com.hrportal.portal.entity.Employee;
import com.hrportal.portal.entity.User;
import jakarta.transaction.Transactional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface EmpRepository extends JpaRepository<Employee,Long> {
    @Query("Select e from Employee e ORDER BY e.empId ASC")
    List<Employee> fetchAll();


    @Modifying
    @Transactional
    void deleteByEmpId(Long empId);

    Employee findByEmpId(Long empId);
}