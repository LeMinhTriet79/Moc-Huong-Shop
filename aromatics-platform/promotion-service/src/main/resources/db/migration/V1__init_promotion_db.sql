-- 1. Coupons
CREATE TABLE coupons (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_type VARCHAR(20) NOT NULL,
    discount_value DECIMAL(15,2) NOT NULL,
    min_order_value DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    max_usages INT NOT NULL DEFAULT 1,
    start_date DATETIME(3) NOT NULL,
    end_date DATETIME(3) NOT NULL
);

-- 2. Flash Sales
CREATE TABLE flash_sales (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_id BIGINT UNSIGNED NOT NULL,
    discount_percentage INT NOT NULL,
    max_quantity INT NOT NULL,
    start_date DATETIME(3) NOT NULL,
    end_date DATETIME(3) NOT NULL
);

-- 3. Combo Deals
CREATE TABLE combo_deals (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    main_product_id BIGINT UNSIGNED NOT NULL,
    bundled_product_id BIGINT UNSIGNED NOT NULL,
    discount_percentage INT NOT NULL
);
