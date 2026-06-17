import os
import re

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"

# 1. Update Catalog Service dependencies
catalog_pom = f"{base_platform}/catalog-service/pom.xml"
security_dep = """
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>
"""
with open(catalog_pom, "r", encoding="utf-8") as f:
    pom_content = f.read()

if "spring-boot-starter-security" not in pom_content:
    pom_content = re.sub(r'(</dependencies>)', security_dep + r'\1', pom_content, 1)
    with open(catalog_pom, "w", encoding="utf-8") as f:
        f.write(pom_content)

# 2. Add SecurityConfig to Catalog Service
config_dir = f"{base_platform}/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice/config"
os.makedirs(config_dir, exist_ok=True)
config_content = """package com.minhtriet.se3979.catalogservice.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableMethodSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                .anyRequest().permitAll() // Allow all by default, restrict specific methods via annotations
            );
        return http.build();
    }
}
"""
with open(f"{config_dir}/SecurityConfig.java", "w", encoding="utf-8") as f:
    f.write(config_content)

# 3. Add @PreAuthorize to ProductController
controller_path = f"{base_platform}/catalog-service/src/main/java/com/minhtriet/se3979/catalogservice/controller/ProductController.java"
with open(controller_path, "r", encoding="utf-8") as f:
    ctrl_content = f.read()

if "import org.springframework.security.access.prepost.PreAuthorize;" not in ctrl_content:
    ctrl_content = ctrl_content.replace(
        "import org.springframework.web.bind.annotation.*;",
        "import org.springframework.web.bind.annotation.*;\nimport org.springframework.security.access.prepost.PreAuthorize;"
    )
    ctrl_content = ctrl_content.replace(
        "@PostMapping",
        '@PreAuthorize("hasRole(\'ADMIN\')")\n    @PostMapping'
    )
    with open(controller_path, "w", encoding="utf-8") as f:
        f.write(ctrl_content)

print("Phase 21 RBAC logic generated.")
