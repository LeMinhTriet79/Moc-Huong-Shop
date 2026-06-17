import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/payment-service/src/main/java/com/minhtriet/se3979/paymentservice"
packages = ["entity", "repository", "service", "controller", "dto"]

for p in packages:
    os.makedirs(os.path.join(base_dir, p), exist_ok=True)

entities = {
    "Transaction": """package com.minhtriet.se3979.paymentservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "transactions")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Transaction {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String transactionId;
    private Long orderId;
    private BigDecimal amount;
    private String paymentMethod;
    private String status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
""",
    "PaymentMethod": """package com.minhtriet.se3979.paymentservice.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "payment_methods")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class PaymentMethod {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String code;
    private String name;
    private Boolean isActive;
}
"""
}

for name, content in entities.items():
    with open(os.path.join(base_dir, "entity", f"{name}.java"), "w") as f:
        f.write(content)

for name in entities.keys():
    repo_content = f"""package com.minhtriet.se3979.paymentservice.repository;

import com.minhtriet.se3979.paymentservice.entity.{name};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {name}Repository extends JpaRepository<{name}, Long> {{
}}
"""
    with open(os.path.join(base_dir, "repository", f"{name}Repository.java"), "w") as f:
        f.write(repo_content)

service_content = """package com.minhtriet.se3979.paymentservice.service;
import com.minhtriet.se3979.paymentservice.entity.Transaction;
import com.minhtriet.se3979.paymentservice.repository.TransactionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class PaymentService {
    @Autowired
    private TransactionRepository transactionRepository;

    public List<Transaction> getAllTransactions() {
        return transactionRepository.findAll();
    }
}
"""

controller_content = """package com.minhtriet.se3979.paymentservice.controller;
import com.minhtriet.se3979.paymentservice.entity.Transaction;
import com.minhtriet.se3979.paymentservice.service.PaymentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/payment")
public class PaymentController {
    @Autowired
    private PaymentService paymentService;

    @GetMapping("/transactions")
    public List<Transaction> getAllTransactions() {
        return paymentService.getAllTransactions();
    }
}
"""

with open(os.path.join(base_dir, "service", "PaymentService.java"), "w") as f:
    f.write(service_content)

with open(os.path.join(base_dir, "controller", "PaymentController.java"), "w") as f:
    f.write(controller_content)

print("Payment Service generated.")
