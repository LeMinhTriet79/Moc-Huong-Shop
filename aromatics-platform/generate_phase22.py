import os

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"
config_server_dir = f"{base_platform}/config-server"
os.makedirs(f"{config_server_dir}/src/main/java/com/minhtriet/se3979/configserver", exist_ok=True)
os.makedirs(f"{config_server_dir}/src/main/resources/config", exist_ok=True)

# 1. Create pom.xml
pom_content = """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.1</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.minhtriet.se3979</groupId>
    <artifactId>config-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>config-server</name>
    <description>Config Server for Aromatics Platform</description>
    <properties>
        <java.version>21</java.version>
        <spring-cloud.version>2023.0.0</spring-cloud.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-config-server</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
"""
with open(f"{config_server_dir}/pom.xml", "w", encoding="utf-8") as f:
    f.write(pom_content)

# 2. Create Application class
app_content = """package com.minhtriet.se3979.configserver;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.config.server.EnableConfigServer;

@SpringBootApplication
@EnableConfigServer
public class ConfigServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigServerApplication.class, args);
    }
}
"""
with open(f"{config_server_dir}/src/main/java/com/minhtriet/se3979/configserver/ConfigServerApplication.java", "w", encoding="utf-8") as f:
    f.write(app_content)

# 3. Create application.yml
yml_content = """server:
  port: 8888

spring:
  application:
    name: config-server
  profiles:
    active: native
  cloud:
    config:
      server:
        native:
          search-locations: classpath:/config
"""
with open(f"{config_server_dir}/src/main/resources/application.yml", "w", encoding="utf-8") as f:
    f.write(yml_content)

# Create a sample config file for another service to demonstrate
with open(f"{config_server_dir}/src/main/resources/config/identity-service.yml", "w", encoding="utf-8") as f:
    f.write("custom:\n  message: Hello from Config Server\n")

# Update root pom.xml to include config-server as a module
root_pom = f"{base_platform}/pom.xml"
if os.path.exists(root_pom):
    with open(root_pom, "r", encoding="utf-8") as f:
        root_content = f.read()
    if "<module>config-server</module>" not in root_content:
        root_content = root_content.replace(
            "</modules>",
            "    <module>config-server</module>\n    </modules>"
        )
        with open(root_pom, "w", encoding="utf-8") as f:
            f.write(root_content)

print("Phase 22 Config Server logic generated.")
