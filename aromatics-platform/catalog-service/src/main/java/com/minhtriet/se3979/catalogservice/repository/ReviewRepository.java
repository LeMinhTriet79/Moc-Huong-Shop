package com.minhtriet.se3979.catalogservice.repository;

import com.minhtriet.se3979.catalogservice.entity.Review;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ReviewRepository extends JpaRepository<Review, Long> {
}
