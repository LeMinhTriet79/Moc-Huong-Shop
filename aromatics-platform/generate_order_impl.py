import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/order-service/src/main/java/com/minhtriet/se3979/orderservice"

os.makedirs(os.path.join(base_dir, "dto", "request"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "dto", "response"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "service", "impl"), exist_ok=True)

with open(os.path.join(base_dir, "dto", "request", "OrderRequest.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.orderservice.dto.request;
import lombok.*;
import java.util.List;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class OrderRequest {
    private Long userId;
    private Long addressId;
    private Long paymentMethodId;
    private String couponCode;
    private List<OrderItemRequest> items;
}
""")

with open(os.path.join(base_dir, "dto", "request", "OrderItemRequest.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.orderservice.dto.request;
import lombok.*;
import java.math.BigDecimal;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class OrderItemRequest {
    private Long productId;
    private Integer quantity;
    private BigDecimal price;
}
""")

with open(os.path.join(base_dir, "dto", "response", "OrderResponse.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.orderservice.dto.response;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;
@Getter @Setter @NoArgsConstructor @AllArgsConstructor @Builder
public class OrderResponse {
    private Long id;
    private Long userId;
    private BigDecimal totalAmount;
    private String status;
    private LocalDateTime createdAt;
}
""")

with open(os.path.join(base_dir, "service", "OrderService.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.orderservice.service;
import com.minhtriet.se3979.orderservice.dto.request.OrderRequest;
import com.minhtriet.se3979.orderservice.dto.response.OrderResponse;
public interface OrderService {
    OrderResponse createOrder(OrderRequest request);
    OrderResponse getOrderById(Long id);
}
""")

with open(os.path.join(base_dir, "service", "impl", "OrderServiceImpl.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.orderservice.service.impl;
import com.minhtriet.se3979.orderservice.dto.request.OrderRequest;
import com.minhtriet.se3979.orderservice.dto.response.OrderResponse;
import com.minhtriet.se3979.orderservice.entity.Order;

import com.minhtriet.se3979.orderservice.repository.OrderRepository;
import com.minhtriet.se3979.orderservice.service.OrderService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Service
@RequiredArgsConstructor
public class OrderServiceImpl implements OrderService {
    private final OrderRepository orderRepository;

    @Override
    public OrderResponse createOrder(OrderRequest request) {
        Order order = new Order();
        order.setUserId(request.getUserId());
        order.setShippingAddress("Address ID: " + request.getAddressId());
        order.setStatus("PENDING");
        
        BigDecimal total = BigDecimal.ZERO;
        if (request.getItems() != null) {
            for(var item : request.getItems()) {
                total = total.add(item.getPrice().multiply(BigDecimal.valueOf(item.getQuantity())));
            }
        }
        order.setTotalAmount(total);
        order.setDiscountAmount(BigDecimal.ZERO);
        
        order = orderRepository.save(order);

        return OrderResponse.builder()
                .id(order.getId())
                .userId(order.getUserId())
                .totalAmount(order.getTotalAmount())
                .status(order.getStatus().name())
                .createdAt(order.getCreatedAt() != null ? order.getCreatedAt() : LocalDateTime.now())
                .build();
    }

    @Override
    public OrderResponse getOrderById(Long id) {
        Order order = orderRepository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
        return OrderResponse.builder()
                .id(order.getId())
                .userId(order.getUserId())
                .totalAmount(order.getTotalAmount())
                .status(order.getStatus().name())
                .createdAt(order.getCreatedAt())
                .build();
    }
}
""")

with open(os.path.join(base_dir, "controller", "OrderController.java"), "w", encoding="utf-8") as f:
    f.write("""package com.minhtriet.se3979.orderservice.controller;
import com.minhtriet.se3979.orderservice.dto.request.OrderRequest;
import com.minhtriet.se3979.orderservice.dto.response.OrderResponse;
import com.minhtriet.se3979.orderservice.service.OrderService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/orders")
@RequiredArgsConstructor
public class OrderController {
    private final OrderService orderService;

    @PostMapping
    public ResponseEntity<OrderResponse> createOrder(@RequestBody OrderRequest request) {
        return ResponseEntity.ok(orderService.createOrder(request));
    }

    @GetMapping("/{id}")
    public ResponseEntity<OrderResponse> getOrder(@PathVariable Long id) {
        return ResponseEntity.ok(orderService.getOrderById(id));
    }
}
""")
print("Order service implementation completed.")
