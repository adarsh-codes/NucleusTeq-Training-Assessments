package com.hrportal.portal.controllers;


import com.hrportal.portal.config.PasswordConfig;
import com.hrportal.portal.entity.User;
import com.hrportal.portal.repository.UserRepository;

import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpSession;



import java.util.Optional;


@RestController
@RequestMapping("/auth")
@CrossOrigin(origins = {"http://127.0.0.1:5500","http://localhost:5500"})
public class AuthController {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;


    public AuthController(UserRepository userRepository, PasswordEncoder passwordEncoder){
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }



    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody User user){
        if(!userRepository.findByEmail(user.getEmail()).isPresent()){
            return ResponseEntity.badRequest().body("User not registered! Please Sign up.");
        }

        User found = userRepository.findByEmail(user.getEmail()).get();

        if(!passwordEncoder.matches(user.getPassword(),found.getPassword())){

            return ResponseEntity.badRequest().body("Invalid Password!");
        }



        return ResponseEntity.ok("Login successful! Welcome " + user.getEmail());
    }

    @PostMapping("/signup")
    public ResponseEntity<String> signup(@RequestBody User user){
        System.out.println("signup endpoint");
        if(userRepository.findByEmail(user.getEmail()).isPresent()){
            return ResponseEntity.badRequest().body("User already registered! Please Log In.");
        }

        User newuser = new User();
        newuser.setEmail(user.getEmail());
        newuser.setName(user.getName());
        newuser.setPassword(passwordEncoder.encode(user.getPassword()));

        userRepository.save(newuser);

        return ResponseEntity.ok("User registered successfully! Please log in.");
    }

}
