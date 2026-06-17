package com.minhtriet.se3979.orderservice.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@FeignClient(name = "payment-service", path = "/api/payment")
public interface PaymentClient {
    @PostMapping("/transactions")
    Object createTransaction(@RequestBody Object transactionRequest);
}
