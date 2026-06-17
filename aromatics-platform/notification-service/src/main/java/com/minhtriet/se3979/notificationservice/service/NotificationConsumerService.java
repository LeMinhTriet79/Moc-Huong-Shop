package com.minhtriet.se3979.notificationservice.service;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;
import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class NotificationConsumerService {

    @KafkaListener(topics = "order-events", groupId = "notification-group")
    public void consumeOrderEvent(String message) {
        log.info("Received order event: {}", message);
        // send email
    }

    @KafkaListener(topics = "user-events", groupId = "notification-group")
    public void consumeUserEvent(String message) {
        log.info("Received user event: {}", message);
        // send email
    }
}
