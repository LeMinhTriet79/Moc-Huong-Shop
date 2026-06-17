import os

base_dir = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform/order-service/src/main/java/com/minhtriet/se3979/orderservice"
os.makedirs(os.path.join(base_dir, "client"), exist_ok=True)

catalog_client = """package com.minhtriet.se3979.orderservice.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient(name = "catalog-service", path = "/api/catalog")
public interface CatalogClient {
    @GetMapping("/products/{id}")
    Object getProductById(@PathVariable("id") Long id);
}
"""

promotion_client = """package com.minhtriet.se3979.orderservice.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient(name = "promotion-service", path = "/api/promotion")
public interface PromotionClient {
    @GetMapping("/coupons/{code}")
    Object getCouponByCode(@PathVariable("code") String code);
}
"""

payment_client = """package com.minhtriet.se3979.orderservice.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@FeignClient(name = "payment-service", path = "/api/payment")
public interface PaymentClient {
    @PostMapping("/transactions")
    Object createTransaction(@RequestBody Object transactionRequest);
}
"""

with open(os.path.join(base_dir, "client", "CatalogClient.java"), "w") as f:
    f.write(catalog_client)

with open(os.path.join(base_dir, "client", "PromotionClient.java"), "w") as f:
    f.write(promotion_client)

with open(os.path.join(base_dir, "client", "PaymentClient.java"), "w") as f:
    f.write(payment_client)

print("Order Service Feign clients generated.")
