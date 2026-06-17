package com.minhtriet.se3979.cartservice.repository;

import com.minhtriet.se3979.cartservice.entity.Cart;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CartRedisRepository extends CrudRepository<Cart, String> {
}
