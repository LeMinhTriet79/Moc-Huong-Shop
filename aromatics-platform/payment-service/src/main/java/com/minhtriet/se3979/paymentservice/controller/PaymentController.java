package com.minhtriet.se3979.paymentservice.controller;
import com.minhtriet.se3979.paymentservice.entity.Transaction;
import com.minhtriet.se3979.paymentservice.service.PaymentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/payment")
public class PaymentController {
    @Autowired
    private PaymentService paymentService;

    @GetMapping("/transactions")
    public List<Transaction> getAllTransactions() {
        return paymentService.getAllTransactions();
    }
}
