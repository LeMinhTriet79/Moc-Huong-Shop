package com.minhtriet.se3979.orderservice.scheduler;

import com.minhtriet.se3979.orderservice.entity.OutboxEvent;
import com.minhtriet.se3979.orderservice.repository.OutboxEventRepository;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class OutboxEventRelay {

    private final OutboxEventRepository repository;
    private final KafkaTemplate<String, Object> kafkaTemplate;

    public OutboxEventRelay(OutboxEventRepository repository, KafkaTemplate<String, Object> kafkaTemplate) {
        this.repository = repository;
        this.kafkaTemplate = kafkaTemplate;
    }

    @Scheduled(fixedDelay = 5000)
    public void relayEvents() {
        List<OutboxEvent> pendingEvents = repository.findByStatus("PENDING");
        for (OutboxEvent event : pendingEvents) {
            try {
                // Publish to Kafka
                kafkaTemplate.send(event.getAggregateType() + "-events", event.getPayload());
                
                // Mark as published
                event.setStatus("PUBLISHED");
                repository.save(event);
            } catch (Exception e) {
                // Log and retry later
                System.err.println("Failed to publish event: " + event.getId());
            }
        }
    }
}
