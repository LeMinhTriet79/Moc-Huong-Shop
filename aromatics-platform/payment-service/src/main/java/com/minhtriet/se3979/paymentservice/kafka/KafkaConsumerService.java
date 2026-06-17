package com.minhtriet.se3979.paymentservice.kafka;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class KafkaConsumerService {

    @KafkaListener(topics = "order-created", groupId = "payment-group")
    public void consumeOrderCreated(String message) {
        log.info("PaymentService received order-created event: {}", message);
        // Logic to create a pending payment record
    }
}
