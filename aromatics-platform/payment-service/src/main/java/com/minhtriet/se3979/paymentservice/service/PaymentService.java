package com.minhtriet.se3979.paymentservice.service;
import com.minhtriet.se3979.paymentservice.entity.Transaction;
import com.minhtriet.se3979.paymentservice.repository.TransactionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class PaymentService {
    @Autowired
    private TransactionRepository transactionRepository;

    public List<Transaction> getAllTransactions() {
        return transactionRepository.findAll();
    }
}
