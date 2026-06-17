package com.minhtriet.se3979.paymentservice.repository;

import com.minhtriet.se3979.paymentservice.entity.Transaction;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TransactionRepository extends JpaRepository<Transaction, Long> {
}
