package com.minhtriet.se3979.orderservice.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient(name = "promotion-service", path = "/api/promotion")
public interface PromotionClient {
    @GetMapping("/coupons/{code}")
    Object getCouponByCode(@PathVariable("code") String code);
}
