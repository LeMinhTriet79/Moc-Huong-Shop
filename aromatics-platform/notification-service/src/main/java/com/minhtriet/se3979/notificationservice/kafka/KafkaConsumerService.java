package com.minhtriet.se3979.notificationservice.kafka;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class KafkaConsumerService {

    @KafkaListener(topics = "order-created", groupId = "notification-group")
    public void consumeOrderCreated(String message) {
        log.info("NotificationService received order-created event: {}", message);
        // Logic to send email/SMS to user about the order
    }
    
    @KafkaListener(topics = "payment-completed", groupId = "notification-group")
    public void consumePaymentCompleted(String message) {
        log.info("NotificationService received payment-completed event: {}", message);
        // Logic to send payment confirmation
    }
}
