package com.minhtriet.se3979.orderservice.service.impl;
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
                .status(order.getStatus())
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
                .status(order.getStatus())
                .createdAt(order.getCreatedAt())
                .build();
    }
}
