import os
import re

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"

# 1. Add Jasypt dependency to identity-service
identity_pom = f"{base_platform}/identity-service/pom.xml"
jasypt_dep = """
        <dependency>
            <groupId>com.github.ulisesbocchio</groupId>
            <artifactId>jasypt-spring-boot-starter</artifactId>
            <version>3.0.5</version>
        </dependency>
"""
with open(identity_pom, "r", encoding="utf-8") as f:
    pom_content = f.read()

if "jasypt-spring-boot-starter" not in pom_content:
    pom_content = re.sub(r'(</dependencies>)', jasypt_dep + r'\1', pom_content, 1)
    with open(identity_pom, "w", encoding="utf-8") as f:
        f.write(pom_content)

# 2. Add Jasypt config class
config_dir = f"{base_platform}/identity-service/src/main/java/com/minhtriet/se3979/identityservice/config"
os.makedirs(config_dir, exist_ok=True)
jasypt_config = """package com.minhtriet.se3979.identityservice.config;

import org.jasypt.encryption.StringEncryptor;
import org.jasypt.encryption.pbe.PooledPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class JasyptConfig {

    @Bean(name = "jasyptStringEncryptor")
    public StringEncryptor getPasswordEncryptor() {
        PooledPBEStringEncryptor encryptor = new PooledPBEStringEncryptor();
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        // In real project, use environment variable for the secret key
        config.setPassword("mySecretKey"); 
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setPoolSize("1");
        config.setProviderName("SunJCE");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setStringOutputType("base64");
        encryptor.setConfig(config);
        return encryptor;
    }
}
"""
with open(f"{config_dir}/JasyptConfig.java", "w", encoding="utf-8") as f:
    f.write(jasypt_config)

# 3. Modify application.yml to use ENC()
yml_path = f"{base_platform}/identity-service/src/main/resources/application.yml"
with open(yml_path, "r", encoding="utf-8") as f:
    yml_content = f.read()

# E.g. replace password: root with password: ENC(xxx)
yml_content = re.sub(r'(password:\s*)(.*)', r'\1ENC(g6/fR0uV+R5qM5O2lT+w/w==)', yml_content)
with open(yml_path, "w", encoding="utf-8") as f:
    f.write(yml_content)

print("Phase 23 Jasypt logic generated.")
