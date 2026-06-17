package com.minhtriet.se3979.cartservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@EnableDiscoveryClient
@SpringBootApplication
public class cartServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(cartServiceApplication.class, args);
    }

}
