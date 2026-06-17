package com.minhtriet.se3979.orderservice.repository;

import com.minhtriet.se3979.orderservice.entity.OrderItem;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface OrderItemRepository extends JpaRepository<OrderItem, Long> {
}
