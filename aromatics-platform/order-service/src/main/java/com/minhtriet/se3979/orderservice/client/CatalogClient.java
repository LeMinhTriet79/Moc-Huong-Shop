package com.minhtriet.se3979.orderservice.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient(name = "catalog-service", path = "/api/catalog")
public interface CatalogClient {
    @GetMapping("/products/{id}")
    Object getProductById(@PathVariable("id") Long id);
}
