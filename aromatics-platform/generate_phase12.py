import os
import re

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"
services = {
    "identity-service": "com/minhtriet/se3979/identityservice",
    "catalog-service": "com/minhtriet/se3979/catalogservice",
    "cart-service": "com/minhtriet/se3979/cartservice",
    "order-service": "com/minhtriet/se3979/orderservice",
    "promotion-service": "com/minhtriet/se3979/promotionservice"
}

validation_dep = """
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
"""

for svc, pkg_path in services.items():
    # 1. Add validation dependency
    pom_path = f"{base_platform}/{svc}/pom.xml"
    with open(pom_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "spring-boot-starter-validation" not in content:
        content = re.sub(r'(</dependencies>)', validation_dep + r'\1', content, 1)
        with open(pom_path, "w", encoding="utf-8") as f:
            f.write(content)

    # 2. Add GlobalExceptionHandler
    exception_dir = f"{base_platform}/{svc}/src/main/java/{pkg_path}/exception"
    os.makedirs(exception_dir, exist_ok=True)
    
    pkg_name = pkg_path.replace('/', '.')
    
    with open(f"{exception_dir}/ErrorResponse.java", "w", encoding="utf-8") as f:
        f.write(f"""package {pkg_name}.exception;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class ErrorResponse {{
    private int status;
    private String message;
}}
""")

    with open(f"{exception_dir}/GlobalExceptionHandler.java", "w", encoding="utf-8") as f:
        f.write(f"""package {pkg_name}.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.stream.Collectors;

@RestControllerAdvice
public class GlobalExceptionHandler {{

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationExceptions(MethodArgumentNotValidException ex) {{
        String errors = ex.getBindingResult()
                .getFieldErrors()
                .stream()
                .map(error -> error.getField() + ": " + error.getDefaultMessage())
                .collect(Collectors.joining(", "));
        return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                .body(new ErrorResponse(HttpStatus.BAD_REQUEST.value(), errors));
    }}

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGeneralExceptions(Exception ex) {{
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(new ErrorResponse(HttpStatus.INTERNAL_SERVER_ERROR.value(), ex.getMessage()));
    }}
}}
""")

print("Phase 12 validation and exception logic generated.")
