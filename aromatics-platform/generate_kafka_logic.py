import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"

# --- ORDER SERVICE ---
order_kafka = f"{base_platform}/order-service/src/main/java/com/minhtriet/se3979/orderservice/kafka/KafkaProducerService.java"
create_file(order_kafka, """package com.minhtriet.se3979.orderservice.kafka;
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
        String message = String.format("{\\"orderId\\":%d, \\"userId\\":%d, \\"totalAmount\\":%f}", orderId, userId, totalAmount.doubleValue());
        kafkaTemplate.send("order-created", message);
    }
}
""")

# Update OrderServiceImpl to use KafkaProducerService
order_impl = f"{base_platform}/order-service/src/main/java/com/minhtriet/se3979/orderservice/service/impl/OrderServiceImpl.java"
with open(order_impl, "r", encoding="utf-8") as f:
    order_content = f.read()

if "KafkaProducerService kafkaProducerService" not in order_content:
    order_content = order_content.replace(
        "private final OrderRepository orderRepository;",
        "private final OrderRepository orderRepository;\n    private final com.minhtriet.se3979.orderservice.kafka.KafkaProducerService kafkaProducerService;"
    )
    order_content = order_content.replace(
        "order = orderRepository.save(order);",
        "order = orderRepository.save(order);\n        kafkaProducerService.publishOrderCreated(order.getId(), order.getUserId(), order.getTotalAmount());"
    )
    with open(order_impl, "w", encoding="utf-8") as f:
        f.write(order_content)

# --- PAYMENT SERVICE ---
payment_kafka = f"{base_platform}/payment-service/src/main/java/com/minhtriet/se3979/paymentservice/kafka/KafkaConsumerService.java"
create_file(payment_kafka, """package com.minhtriet.se3979.paymentservice.kafka;
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
""")

# --- NOTIFICATION SERVICE ---
notification_kafka = f"{base_platform}/notification-service/src/main/java/com/minhtriet/se3979/notificationservice/kafka/KafkaConsumerService.java"
create_file(notification_kafka, """package com.minhtriet.se3979.notificationservice.kafka;
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
""")

print("Kafka logic generated successfully.")
