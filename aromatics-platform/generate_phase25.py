import os
import re

base_platform = "g:/ChuyenNganh/ChuyenNganh8/MSS301/Moc-Huong-Shop/aromatics-platform"
catalog_dir = f"{base_platform}/catalog-service"

# 1. Add dependency
pom_path = f"{catalog_dir}/pom.xml"
graphql_dep = """
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-graphql</artifactId>
        </dependency>
"""
with open(pom_path, "r", encoding="utf-8") as f:
    pom_content = f.read()
if "spring-boot-starter-graphql" not in pom_content:
    pom_content = re.sub(r'(</dependencies>)', graphql_dep + r'\1', pom_content, 1)
    with open(pom_path, "w", encoding="utf-8") as f:
        f.write(pom_content)

# 2. Add GraphQL Schema
graphql_dir = f"{catalog_dir}/src/main/resources/graphql"
os.makedirs(graphql_dir, exist_ok=True)
schema_content = """
type Query {
    productById(id: ID!): Product
    allProducts: [Product]
}

type Product {
    id: ID!
    name: String!
    description: String
    price: Float
}
"""
with open(f"{graphql_dir}/schema.graphqls", "w", encoding="utf-8") as f:
    f.write(schema_content)

# 3. Add GraphQl Controller mappings
controller_path = f"{catalog_dir}/src/main/java/com/minhtriet/se3979/catalogservice/controller/ProductController.java"
with open(controller_path, "r", encoding="utf-8") as f:
    ctrl_content = f.read()

if "org.springframework.graphql.data.method.annotation.QueryMapping" not in ctrl_content:
    ctrl_content = ctrl_content.replace(
        "import org.springframework.web.bind.annotation.*;",
        "import org.springframework.web.bind.annotation.*;\nimport org.springframework.graphql.data.method.annotation.QueryMapping;\nimport org.springframework.graphql.data.method.annotation.Argument;"
    )
    
    graphql_methods = """
    @QueryMapping
    public ProductResponse productById(@Argument String id) {
        return productService.getProduct(id);
    }

    @QueryMapping
    public List<ProductResponse> allProducts() {
        return productService.getAllProducts();
    }
"""
    # Insert before the last closing brace
    ctrl_content = re.sub(r'}\s*$', graphql_methods + "\n}", ctrl_content)
    with open(controller_path, "w", encoding="utf-8") as f:
        f.write(ctrl_content)

print("Phase 25 GraphQL logic generated.")
