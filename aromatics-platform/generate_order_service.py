import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/order-service/src/main/java/com/minhtriet/se3979/orderservice"
packages = ["entity", "repository", "service", "controller", "dto"]

for p in packages:
    os.makedirs(os.path.join(base_dir, p), exist_ok=True)

entities = {
    "Order": """package com.minhtriet.se3979.orderservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "orders")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class Order {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long userId;
    private String orderNumber;
    private String status;
    private BigDecimal totalAmount;
    private BigDecimal shippingFee;
    private BigDecimal discountAmount;
    private String paymentMethod;
    private String shippingAddress;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
""",
    "OrderItem": """package com.minhtriet.se3979.orderservice.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;

@Entity
@Table(name = "order_items")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class OrderItem {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long orderId;
    private Long productId;
    private Long variantId;
    private String productName;
    private Integer quantity;
    private BigDecimal unitPrice;
    private BigDecimal totalPrice;
}
"""
}

for name, content in entities.items():
    with open(os.path.join(base_dir, "entity", f"{name}.java"), "w") as f:
        f.write(content)

for name in entities.keys():
    repo_content = f"""package com.minhtriet.se3979.orderservice.repository;

import com.minhtriet.se3979.orderservice.entity.{name};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {name}Repository extends JpaRepository<{name}, Long> {{
}}
"""
    with open(os.path.join(base_dir, "repository", f"{name}Repository.java"), "w") as f:
        f.write(repo_content)

service_content = """package com.minhtriet.se3979.orderservice.service;
import com.minhtriet.se3979.orderservice.entity.Order;
import com.minhtriet.se3979.orderservice.repository.OrderRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class OrderService {
    @Autowired
    private OrderRepository orderRepository;

    public List<Order> getAllOrders() {
        return orderRepository.findAll();
    }
}
"""

controller_content = """package com.minhtriet.se3979.orderservice.controller;
import com.minhtriet.se3979.orderservice.entity.Order;
import com.minhtriet.se3979.orderservice.service.OrderService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/order")
public class OrderController {
    @Autowired
    private OrderService orderService;

    @GetMapping
    public List<Order> getAllOrders() {
        return orderService.getAllOrders();
    }
}
"""

with open(os.path.join(base_dir, "service", "OrderService.java"), "w") as f:
    f.write(service_content)

with open(os.path.join(base_dir, "controller", "OrderController.java"), "w") as f:
    f.write(controller_content)

print("Order Service generated.")
