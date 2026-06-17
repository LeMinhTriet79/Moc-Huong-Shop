package com.minhtriet.se3979.cartservice.service;
import com.minhtriet.se3979.cartservice.redis.CartRedisRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CartService {
    @Autowired
    private CartRedisRepository cartRedisRepository;
}
