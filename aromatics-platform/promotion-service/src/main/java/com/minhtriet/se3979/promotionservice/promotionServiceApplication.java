package com.minhtriet.se3979.promotionservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@EnableDiscoveryClient
@SpringBootApplication
public class promotionServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(promotionServiceApplication.class, args);
    }

}
