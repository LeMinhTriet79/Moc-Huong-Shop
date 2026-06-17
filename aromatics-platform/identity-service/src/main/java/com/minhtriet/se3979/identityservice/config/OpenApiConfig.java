package com.minhtriet.se3979.identityservice.config;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.enums.SecuritySchemeType;
import io.swagger.v3.oas.annotations.info.Info;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.security.SecurityScheme;
import org.springframework.context.annotation.Configuration;

@Configuration
@OpenAPIDefinition(
        info = @Info(
                title = "Identity Service API - Mộc Hương",
                version = "1.0",
                description = "Tài liệu API cho dịch vụ quản lý danh tính (Identity Service)"
        ),
        // Áp dụng yêu cầu bảo mật này cho tất cả các API (nếu API nào không cần thì vẫn gọi bình thường)
        security = @SecurityRequirement(name = "bearerAuth")
)
@SecurityScheme(
        name = "bearerAuth",
        type = SecuritySchemeType.HTTP,
        scheme = "bearer",
        bearerFormat = "JWT",
        description = "Nhập Access Token của bạn vào đây (không cần thêm chữ Bearer)"
)
public class OpenApiConfig {
}