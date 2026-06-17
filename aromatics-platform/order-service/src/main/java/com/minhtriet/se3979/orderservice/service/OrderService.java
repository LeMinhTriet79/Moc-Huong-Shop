package com.minhtriet.se3979.orderservice.service;
import com.minhtriet.se3979.orderservice.dto.request.OrderRequest;
import com.minhtriet.se3979.orderservice.dto.response.OrderResponse;
public interface OrderService {
    OrderResponse createOrder(OrderRequest request);
    OrderResponse getOrderById(Long id);
}
