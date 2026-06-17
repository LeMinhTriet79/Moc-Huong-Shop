import os

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"

kafka_config_dir = f"{base_platform}/notification-service/src/main/java/com/minhtriet/se3979/notificationservice/config"
os.makedirs(kafka_config_dir, exist_ok=True)

kafka_config_content = """package com.minhtriet.se3979.notificationservice.config;

import org.apache.kafka.common.TopicPartition;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.listener.DeadLetterPublishingRecoverer;
import org.springframework.kafka.listener.DefaultErrorHandler;
import org.springframework.util.backoff.FixedBackOff;

@Configuration
public class KafkaConfig {

    @Bean
    public DefaultErrorHandler errorHandler(KafkaTemplate<Object, Object> template) {
        DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(template,
                (r, e) -> new TopicPartition(r.topic() + ".DLT", r.partition()));
        // Retry 3 times with 1 second delay before sending to DLQ
        return new DefaultErrorHandler(recoverer, new FixedBackOff(1000L, 3L));
    }
}
"""

with open(f"{kafka_config_dir}/KafkaConfig.java", "w", encoding="utf-8") as f:
    f.write(kafka_config_content)

print("Phase 19 Kafka DLQ logic generated.")
