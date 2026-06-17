package com.minhtriet.se3979.cartservice.redis;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class CartRedisRepository {
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    // basic operations
}
