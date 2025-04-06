package com.hrportal.portal.controllers;

import com.hrportal.portal.entity.Employee;
import com.hrportal.portal.entity.User;
import com.hrportal.portal.repository.EmpRepository;
import com.hrportal.portal.repository.UserRepository;
import jakarta.servlet.http.HttpSession;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.swing.text.html.Option;
import java.util.List;
import java.util.Optional;


@RestController
@RequestMapping("/employees")
@CrossOrigin(origins = {"http://127.0.0.1:5500","http://localhost:5500"},allowCredentials = "true")
public class EmpController {

    private EmpRepository empRepository;
    private UserRepository userRepository;

    public EmpController(EmpRepository empRepository,UserRepository userRepository){
        this.empRepository = empRepository;
        this.userRepository = userRepository;
    }

    @PostMapping("/add")
    public ResponseEntity<String> addEmp(@RequestBody Employee employee){
        empRepository.save(employee);
        return ResponseEntity.ok("Employee added successfully.");
    }


    @GetMapping("/fetchEmployees")
    public ResponseEntity<?> fetchEmp(){
        List<Employee> list = empRepository.fetchAll();
        return ResponseEntity.ok(list);
    }

    @GetMapping("/fetchEmployees/{id}")
    public ResponseEntity<?> fetchEmp(@PathVariable Long id){
        Employee emp = empRepository.findByEmpId(id);
        return ResponseEntity.ok(emp);
    }

    @PutMapping("/editemp/{id}")
    public ResponseEntity<String> edit(@PathVariable Long id, @RequestBody Employee updatedEmployee) {
        Optional<Employee> optionalEmp = empRepository.findById(id);

        if (optionalEmp.isPresent()) {
            Employee existingEmp = optionalEmp.get();

            existingEmp.setName(updatedEmployee.getName());
            existingEmp.setDepartment(updatedEmployee.getDepartment());
            existingEmp.setEmail(updatedEmployee.getEmail());
            existingEmp.setSalary(updatedEmployee.getSalary());

            empRepository.save(existingEmp);
            return ResponseEntity.ok("Employee updated successfully.");
        } else {
            return ResponseEntity.badRequest().body("Employee not found.");
        }
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<String> delete(@PathVariable Long id){
        empRepository.deleteByEmpId(id);
        return ResponseEntity.ok("DELETED EMPLOYEE");
    }

}
