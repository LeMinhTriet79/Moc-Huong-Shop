package com.minhtriet.se3979.orderservice.repository;

import com.minhtriet.se3979.orderservice.entity.OutboxEvent;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface OutboxEventRepository extends JpaRepository<OutboxEvent, String> {
    List<OutboxEvent> findByStatus(String status);
}
