package com.minhtriet.se3979.orderservice.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;
import java.time.LocalDateTime;

@Entity
@Table(name = "outbox_event")
@Data
public class OutboxEvent {
    @Id
    private String id;
    private String aggregateType;
    private String aggregateId;
    private String type;
    private String payload;
    private LocalDateTime createdAt;
    private String status; // PENDING, PUBLISHED
}
