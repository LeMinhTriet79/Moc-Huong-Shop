package com.minhtriet.se3979.paymentservice.repository;

import com.minhtriet.se3979.paymentservice.entity.PaymentMethod;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PaymentMethodRepository extends JpaRepository<PaymentMethod, Long> {
}
