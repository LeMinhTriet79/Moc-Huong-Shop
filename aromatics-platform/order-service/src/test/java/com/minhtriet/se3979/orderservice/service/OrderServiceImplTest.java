package com.minhtriet.se3979.orderservice.service;

import com.minhtriet.se3979.orderservice.dto.request.OrderRequest;
import com.minhtriet.se3979.orderservice.dto.response.OrderResponse;
import com.minhtriet.se3979.orderservice.entity.Order;
import com.minhtriet.se3979.orderservice.repository.OrderRepository;
import com.minhtriet.se3979.orderservice.kafka.KafkaProducerService;
import com.minhtriet.se3979.orderservice.service.impl.OrderServiceImpl;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.math.BigDecimal;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class OrderServiceImplTest {

    @Mock
    private OrderRepository orderRepository;

    @Mock
    private KafkaProducerService kafkaProducerService;

    @InjectMocks
    private OrderServiceImpl orderService;

    @Test
    void testGetOrderById() {
        Order mockOrder = new Order();
        mockOrder.setId(1L);
        mockOrder.setUserId(100L);
        mockOrder.setTotalAmount(BigDecimal.valueOf(500.0));
        mockOrder.setStatus("PENDING");

        when(orderRepository.findById(1L)).thenReturn(Optional.of(mockOrder));

        OrderResponse response = orderService.getOrderById(1L);

        assertNotNull(response);
        assertEquals(1L, response.getId());
        assertEquals(100L, response.getUserId());
        verify(orderRepository, times(1)).findById(1L);
    }
}
