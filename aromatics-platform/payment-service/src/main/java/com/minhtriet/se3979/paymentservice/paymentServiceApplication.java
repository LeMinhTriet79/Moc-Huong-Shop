package com.minhtriet.se3979.paymentservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@EnableDiscoveryClient
@SpringBootApplication
public class paymentServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(paymentServiceApplication.class, args);
    }

}
