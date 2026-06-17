import os

kafka_config = """
  kafka:
    bootstrap-servers: localhost:9092
    producer:
      key-serializer: org.apache.kafka.common.serialization.StringSerializer
      value-serializer: org.springframework.kafka.support.serializer.JsonSerializer
    consumer:
      group-id: aromatics-group
      auto-offset-reset: earliest
      key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value-deserializer: org.springframework.kafka.support.serializer.JsonDeserializer
      properties:
        spring.json.trusted.packages: "*"
"""

services = ["order-service", "payment-service", "notification-service"]

for svc in services:
    yml_path = f"g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/{svc}/src/main/resources/application.yml"
    with open(yml_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "kafka:" not in content:
        with open(yml_path, "a", encoding="utf-8") as f:
            f.write(kafka_config)
        print(f"Added Kafka config to {svc}")
    else:
        print(f"Kafka config already exists in {svc}")
