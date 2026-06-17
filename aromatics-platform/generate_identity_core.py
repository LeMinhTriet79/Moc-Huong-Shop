import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/identity-service/src/main/java/com/minhtriet/se3979/identityservice"

# DTOs
dto_dir = os.path.join(base_dir, "dto", "request")
os.makedirs(dto_dir, exist_ok=True)
with open(os.path.join(dto_dir, "RegisterRequest.java"), "w") as f:
    f.write("""package com.minhtriet.se3979.identityservice.dto.request;
import lombok.*;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class RegisterRequest {
    private String email;
    private String password;
    private String fullName;
}
""")
with open(os.path.join(dto_dir, "LoginRequest.java"), "w") as f:
    f.write("""package com.minhtriet.se3979.identityservice.dto.request;
import lombok.*;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class LoginRequest {
    private String email;
    private String password;
}
""")

resp_dir = os.path.join(base_dir, "dto", "response")
os.makedirs(resp_dir, exist_ok=True)
with open(os.path.join(resp_dir, "AuthResponse.java"), "w") as f:
    f.write("""package com.minhtriet.se3979.identityservice.dto.response;
import lombok.*;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class AuthResponse {
    private String accessToken;
    private String refreshToken;
    private UserResponse user;
}
""")

# AuthService
with open(os.path.join(base_dir, "service", "AuthService.java"), "w") as f:
    f.write("""package com.minhtriet.se3979.identityservice.service;

import com.minhtriet.se3979.identityservice.dto.request.LoginRequest;
import com.minhtriet.se3979.identityservice.dto.request.RegisterRequest;
import com.minhtriet.se3979.identityservice.dto.response.AuthResponse;
import com.minhtriet.se3979.identityservice.dto.response.UserResponse;
import com.minhtriet.se3979.identityservice.entity.User;
import com.minhtriet.se3979.identityservice.repository.UserRepository;
import com.minhtriet.se3979.identityservice.security.JwtUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthService {
    private final UserRepository userRepository;
    private final JwtUtil jwtUtil;

    public AuthResponse register(RegisterRequest request) {
        User user = new User();
        user.setEmail(request.getEmail());
        user.setFullName(request.getFullName());
        // Hash password normally here
        user.setPasswordHash(request.getPassword()); 
        user = userRepository.save(user);

        String token = jwtUtil.generateToken(user.getId(), user.getEmail());
        return AuthResponse.builder().accessToken(token).user(UserResponse.builder().id(user.getId()).email(user.getEmail()).fullName(user.getFullName()).build()).build();
    }

    public AuthResponse login(LoginRequest request) {
        User user = userRepository.findByEmail(request.getEmail()).orElseThrow(() -> new RuntimeException("User not found"));
        // Check password normally here
        String token = jwtUtil.generateToken(user.getId(), user.getEmail());
        return AuthResponse.builder().accessToken(token).user(UserResponse.builder().id(user.getId()).email(user.getEmail()).fullName(user.getFullName()).build()).build();
    }
}
""")

# AuthController
with open(os.path.join(base_dir, "controller", "AuthController.java"), "w") as f:
    f.write("""package com.minhtriet.se3979.identityservice.controller;

import com.minhtriet.se3979.identityservice.dto.request.LoginRequest;
import com.minhtriet.se3979.identityservice.dto.request.RegisterRequest;
import com.minhtriet.se3979.identityservice.dto.response.AuthResponse;
import com.minhtriet.se3979.identityservice.service.AuthService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/identity/auth")
@RequiredArgsConstructor
public class AuthController {
    private final AuthService authService;

    @PostMapping("/register")
    public ResponseEntity<AuthResponse> register(@RequestBody RegisterRequest request) {
        return ResponseEntity.ok(authService.register(request));
    }

    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody LoginRequest request) {
        return ResponseEntity.ok(authService.login(request));
    }
}
""")

print("Identity service core logic generated.")
