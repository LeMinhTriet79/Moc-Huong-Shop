package com.minhtriet.se3979.orderservice.service;
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
