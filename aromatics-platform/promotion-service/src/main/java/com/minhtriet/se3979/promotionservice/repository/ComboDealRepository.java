package com.minhtriet.se3979.promotionservice.repository;

import com.minhtriet.se3979.promotionservice.entity.ComboDeal;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ComboDealRepository extends JpaRepository<ComboDeal, Long> {
}
