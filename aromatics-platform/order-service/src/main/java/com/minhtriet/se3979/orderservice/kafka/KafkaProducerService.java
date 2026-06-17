package com.minhtriet.se3979.orderservice.kafka;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class KafkaProducerService {
    private final KafkaTemplate<String, Object> kafkaTemplate;

    public void publishOrderCreated(Long orderId, Long userId, java.math.BigDecimal totalAmount) {
        log.info("Publishing order-created event for orderId: {}", orderId);
        // For simplicity, passing a map or custom object. Here we pass a String or object.
        String message = String.format("{\"orderId\":%d, \"userId\":%d, \"totalAmount\":%f}", orderId, userId, totalAmount.doubleValue());
        kafkaTemplate.send("order-created", message);
    }
}
