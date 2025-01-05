

Tôi sẽ giúp bạn tạo file `format_data.md`:

```markdown
# Format Data Guide

## 1. Input Data Format

### 1.1. JSON Format
```json
[
    {
        "content": "Nội dung văn bản...",
        "link": "https://example.com/page1",
        "date": "19 August 2024",  // optional
        "metadata": {              // optional
            "source": "web",
            "category": "news"
        }
    }
]
```

### 1.2. MongoDB Format
```json
{
    "_id": "unique_id",
    "page_content": "Nội dung văn bản...",
    "source": "https://example.com",
    "date": "2024-08-19",
    // các trường metadata khác
}
```

### 1.3. CSV Format
```csv
content,link,date
"Nội dung văn bản...","https://example.com","19 August 2024"
```

## 2. Processing Steps

1. **Text Chunking**:
   - Chunk size: 350 tokens
   - Overlap: 50 tokens
   - Loại bỏ chunks trùng lặp

2. **Vector Embedding**:
   - Model: hiieu/halong_embedding
   - Vector size: 768 dimensions
   - Distance metric: COSINE

## 3. Qdrant Storage Format

### 3.1. Collection Configuration
```json
{
    "name": "cmc_final_db",
    "vectors_config": {
        "size": 768,
        "distance": "Cosine"
    }
}
```

### 3.2. Point Format
```json
{
    "id": 123,                    // Unique ID (auto-increment)
    "vector": [                   // 768-dimensional vector
        0.123, 0.456, ..., 0.789
    ],
    "payload": {
        "page_content": "Nội dung chunk văn bản...",
        "metadata": {
            "link": "https://example.com",
            "date": "19 August 2024",
            "source": "web",
            // các metadata khác
        }
    }
}
```

## 4. Example Usage

### 4.1. Add Single Document
```python
doc = Document(
    page_content="Nội dung văn bản...",
    metadata={
        "link": "https://example.com",
        "date": "19 August 2024"
    }
)
vector_db.add_documents([doc])
```

### 4.2. Batch Upload
```python
docs = [
    Document(
        page_content=content,
        metadata={"link": link, "date": date}
    )
    for content, link, date in data
]
vector_db.add_documents(docs)
```

## 5. Validation Rules

1. **Required Fields**:
   - page_content: Không được trống
   - id: Unique, auto-increment

2. **Optional Fields**:
   - date: Format "DD Month YYYY"
   - link: Valid URL
   - metadata: Additional key-value pairs

3. **Constraints**:
   - Vector size: Phải đúng 768 chiều
   - Distance metric: COSINE
   - Chunk size: 250-350 tokens
```

File này mô tả:
1. Các format input được chấp nhận
2. Quá trình xử lý data
3. Format lưu trữ trên Qdrant
4. Cách sử dụng
5. Các quy tắc validation

Bạn có thể thêm hoặc sửa đổi theo nhu cầu cụ thể của dự án.
